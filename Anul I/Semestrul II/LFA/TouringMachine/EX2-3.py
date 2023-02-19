# AUTORI:
# Hutan Mihai-Alexandru - grupa 143
# Totolici Alexandru-Gabriel - grupa 143
# Stanciu Ioan Carol - grupa 143


import copy
import sys


# In urmatoarea functie se extrag datele din fiecare parte a config file-ului si sunt introduse intr-o lista
# care mai apoi este returnata


def get_part(name, lista):  # name = numele partii pe care o cautam, lista = lista de linii din fisierul config
    templist = []  # lista goala in care vom introduce elementele dorite
    valid = False  # variabila booleana in care verificam daca intalnim partea de config dorita.
    for line in lista:  # parsam liniile din lista transmisa ca parametru
        if line == name + ':':  # verificam daca partea cautata este in linia curenta
            valid = True
            continue  # sarim urmatorul pas in for
        if line == 'end':
            valid = False  # oprim transcrierea cu acest False 
        if valid:
            templist.append(line)  # copiem liniile dorite in lista temporara
    return templist  # returnam lista temporara


# In primul rand vrem sa mentionam motivul pentru care am creat validarea si functia load in aceeasi functie.
# Daca ar fi fost sa le facem separat, ar fi insemnat sa parsam de doua ori fisierul si sa extragem datele pe care mai
# apoi sa le verificam, lucru care ar fi fost ineficient.

# Asadar am integrat amebele functii in una singura, astfel in cazul in care config-file-ul este invalid
# returnam 1, 1, 1, 1, 1, lucru pe care il verificam ulterior in main. Cazul in care config-file-ul este valid
# se face load la date, respectiv lista de state-uri, lista sigma, lista gamma, lista tranzitiilor, lista starilor
# de start (trebuie sa fie 1 si numai 1, lucru verificat in functie) si lista starilor finale.

# Bineinteles, toate aceste date sunt transmise daca si numai daca corespund standard-ului impus de noi asupra
# configurarilor acceptate.

# Standardele stabilite si verificate:
# 1. Fiecare parte din config va incepe chiar cu denumirea partii respective, urmata de ':'. (exemplu: Sigma:)
# si se va termina cu End. (config-file-ul acceptat nu este case sensitive)
# 2. Starile, literele din Sigma, literele din Gamma si tranzitiile sunt scrise una cate una pe linii.
# 3. Starile finale trebuie urmate de string-ul 'final', iar starea de start trebuie sa fie urmata de 'start'.
# 4. Elementele ce compun o tranzitie trebuie sa fie separate prin spatiu, si sunt de forma:
#               STARE1 LITERA1 STARE2 LITERA2 L/R
# , unde stare1 reprezinta starea curenta, iar in momentul in carea head-ul arata spre o casuta cu valoarea litera1
# ne vom muta in stare2, scriind in casuta spre care arata head-ul litera2, iar mai apoi mutand head-ul cu o pozitie
# mai la stanga in cazul L, sau mai la dreapta in cazul R, tinand cont de pozitia de start a tape-ului si de lungimea
# input-ului introdus in tape.
# 5. Prima stare de final va fi cea de acceptare, iar cea dea doua va fi cea de reject.


