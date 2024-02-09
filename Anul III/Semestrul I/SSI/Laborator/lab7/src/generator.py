def generate_input_txt_file(number: int, word: str) -> None:
    with open("input.txt", "w") as w:
        for i in range(number):
            w.write(word + str(i) + "\n")


if __name__ == '__main__':
    generate_input_txt_file(1000000, "test")
