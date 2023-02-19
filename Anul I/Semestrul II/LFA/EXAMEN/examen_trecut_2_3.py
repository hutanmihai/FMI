import sys


def get_section(name, list_generate):  # se ia fiecare sectiune in parte si se face o lista cu fiecare in parte
    boolean = False  # verifica daca sectiunea este bine definita
    list_section = []  # se considera o lista goala pentru a se adauga ceea ce este in sectiunea respectiva

    for line in list_generate:  # se parcurge lista data ca parametru
        if line == name + ':':  # se verifica daca numele sectiunii este corect si se incepe adaugarea liniilor in lista
            boolean = True
            continue  # trece peste celelalte if-uri si se duce inapoi in for
        if line == "end":  # s-a terminat sectiunea
            boolean = False
        if boolean == True:  # daca inca suntem in sectiune se adauga liniile in lista
            list_section.append(line)
    return list_section  # se returneaza lista corespunzatoare datelor din sectiune


def validate(file_name):  # se valideaza fisierul de intrare
    list_generate = []  # lista cu toate liniile
    if len(file_name) > 1:
        f = open(file_name, 'r')
    else:
        # 0= totul e corect, 1= nu exista fisier, 2=nu avem sectiune, 3= tranzițiile au erori
        # 4= stari finale/initiale definite incorect
        return 1

    for line in f:
        line = line.strip().lower()  # se sparge fiecare linie in mai multe stringuri dupa spatii, iar toate literele
        # se transforma in caractere mici
        if len(line) > 0:  # daca linia nu este goala se adauga in lista
            list_generate.append(line)

    l_states = get_section("states", list_generate)  # se genereaza lista de stari
    l_sigma = get_section("sigma", list_generate)  # se genereaza lista de simboluri din alfabetul input-ului
    l_gamma = get_section("gamma", list_generate)  # se genereaza lista de simboluri din alfabetul benzii
    l_transitions = get_section("transitions", list_generate)  # se genereaza lista da tranzitii

    if len(l_gamma) == 0 or len(l_sigma) == 0 or len(l_states) == 0 or len(
            l_transitions) == 0:  # daca cel putin o lista e goala se intoarce 2
        return 2

    l_start = []  # starea de start
    l_final = []  # stari finale
    l_states_aux = []  # se creeaza o lista care contine doar numele starilor, nu si tipul lor
    for state in l_states:
        state = state.split(" ")  # se separa starile in functie de caracterul spatiu
        if len(state) > 1:  # se verifica daca starea curenta este initiala sau finala si se aduga starile in lista
            if state[1] == 's' and len(l_start) == 0:
                l_start.append(state[0])
            elif state[1] == 'f':
                l_final.append(state[0])
            else:
                return 4
        l_states_aux.append(state[0])  # se adauga in lista auxiliara starea
    l_states = l_states_aux  # se copiaza lista starilor auxiliare in lista de stari

    if len(l_start) == 0 or len(l_final) == 0:  # daca nu exista stare de start sau finala se intoarce 4
        return 4

    trans_ok = True  # se presupune ca tranzitiile sunt bune initial
    for trans in l_transitions:
        tmp = trans.split(" ")  # se separe elementele aferente fiecarei tranzitii

        if (tmp[0] not in l_states) or (tmp[1] not in l_gamma) or tmp[2] not in l_gamma or tmp[3] not in l_states or (
                tmp[4] not in l_gamma and tmp[4] != 'e') or (tmp[5] not in l_gamma and tmp[5] != 'e') or (
                tmp[6] != 'l' and tmp[6] != 'r' and tmp[6] != 'n') or (
                tmp[7] != 'l' and tmp[7] != 'r' and tmp[7] != 'n'):
            trans_ok = False
            # daca primul element din tranzitie nu este in lista de stari sau
            # daca al doilea element nu se afla in limbajul de pe banda sau
            # daca al treilea element nu se afla in limbajul de pe banda sau
            # daca al patrulea element nu este in lista de stari sau
            # daca al cincilea element nu se afla in limbajul benzii si nu este nici 'e' ( nu se modifica banda) sau
            # daca al saselea element nu se afla in limbajul benzii si nu este nici 'e' ( nu se modifica banda) sau
            # daca penultimul element nu este l(left)  sau r (right) sau n(stationare) sau
            # daca ultimul element nu este l(left)  sau r (right) sau n(stationare)
            # inseamna ca tranzitia este incorecta
    if trans_ok == False:
        return 3
    else:
        return 0  # tranzitie buna


# 0= totul e corect, 1= nu exista fisier, 2=nu avem sectiune, 3= tranzițiile au erori
# 4= stari finale/initiale definite incorect

