# EX1:
# s = input("s= ")
# sn = s.replace(s[0],"")
# print(f"Dupa stergerea literei {s[0]} sirul obtinut este {sn} de lungime {len(sn)}")
# print("Dupa stergerea literei {} sirul obtinut este {} de lungime {}".format(s[0],sn,len(sn)))
# print("Dupa stergerea literei {0} sirul obtinut este {1} de lungime {2}".format(s[0],sn,len(sn)))
# print("Dupa stergerea literei {litera} sirul obtinut este {sirnou} de lungime {lung}".format(litera=s[0],sirnou=sn,lung=len(sn)))

# EX2:

# V1:
# s = input("sir = ")
# subsir = input("subsir = ")
#
# print("Pozitiile pe care se afla subsirul sunt: ", end="")
# poz = s.find(subsir)
# while poz != -1:
#     print(poz, end=" ")
#     poz = s.find(subsir, poz + len(subsir))

# #################################

# V2:
# s = input("sir = ")
# subsir = input("subsir = ")
#
# print("Pozitiile pe care se afla subsirul sunt: ", end="")
#
# poz = -len(subsir)
#
# while True:
#     try:
#         poz = s.index(subsir, poz + len(subsir))
#         print(poz, end=" ")
#     except:
#         print("Gata")
#         break

# EX3:
# s = input("s = ")
# i = 0
# while i < len(s)-i:
#    print(s[i:len(s)-i].center(len(s),"*"))
#    #print(s[i:j].rjust(len(s)))
#    i+=1

# EX4:
# s = input("s= ")
# cr = input("corect= ")
# gr = input("greseala= ")
# s1 = s.replace(gr, cr)
# print(s1)
# k = s.count(gr)
# s1 = s.replace(gr, cr, 2)
# print(s1)
# if (k > 2):
#     print("textul contine prea multe greseli, doar 2 au fost corectate")

# EX5:
# sir="ana re are  meremere  si  pere si re"
# s="re"
# t="pe"
# L=sir.split()
# print(L)
# for i in range(len(L)):
#    if L[i]==s:
#        L[i]=t
# # print(L)
# Rez=" ".join(L)
# print(Rez)

# EX6:

# a)
# prop = "1G10o4l"
# # 1G10o4l
# length = len(prop)
# lista = []
# nr_cifre = 0
# for i in range(len(prop)):
#     if prop[i].isdigit():
#         nr_cifre += 1
#     elif prop[i].isalpha():
#         nr = int(prop[i - nr_cifre:i])
#         s = prop[i] * nr
#         lista += [s]
#         nr_cifre = 0
# print(lista)
# rez = "".join(lista)
# print(rez)

# b)
# prop = "Goooooooooollll"
# nr_litere = 0
# litera_curenta = prop[0]
# rez = ""
# for i in range(len(prop)):
#     if prop[i] == litera_curenta:
#         nr_litere += 1

# EX7:

# prop = "Astăzi am cumpărat pâine de 5 RON, pe lapte am dat 10 RON, iar de 15 RON am cumpărat niște cașcaval. De asemenea, mi-am cumpărat și niște papuci cu 50 RON!"
# ls = prop.split()
# ls_nou = [int(x) for x in ls if x.isdigit()]
# suma = 0
# for x in ls_nou:
#     suma += x
# print(suma)

