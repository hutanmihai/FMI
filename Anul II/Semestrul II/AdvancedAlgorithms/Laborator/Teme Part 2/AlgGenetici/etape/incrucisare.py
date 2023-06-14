def incrucisare(cromozom1: str, cromozom2: str, punct: int) -> tuple:
    return (
        cromozom1[:punct] + cromozom2[punct:],
        cromozom2[:punct] + cromozom1[punct:],
    )


if __name__ == "__main__":
    lungime_cromozomi = int(input())
    cromozom1 = input()
    cromozom2 = input()
    punct = int(input())

    incrucisare1, incrucisare2 = incrucisare(cromozom1, cromozom2, punct)

    print(incrucisare1)
    print(incrucisare2)
