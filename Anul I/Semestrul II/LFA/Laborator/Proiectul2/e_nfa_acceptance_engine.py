import copy
import sys
# f = open("e_nfa_config_file1.in", "r")
# word = input("Word to verify: ")
f = open(sys.argv[1], "r")
word = sys.argv[2]

lsw = []
sigma = []
states = []
transitions = []
temp = []
tail = []
start = []

for x in word:
    lsw.append(x)
for line in f:
    line.strip()
    if line[0] == '#':
        continue
    elif line[0] == '\n':
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
                if len(ls) == 2:
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
                if len(lineTransitions)!= 0:
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

e_nfa_transitions = []
sigma.append('*')
for transition in transitions:
    if transition[1] == '*':
        for transition2 in transitions:
            if transition2[0] == transition[2]:
                e_nfa_transitions.append([transition[0], transition2[1], transition2[2]])
        if transition[0] in start:
            start.append(transition[2])
        if transition[2] in finals:
            finals.append(transition[0])
    else:
        e_nfa_transitions.append(transition)

transitions = e_nfa_transitions
show = 0
nr = 0
lung = len(start)

temptail = []
for elem in start:
    nr += 1
    tail = [[elem]]
    for chr in lsw:
        for i in range(len(tail)):
            rn = tail.pop()
            if chr in sigma:
                for transition in transitions:
                    if transition[0] == rn[len(rn)-1] and transition[1] == chr:
                        rn.append(transition[2])
                        temptail.append(copy.deepcopy(rn))
                        rn.pop()
            else:
                print("Not good word!")
                exit(0)
            rn.clear()
        tail = copy.deepcopy(temptail)
        temptail.clear()
        if not tail:
            break
    for x in tail:
        if x[len(x) - 1] in finals:
            show = 1
            # @TODO PENTRU A VEDEA DRUMUL SE POATE DA PRINT(x) AICI

if show == 0:
    print("Not accepted!")
else:
    print("ACCEPTED")
