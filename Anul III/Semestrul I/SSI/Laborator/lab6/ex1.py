def lfsr(coefficients, state):
    period = 0
    initial_state = state.copy()
    output = []
    output.append(state[0])

    print(state)

    while True:
        # Varianta 1
        feedback = sum(c * s for c, s in zip(coefficients, state)) % 2
        state = [feedback] + state[:-1]  # Adaugam feedback-ul la inceputul listei si eliminam ultimul element

        # Varianta 2
        # feedback = sum(c * s for c, s in zip(coefficients, state[::-1])) % 2
        # state = state[1:] + [feedback]

        period += 1
        print(state)

        output.append(state[0])

        if state == initial_state:
            break

    print("Secvența de ieșire este:", output)
    return period


if __name__ == "__main__":
    # Citirea lungimii registrelor de la tastatură
    L = int(input("Introduceți lungimea registrelor (L): "))

    # Citirea coeficienților și stării inițiale de la tastatură
    coefficients = [int(input(f"Introduceți coeficientul c{i + 1}: ")) for i in range(L)]
    state = [int(input(f"Introduceți starea inițială s{i}: ")) for i in range(L)]

    # Generarea și afișarea secvenței de ieșire și valoarea perioadei
    period = lfsr(coefficients, state)
    print(f"Valoarea perioadei este: {period}")
