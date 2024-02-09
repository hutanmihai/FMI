import hashlib

import requests


def hash_file(file_path: str) -> str:
    """
    Return the hash of the file at file_path.
    :param file_path: path to the file
    :return: the hash of the file
    """
    with open(file_path, 'rb') as file:
        return hashlib.sha256(file.read()).hexdigest()


def get_file_info(file_path: str) -> dict | None:
    """
    Return the information about the file at file_path.
    :param file_path: path to the file
    :return: the information about the file
    """
    api_url = 'https://www.virustotal.com/api/v3/files'
    headers = {'x-apikey': 'c05fb51b7c739e4e9559bfed48a4c361f76fcbf9f2566b58ac6dc0ea94ef1607'}
    with open(file_path, 'rb') as file:
        files = {'file': ('malware.png', file)}
        response = requests.post(api_url, headers=headers, files=files)
        if response.status_code == 200:
            file_identifier = hash_file(file_path)
            url = f"https://www.virustotal.com/api/v3/files/{file_identifier}"
            response2 = requests.request("GET", url, headers=headers)
            if response2.status_code == 200:
                return response2.json()
    return None


if __name__ == '__main__':
    file_path = 'malware.png'
    file_info = get_file_info(file_path)
    counter = 0
    if file_info is not None:
        vendors = file_info['data']['attributes']['last_analysis_results']
        for vendor in vendors:
            print(f'{vendor}: {vendors[vendor]["category"]}')
            if vendors[vendor]["category"] == 'malicious':
                counter += 1

        print(f'The file is malicious for {counter} vendors.')
    else:
        print(f'File {file_path} not found.')
