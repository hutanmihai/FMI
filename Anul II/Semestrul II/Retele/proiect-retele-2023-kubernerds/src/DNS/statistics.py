BLOCKED_DOMAINS = "blocked_domains.txt"
FACEBOOK = "facebook"
GOOGLE = "google"
AMAZON = "amazon"
YAHOO = "yahoo"
FBCDN = "fbcdn"

if __name__ == '__main__':
    statistics = {
        FACEBOOK: 0,
        GOOGLE: 0,
        AMAZON: 0,
        YAHOO: 0
    }
    with open(BLOCKED_DOMAINS, "r") as infile:
        for line in infile.readlines():
            for key in statistics.keys():
                if key == FBCDN:
                    if FBCDN in line:
                        statistics[FACEBOOK] += 1
                        break
                elif key in line:
                    statistics[key] += 1
                    break
    with open(f"statistics.txt", "w") as outfile:
        for k, v in statistics.items():
            print(f"{k}: {v}")
            outfile.write(f"{k}: {v}\n")


