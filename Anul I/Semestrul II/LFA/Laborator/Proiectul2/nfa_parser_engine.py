import sys

f = open(sys.argv[1], "r")
# f = open("nfa_config_file1.in", 'r')
sigma = []
states = []
transitions = []
temp = []
end = 0
S = 0
F = 0
Sigma = False
States = False
Transitions = False

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
                    end += 1
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
                    end += 1
                    break
                if len(lineStates) != 0:
                    states.append(lineStates.split())
            for ls in states:
                ls[0] = ls[0].rstrip(",")
                if len(ls) == 2:
                    if ls[1] == "S":
                        S += 1
                    elif ls[1] == "F":
                        F = 1
                    else:
                        print("Not good!")
                        exit(0)
                if len(ls) == 3:
                    ls[1] = ls[1].rstrip(",")
                    if ls[1] == "S" and ls[2] == "F":
                        S += 1
                        F = 1
                    elif ls[1] == "F" and ls[2] == "S":
                        S += 1
                        F = 1
                    else:
                        print("Not good!")
                        exit(0)
            if S != 1 or F == 0:
                print("Not good!")
                exit(0)

        elif temp[0].lower().startswith('transitions'):
            Transitions = True
            temp.clear()
            for lineTransitions in f:
                lineTransitions = lineTransitions.rstrip("\n")
                lineTransitions = lineTransitions.strip()
                temporary = lineTransitions.split('#')
                lineTransitions = temporary[0].rstrip()
                if lineTransitions.lower().startswith('end'):
                    end += 1
                    break
                if len(lineTransitions)!= 0:
                    transitions.append(lineTransitions.split())
            for ls in transitions:
                try:
                    ls[0] = ls[0].rstrip(",")
                    ls[1] = ls[1].rstrip(",")
                except:
                    print("Not a complete transition!")
                    exit(0)
        else:
            print("Not a good input!")
            exit(0)

f.close()

# verificam daca elementele din tranzitie fac parte din alfabet, respectiv stari, si daca tranzitia este una valida (stare -> litera -> stare)

for ls in transitions:
    mij = 0
    st = 0
    dr = 0
    if len(ls) != 3:
        print("Not good!")
        exit(0)
    for state in states:
        if ls[0] in state[0]:
            st = 1
        if ls[2] in state[0]:
            dr = 1
        if ls[1] in sigma:
            mij = 1
    if st == 0 or dr == 0 or mij == 0:
        print("Not good!")
        exit(0)

# verificam daca au aparut toate 3 si daca a aparut end de 3 ori

if end != 3 or Sigma == False or States == False or Transitions == False:
    print("Not good!")
    exit(0)

print("GOOD INPUT")