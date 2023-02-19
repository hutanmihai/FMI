import copy
import sys
# f = open("nda.in", "r")
# f = open("nfa_config_file.in", 'r')
f = open(sys.argv[1], "r")

sigma = []
states = []
transitions = []
temp = []
tail = []
start = []


def set_to_str(set_to_convert, separator="--"):
    return separator.join(map(str, set_to_convert))

for line in f:
    line.strip()
    if line[0] == '#':
        continue
    else:
        line = line.rstrip('\n')
        temporary = line.split('#')
        temp = temporary[0].rstrip()
        temp = temp.split()
        if len(temp)!=0:
            if temp[0].lower().startswith('sigma'):
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
f.close()

finals = []
for state in states:
    if len(state) == 2 and state[1] == "S":
        start.append(state[0])
    if len(state) == 2 and state[1] == "F":
        finals.append(state[0])
    if len(state) == 3 and state[1] == "S" and state[2] == "F":
        finals.append(state[0])
        start.append(state[0])
    elif len(state) == 3 and state[1] == "F" and state[2] == "S":
        finals.append(state[0])
        start.append(state[0])

# @TODO INCEPE CONVERSIA AICI

nfa_states = []
nfa_transitions = []
nfa_sigma = sigma
verify = {}
temptrans = []

nfa_states.append(start.pop())

for state in nfa_states:
    print(nfa_states)
    print(verify)
    if state not in verify.keys():
        for chr in nfa_sigma:
            temp.clear()
            temptrans.clear()
            for transition in transitions:
                if chr in transition and state == transition[0]:
                    temp.append(transition[2])
                    temptrans.append(transition)
            if len(temp) > 1:
                if f'{temp[0]}--{temp[1]}' not in verify.keys():
                    verify[f'{temp[0]}--{temp[1]}'] = [x for x in temp]
                if f'{temp[0]}--{temp[1]}' not in nfa_states:
                    nfa_states.append(f'{temp[0]}--{temp[1]}')
                if [state, chr, f'{temp[0]}--{temp[1]}'] not in nfa_transitions:
                    nfa_transitions.append([state, chr, f'{temp[0]}--{temp[1]}'])
            elif len(temp) == 1:
                if temp[0] not in nfa_states:
                    nfa_states.append(temp[0])
                if temptrans[0] not in nfa_transitions:
                    nfa_transitions.append(temptrans[0])
    else:
        for chr in nfa_sigma:
            stringcreator = ''
            temporary = set()
            for elem in verify[state]:
                curent = set()
                for transition in transitions:
                    if transition[0] == elem and transition[1] == chr:
                        curent.add(copy.deepcopy(transition[2]))
                temporary = temporary.union(curent)
            temporary = sorted(temporary)
            stringcreator = set_to_str(copy.deepcopy(temporary))
            stringcreator.rstrip('--')
            if [state, chr, stringcreator] not in nfa_transitions:
                nfa_transitions.append(copy.deepcopy([state, chr, stringcreator]))
            if stringcreator not in nfa_states:
                nfa_states.append(copy.deepcopy(stringcreator))
            if len(temporary) > 1 and stringcreator not in verify.keys():
                verify[stringcreator] = [x for x in temporary]


print("Sigma:")
print(*nfa_sigma,sep='\n')
print("End")
print("States:")
if nfa_states[0] in finals:
    print(f'{nfa_states[0]}, S, F')
else:
    print(f'{nfa_states[0]}, S')
for i in range(len(nfa_states)):
    if i == 0 : continue
    else:
        x = 0
        for state in states:
            if state[0] == nfa_states[i]:
                if nfa_states[i] in finals:
                    print(f'{nfa_states[i]}, F')
                    x = 1
                else:
                    print(nfa_states[i])
                    x = 1
        if x == 0:
            y = 0
            lista = nfa_states[i].split('--')
            for x in lista:
                if x in finals:
                    print(f'{nfa_states[i]}, F')
                    y = 1
                    break
            if y == 0:
                print(nfa_states[i])
print("End")
print("Transitions:")
for transition in nfa_transitions:
    print(*transition,sep=', ')
print("End")