# EX8:
# def checklungime(x):
#     if len(x) < 3:
#         return 0
#     else:
#         return 1
#
# def checkprimalit(x):
#     return x.isupper()
#
# def checkliteremari(x):
#     for i in range(1,len(x)):
#         verif = x[i].islower()
#         if verif == False:
#             return False
#
#     return True
# s = input("sir = ")
# ls = s.split()
# nume = ls[0]
# prenume = ls[1]
# lsnumev = nume.split("-")
# lsprenumev = prenume.split("-")
# c = 0
#
# if len(ls)>2:
#     print("Nu este un nume corect")
# else:
#     if len(lsnumev)>2 or len(lsprenumev)>2:
#         print("Nu este un nume corect")
#     else:
#         for i in lsnumev:
#             verif1 = checkprimalit(i[0])
#             verif2 = checklungime(i)
#             verif3 = checkliteremari(i)
#             if verif1 == False or verif2 == 0 or verif3 == False:
#                 print("Nu este un nume corect")
#                 c = 1
#                 break
#         if c == 0:
#             for i in lsprenumev:
#                 verif1 = checkprimalit(i[0])
#                 verif2 = checklungime(i)
#                 verif3 = checkliteremari(i)
#                 if verif1 == 0 or verif2 == 0 or verif3 == 0:
#                     print("Nu este un nume corect")
#                     c = 1
#                     break
#             if c == 0:
#                 print("Este Nume Complet si Corect")


# EX9:

# a)
# text = input("Sir de criptat = ")
# ls = [ord(x) for x in text]
# k = int(input("k = "))
# for i in range(len(ls)):
#     if ls[i] != 32:
#         if 65 <= ls[i] <= 90:
#             ls[i] += k
#             if ls[i] > 90:
#                 while ls[i] > 90:
#                     ls[i] -= 26
#
#         elif 97 <= ls[i] <= 122:
#             ls[i] += k
#             if ls[i] > 122:
#                 while ls[i] > 122:
#                     ls[i] -= 26
# ls = [chr(x) for x in ls]
# ls = "".join(ls)
# print(ls)

# b)
# k = int(input("k = "))
# text = input("Sir criptat = ")
# ls = [ord(x) for x in text]
# for i in range(len(ls)):
#     if ls[i] != 32:
#         if 65 <= ls[i] <= 90:
#             ls[i] -= k
#             if ls[i] < 65:
#                 while ls[i] <65:
#                     ls[i] += 26
#
#         elif 97 <= ls[i] <= 122:
#             ls[i] -= k
#             if ls[i] < 97:
#                 while ls[i] < 97:
#                     ls[i] += 26
# ls = [chr(x) for x in ls]
# ls = "".join(ls)
# print(ls)


# EX10:
# cuv1 = input("Primul cuvant: ")
# cuv2 = input("Al doliea cuvant: ")
# ls1 = [ord(i) for i in cuv1]
# ls2 = [ord(i) for i in cuv2]
# ls1.sort()
# ls2.sort()
# if ls1 == ls2:
#     print(f"Cuvintele '{cuv1}' si '{cuv2}' sunt anagrame!")
# else:
#     print(f"Cuvintele '{cuv1}' si '{cuv2}' NU sunt anagrame!")\

# EX11:

# a)
# text = input("Text: ")
# text = text.replace("a", "apa")
# text = text.replace("e", "epe")
# text = text.replace("i", "ipi")
# text = text.replace("o", "opo")
# text = text.replace("u", "upu")
# text = text.replace("A", "Apa")
# text = text.replace("E", "Epe")
# text = text.replace("I", "Ipi")
# text = text.replace("O", "Opo")
# text = text.replace("U", "Upu")
# print(text)
#
# text = text.replace("apa", "a")
# text = text.replace("epe", "e")
# text = text.replace("ipi", "i")
# text = text.replace("opo", "o")
# text = text.replace("upu", "u")
# text = text.replace("Apa", "A")
# text = text.replace("Epe", "E")
# text = text.replace("Ipi", "I")
# text = text.replace("Opo", "O")
# text = text.replace("Upu", "U")
# print(text)

# b)
# s = input("Text: ")
# s = s.replace(" ", "-")
# ls = s.split(sep= '-')
# print(ls)
# for i in range(len(ls)):
#     ultima = ls[i][len(ls[i])-1]
#     sir = ultima + "p" + ultima
#     ls[i] = ls[i].replace(ultima, sir)
# print(ls)