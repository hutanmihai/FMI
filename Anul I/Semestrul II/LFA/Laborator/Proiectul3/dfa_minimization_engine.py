import sys
f = open("dfa_config_file1.in", "r")
# f = open(sys.argv[1], "r")
def set_to_str(set_to_convert, separator="--"):
    return separator.join(map(str, set_to_convert))

sigma = []
states = []
transitions = []
temp = []

# retinem alfabetul, starile si tranzitiile in liste
for line in f:
    line.strip()
    if line[0] == '#':
        continue
    else:
        line = line.rstrip('\n')
        temporary = line.split('#')
        temp = temporary[0].rstrip()
        temp = temp.split()
        if temp[0].lower().startswith('sigma'):
            Sigma = True
            temp.clear()
            for lineSigma in f:
                lineSigma = lineSigma.strip('\n')
                lineSigma = lineSigma.strip()
                temporary = lineSigma.split('#')
                lineSigma = temporary[0].rstrip()
                if lineSigma.lower().startswith('end'):
                    break
                if len(lineSigma) != 0:
                    sigma.append(lineSigma)

        elif temp[0].lower().startswith('states'):
            States = True
            temp.clear()
            for lineStates in f:
                lineStates = lineStates.rstrip("\n")
                lineStates = lineStates.strip()
                temporary = lineStates.split('#')
                lineStates = temporary[0].rstrip()
                if lineStates.lower().startswith('end'):
                    break
                if len(lineStates) != 0:
                    states.append(lineStates.split())
            for ls in states:
                ls[0] = ls[0].rstrip(",")
                if len(ls) == 3:
                    ls[1] = ls[1].rstrip(",")

        elif temp[0].lower().startswith('transitions'):
            Transitions = True
            temp.clear()
            for lineTransitions in f:
                lineTransitions = lineTransitions.rstrip("\n")
                lineTransitions = lineTransitions.strip()
                temporary = lineTransitions.split('#')
                lineTransitions = temporary[0].rstrip()
                if lineTransitions.lower().startswith('end'):
                    break
                if len(lineTransitions) != 0:
                    transitions.append(lineTransitions.split())
            for ls in transitions:
                ls[0] = ls[0].rstrip(",")
                ls[1] = ls[1].rstrip(",")

finals = []

# facem lista pentru toate starile finale si o variabila pentru starea de start

for state in states:
    if len(state) == 2 and state[1] == "S":
        start = state[0]
    if len(state) == 2 and state[1] == "F":
        finals.append(state[0])
    if len(state) == 3 and state[1] == "S" and state[2] == "F":
        finals.append(state[0])
        start = state[0]
    elif len(state) == 3 and state[1] == "F" and state[2] == "S":
        finals.append(state[0])
        start = state[0]

f.close()

matrix = []

for i in range(1,len(states)):
    row = []
    for j in range(0,i):
            if states[i][0] in finals and states[j][0] not in finals:
                row.append(1)
            elif states[j][0] in finals and states[i][0] not in finals:
                row.append(1)
            elif i==j:
                row.append(5)
            else:
                row.append(0)
    matrix.append(row)

d = {}
for i in range(len(matrix)):
    d[states[i+1][0]] = []
    for j in range(len(matrix[i])):
        d[states[i+1][0]].append([states[j][0], matrix[i][j]])
d[states[0][0]] = []
for i in range(len(matrix)):
    d[states[0][0]].append([states[i+1][0],matrix[i][0]])

change = True
while change:
    change = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                for letter in sigma:
                    one = []
                    two = []
                    for state in states:
                        if [states[i+1][0], letter, state[0]] in transitions:
                            one = [states[i+1][0], letter, state[0]]
                        if [states[j][0], letter, state[0]] in transitions:
                            two = [states[j][0], letter, state[0]]
                    lista = d.get(one[2])
                    for l in range(len(lista)):
                        if lista[l][0] == two[2] and lista[l][1] == 1:
                            matrix[i][j] = 1
                            change = True
    d = {}
    for i in range(len(matrix)):
        d[states[i + 1][0]] = []
        for j in range(len(matrix[i])):
            d[states[i + 1][0]].append([states[j][0], matrix[i][j]])
    d[states[0][0]] = []
    for i in range(len(matrix)):
        d[states[0][0]].append([states[i + 1][0], matrix[i][0]])

dfa_minimized_states = []
dfa_minimized_states_new = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            if len(dfa_minimized_states_new) != 0:
                change = False
                for k in range(len(dfa_minimized_states_new)):
                    if states[i+1][0] in dfa_minimized_states_new[k] and states[j][0] in dfa_minimized_states_new[k]:
                        change = True
                        continue
                    elif states[i+1][0] in dfa_minimized_states_new[k]:
                        dfa_minimized_states_new[k].append(states[j][0])
                        change = True
                    elif states[j][0] in dfa_minimized_states_new[k]:
                        dfa_minimized_states_new[k].append(states[i+1][0])
                        change = True
                if change is False:
                    dfa_minimized_states_new.append([states[i+1][0],states[j][0]])
            else:
                dfa_minimized_states_new.append([states[i+1][0],states[j][0]])

for i in range(len(dfa_minimized_states_new)):
    curent = set(dfa_minimized_states_new[i])
    curent = sorted(curent)
    dfa_minimized_states.append(set_to_str(curent))

anlist = []
for x in dfa_minimized_states:
    lista = x.split('--')
    for chestie in lista:
        if chestie not in anlist:
            anlist.append(chestie)
for state in states:
   if state[0] not in anlist:
    dfa_minimized_states.append(state[0])

dfa_minimized_finals = []
dfa_minimized_start = []
dfa_minimized_transitions = []
for state in dfa_minimized_states:
    list = state.split('--')
    for x in list:
        if x in finals and state not in dfa_minimized_finals:
            dfa_minimized_finals.append(state)
    for x in list:
        if x in start and state not in dfa_minimized_start:
            dfa_minimized_start.append(state)

for state in dfa_minimized_states:
    list = state.split('--')
    for chr in sigma:
        for transition in transitions:
            if transition[0] == list[0] and transition[1] == chr:
                last = transition[2]
        for state2 in dfa_minimized_states:
            list2 = state2.split('--')
            if last in list2:
                dfa_minimized_transitions.append([state, chr, state2])

print('Sigma:')
for x in sigma:
    print(x)
print('End')
print('States:')
for x in dfa_minimized_states:
    if x in dfa_minimized_start and x in dfa_minimized_finals:
        print(f'{x}, S, F')
    elif x in dfa_minimized_start:
        print(f'{x}, S')
    elif x in dfa_minimized_finals:
        print(f'{x}, F')
    else:
        print(x)
print('End')
print('Transitions:')
for x in dfa_minimized_transitions:
    print(*x, sep=', ')
print('End')