def load_config_file(file_name):  # aceasta functie returneaza listele specifice unei masini Turing sau
    # mesajele corespunzatoare erorilor intalnite
    # (comentariile aferente acestei bucati de cod se regasesc mai sus)
    if validate(file_name) == 0:
        list_generate = []
        if len(file_name) > 1:
            f = open(file_name, 'r')

        for line in f:
            line = line.strip().lower()
            if len(line) > 0:
                list_generate.append(line)

        l_states = get_section("states", list_generate)
        l_sigma = get_section("sigma", list_generate)
        l_gamma = get_section("gamma", list_generate)
        l_transitions = get_section("transitions", list_generate)
        l_start = []
        l_final = []
        l_states_aux = []
        for state in l_states:
            state = state.split(" ")
            if len(state) > 1:
                if state[1] == 's' and len(l_start) == 0:
                    l_start.append(state[0])
                else:
                    if state[1] == 'f':
                        l_final.append(state[0])

            l_states_aux.append(state[0])
        l_states = l_states_aux
        return l_states, l_start, l_final, l_sigma, l_gamma, l_transitions

    # cazurile de erori
    elif validate(file_name) == 1:
        print("Invalid configuration file: Missing file")
        return
    elif validate(file_name) == 2:
        print("Invalid configuration file: Section missing")
        return
    elif validate(file_name) == 3:
        print("Invalid configuration file: Incorrect transitions")
        return
    else:
        print("Invalid configuration file: Incorrect start/final states")
        return


def turing_simulator(input_string, l_start, l_final, l_transitions):
    accept = l_final[0]  # stare de accept
    reject = l_final[1]  # stare de reject
    current_state = l_start[0]  # se porneste de la starea de start
    tape = [x for x in input_string]
    if tape.count('#') == 0:  # caz particular pentru exercitiul 3
        return 'Rejected'
    j = len(tape) - 1  # ultimul caracter al input-ului - locul unde arata initial capul din dreapta
    tape.append('_')  # se adauga spatiu pentru a verifica daca se ajunge in stare de accept
    i = 0  # index care arata unde este capul stang de citire/scriere al masinii

    while current_state != accept and current_state != reject:  # cat timp nu a ajuns in stare de accept, respectiv reject
        for trans in l_transitions:  # se parcurg tranzitiile
            trans = trans.split()  # se sparge fiecare tranzitie in componentele sale
            if trans[0] == current_state:  # daca prima componenta este starea curenta
                if tape[i] == trans[1] and tape[j] == trans[
                    2]:  # daca s-a gasit o tranzitie din starea curenta cu simbolul
                    # la care s-a ajuns cu capul stang su cu simbolul la care
                    # s-a ajuns cu capul drept
                    current_state = trans[
                        3]  # atunci starea curenta va deveni cea care apare pe pozitia a treia in lista de tranzitii
                    if trans[4] != 'e':  # daca se poate scrie ceva pe banda in locul unde arata capul stang
                        tape[i] = trans[
                            4]  # atunci caracterul care trebuie scris in acel spatiu ia locul caracterului existent acolo
                    if trans[5] != 'e':  # daca se poate scrie ceva pe banda in locul unde arata capul drept
                        tape[j] = trans[
                            5]  # atunci caracterul care trebuie scris in acel spatiu ia locul caracterului existent acolo
                    if trans[
                        6] == 'l' and i != 0:  # daca penultimul element este l atunci se decremeneteaza indicele pentru a se deplasa spre stanga capul stang
                        i = i - 1
                    if trans[
                        7] == 'l' and j != 0:  # daca ultimul element este l atunci se decremeneteaza indicele pentru a se deplasa spre stanga capul drept
                        j = j - 1
                    if trans[6] == 'r' and i < len(
                            tape):  # daca penultimul caracter este r si indicele unde se afla capul stang este mai mic decat tape-ul atunci se incrementeaza
                        i = i + 1
                    if trans[7] == 'r' and j < len(
                            tape):  # daca ultimul caracter este r si indicele unde se afla capul drept este mai mic decat tape-ul atunci se incrementeaza
                        j = j + 1
    if current_state == reject:  # daca a ajuns in starea de reject atunci returnam mesaj corespunzator
        return 'Rejected'
    if current_state == accept:  # daca a ajuns in starea de accept atunci returnam mesaj corespunzator
        return 'Accepted'


# main
if load_config_file(sys.argv[1]) != None:
    l_states, l_start, l_final, l_sigma, l_gamma, l_transitions = load_config_file(sys.argv[1])
    input_string = '00#0'
    result = turing_simulator(input_string, l_start, l_final, l_transitions)
    print(result)

# teste pentru functia validate
'''er=validate(sys.argv[1])
print(er)
l_states, l_start, l_final, l_sigma, l_gamma, l_transitions=load_config_file(sys.argv[1])
print(l_states,l_start,l_final,l_sigma,l_gamma,l_transitions)'''
