# Proiect_Criptare_Decriptare_XOR

Membrii echipei: Militaru Mihai-Alexandru, Hutan Mihai-Alexandru.

Cerinta este enuntata in Proiect 0x00.

Partea 1 a fost scrisa in totalitate de Militaru Mihai-Alexandru.

Partea 2 a fost scrisa in echipa, partea de brute-force fiind scrisa de catre Militaru Mihai-Alexandru, iar partea de decriptare fara a cunoaste inputul si nici parola a fost scrisa de mine.

# Partea 1:

Fisierele sursa encrypt.py, decrypt.py, input.txt si output

Pentru criptare am folosit comanda:

python2 encrypt.py nume_parola input.txt output

Pentru decriptare am folosit comanda:

python2 decrypt.py output nume_parola input_recuperat.txt

# Partea 2:

Numele echipei: Pythoneers

Numele echipei adverse: Led xorllin

Link repository al echipei adverse: https://github.com/Meepo39-1/ProiectASC

Parola echipei adverse este: "trivialmente"

Pentru aflarea parolei cu ajutorul fisierului inputul_adversarilor am folosit metoda brute-force si proprietatea parolei de a fi intre 10 si 15 caractere, observand in consola sirul care se repeta, acela fiind parola. Pentru verificare am decriptat prin metoda folosita de adversarii nostri cu parola obtinuta de noi si am ajuns la textul lor initial. 
Aceasta metoda este prezenta in fisierul brute_force_cracking.py.

Pentru aflarea parolei doar cu ajutorul fisierului binar outputul_adversarilor, am luat toate variantele posibile de lungime a parolei (de la 10 la 15) si am folosit operatia XOR intre codurile ascii ale output.ului adversarilor (din 10 in 10, din 11 in 11 ... din 15 in 15) si codurile ascii ale caracterelor posibile in parola (cifre, litere mici si litere mari). Rezultatul era un caracter ascii pe care il cautam intr-o multime de coduri ascii ale caracterelor intalnite in fisierul text_mare_literatura_romana_custom (fisier ce contine un numar mare de diferite texte literare din literatura). Daca rezultatul era in acea multime, il afisam, altfel opream fortat loop.ul si afisam "Nu este bun".  

Analizand print.ul in urma rularii fisierului decriptare_doar_cu_outputul_adversarilor.py am observat ca doar caracterul 't' poate fi prima litera din parola si ca parola are lungimea egala cu 12.

Stiind ca lungimea parolei este 12 cautam si restul caracterelor din parola modificand putin codul initial (detalii in comentariile codului).

Pe parcursul acestui proces pentru unele pozitii din parola am observat ca un singur caracter este posibil, dar in altele afisarea imi arata ca niciun caracter nu este bun pentru acea pozitie. Folosind oprirea fortata se observa ca anumite caractere treceau mult mai multe teste fata de celelalte si presupuneam ca acela este caracterul din parola pe pozitia respectiva (eroarea apare din cauza multimii create de noi care nu poate fi perfecta pentru orice text literar, insa foarte apropiata). 

Astfel, pe parcursul codului si al afisarilor am regasit parola "trivialmente" pe care am si verificat-o ulterior cu algoritmul de decriptare al oponentilor si ne-a rezultat un text literar pe care ulterior l-am criptat cu parola "trivialmente" si rezultatul a fost exact output.ul oponentilor, fapt ce a confirmat corectitudinea cheii.
