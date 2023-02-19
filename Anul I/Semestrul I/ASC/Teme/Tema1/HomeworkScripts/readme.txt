Testele pentru verificarea temei 

1. Pentru a seta environmentul trebuie sa rulati urmatoarele comenzi: 

$ apt-get update
$ apt-get install python3-pycryptodome xinetd libffi-dev python3-wheel gcc gdb python3-setuptools python3-dev libssl-dev git libc6-dbg python3-pip make gcc-multilib socat
$ pip3 install pwntools

2. Dupa ce ati instalat pachetele de mai sus, trebuie sa va asigurati ca in acelasi folder cu script.py se regasesc cele patru executabile cerinta1, cerinta2, cerinta3, respectiv cerinta4. Atentie, nu este suficient sa aveti doar fisierele .asm, trebuie sa ajungeti din fisiere .asm in executabile. Inainte de a rula scriptul, rulati

$ as --32 cerinta1.asm -o cerinta1.o
$ gcc -m32 cerinta1.o -o cerinta1 

si analog pentru cerinta2.asm, cerinta3.asm si cerinta4.asm. 

3. Rulati scriptul prin comanda 
$ python script.py 

Veti primi in consola un raport referitoare la testele care au fost trecute cu succes, respectiv testele esuate. Pentru fiecare test esuat, puteti vedea inputul primit, ce output ati oferit, respectiv outputul asteptat. 

Daca vreti rezultatele intr-un fisier, puteti rula comanda

$ python script.py > result.txt

4. La cerinta 4 testele i si i + 1 sunt teste perechi. Testele 0 si 1 evalueaza acelasi lucru, la fel 2 si 3, la fel 4 si 5, 6 si 7, 8 si 9. Este suficient sa treceti doar un test din fiecare grupa (i, i + 1) pentru a se considera punctajul maxim pe cerinta respectiva. Acest lucru vine din faptul ca in cerinta i inputul arata

nume_matrice nr_linii nr_coloane nr_linii*nr_coloane_elemente let nume_matrice operand operatie 
unde operand lipseste cand operatie = rot90d 

iar in cerinta i + 1 lipseste nume_matrice de dupa let, adica 

nume_matrice nr_linii nr_coloane nr_linii*nr_coloane_elemente let operand operatie 
unde operand lipseste cand operatie = rot90d 

IMPORTANT! Punctajul obtinut pe aceste teste este estimativ, si pot aparea diferente la evaluarea finala, care va fi pe alte teste. 