def validation_and_load(fisier):  # fisier = numele fisierului pe care vrem sa-l validam si transmite 
    templist = []  # lista goala
    if len(fisier) > 1:
        file = open(fisier, 'r')
    else:
        print("Fisierul nu exista!")
        return 1, 1, 1, 1, 1, 1

    for line in file:
        line = line.strip().lower()  # dam strip spatiilor goale si lower pentru a avea un validator case insesitive

        if len(line) > 0:
            templist.append(line)  # adaugam doar liniile care nu sunt goale

    tempstates = get_part('states', templist)  # generam o lista temporara de stari
    sigma = get_part('sigma', templist)  # generam o lista de simboluri din alfabetul sigma
    gamma = get_part('gamma', templist)  # generam o lista de simboluri din alfabetul gamma
    transitions = get_part('transitions', templist)  # generam lista tranzitiilor

    for x in sigma:  # verificam daca toate simbolurile din sigma se afla si in gamma
        if x not in gamma:
            return 1, 1, 1, 1, 1, 1

    if len(tempstates) == 0 or len(sigma) == 0 or len(gamma) == 0 or len(transitions) == 0:
        print('Invalid!')  # daca cel putin o lista se intoarce goala atunci afisam invalid
        return 1, 1, 1, 1, 1, 1

    start_state = []  # lista goala in care vom retine starea de start
    final_states = []  # lista goala in care vom retine starile finale
    states = []  # lista goala in care vom retine starile fara a mai avea cuvintele suplimentare specifice starilor
    # finale si starii de start.

    for state in tempstates:
        state = state.split()
        if len(state) > 1:
            if state[1] == 'final':
                final_states.append(state[0])
            elif state[1] == 'start':
                start_state.append(state[0])
        states.append(state[0])  # retinem doar primul cuvant din fiecare elem din lista de tempstates

    if len(start_state) != 1 or len(final_states) == 0:  # verificam daca exista doar 1 si numai 1 stare de start,
        # si daca au fost gasite stari finale, cel putin una.
        print('Nu exista stare de start sau final!')
        return 1, 1, 1, 1, 1, 1

    for transition in transitions:  # verificam elementele ce contin o tranzitie,
        # daca apartin listei states,gamma,states,gamma,['l','r'] exact in aceasta ordine.
        temptrans = transition.split()
        if (temptrans[0] not in states) or (temptrans[1] not in gamma) or (temptrans[2] not in states) or (temptrans[3]
                                                                                                           not in gamma) or (
                temptrans[4] not in ['l', 'r']):
            print('Tranzitiile nu sunt corecte!')
            return 1, 1, 1, 1, 1, 1

    # daca functia nu a fost oprita pana in acest moment de niciun return, inseamna ca fisierul config este valid,
    # asadar returnam datele necesare.
    return states, sigma, gamma, transitions, start_state, final_states


def simulator(user_input, start_state, final_states, transitions):
    # user_input = input de la tastatura, start_state = starea de inceput,
    # final_states = lista starilor finale, transitions = lista tranzitiilor
    accept = final_states[0]  # retinem in aceasta variabila starea de acceptare
    reject = final_states[1]  # retinem in aceasta variabila starea de reject
    current = start_state[0]  # initializam starea curenta cu starea de start
    tape1 = [x for x in user_input]  # initializam tape1
    tape1.append('_')  # adaugam '_' la final-ul tape-ului pentru a stii unde se termina input-ul
    tape2 = copy.deepcopy(tape1)  # copiem tape1 in tape2

    for x in user_input:  # verificam daca simbolurile din input apartin multimii sigma
        if x not in sigma:
            print('Input gresit! Caractere care nu sunt in Sigma!')
            return
    i = 0  # index care arata unde este head-ul

    while (current != accept) and (current != reject):  # cat timp nu a ajuns in stare de accept sau reject
        for transition in transitions:  # parcurgem tranzitiile
            transition = transition.split()  # obtinem o lista de elemente ale tranzitiei curente
            if transition[0] == current:  # daca primul element este starea curenta
                if tape1[i] == transition[1]:  # daca litera pe care se afla head-ul corespunde cu elementul 2
                    current = transition[2]  # schimbam starea curenta
                    tape1[i] = transition[3]  # scriem noua litera pe tape1
                    tape2[i] = transition[3]  # scriem noua litera pe tape2 (tape de backup)
                    if transition[4] == 'l' and i != 0:  # daca elementul pe poz 4 este l si nu ne aflam in capatul
                        # din stanga al tape-ului ne mutam cu head-ul o casuta mai la stanga
                        i -= 1
                    elif transition[4] == 'r' and i < len(tape1) - 1:  # daca elementul pe poz 4 este r si nu
                        # ne aflam in capatul din dreapta al tape-ului ne mutam cu head-ul o casuta mai la dreapta
                        i += 1

    if tape1 != tape2:  # verificam integritatea lui tape1 comparandu-l cu tape2
        print('Error occured!')
    else:
        if current == accept:  # daca s-a terminat in stare de acceptare
            print('Accepted!')
            return
        elif current == reject:  # daca s-a terminat in stare de reject
            print('Rejected')
            return


states, sigma, gamma, transitions, start_state, final_states = validation_and_load(sys.argv[1])
# states, sigma, gamma, transitions, start_state, final_states = validation_and_load('EX2-3-CONFIG.txt')
# states, sigma, gamma, transitions, start_state, final_states = validation_and_load('EX4-CONFIG.txt')
if [states, sigma, gamma, transitions, start_state, final_states] != [1, 1, 1, 1, 1, 1]:
    # daca ar fi fost egale ar fi insemnat ca fisierul de config este invalid, deci nu avea rost citirea unui input
    user_input = input("INPUT: ")
    simulator(user_input, start_state, final_states, transitions)
