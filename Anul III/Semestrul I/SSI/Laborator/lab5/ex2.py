import string
import secrets
import hashlib
import random

'''
Generează  o  parolă  de minim 10 caractere care conține  cel puțin o literă mare, o 
literă mică, o cifră și un caracter special (.!$@).  
La ce poate să folosească într-o aplicație informatică această funcționalitate? Dați 
exemplu de un scenariu de utilizare.
# Utilizare: generare parola sigura.
'''
while True:
    password = ""
    random_integer = random.randint(10, 20)
    for i in range(random_integer):
        password += secrets.choice(string.ascii_letters + string.digits + ".!$@")

    print("Parola generata: ", password)
    break

random_integer = random.randint(32, 40)

'''
Generează un string URL-safe de (cel puțin) 32 caractere.  
La ce poate să folosească într-o aplicație informatică această funcționalitate? Dați 
exemplu de un scenariu de utilizare.
# Utilizare: forgot password, confirm email.
'''
print(f"String url safe generat: {secrets.token_urlsafe(random_integer)}")

'''
Generează un token hexazecimal de (cel puțin) 32 cifre hexazecimale. 
La ce poate să folosească într-o aplicație informatică această funcționalitate? Dați 
exemplu de un scenariu de utilizare (diferit de scenariul anterior). 
# Utilizare: sistem de autentificare.
'''
print(f"Token hexazecimal generat: {secrets.token_hex(random_integer)}")

'''
Verifică dacă 2 secvențe sunt identice sau nu, minimizând riscul unui atac de timp 
(timing attack).
'''
print(
    f"Verificare daca doua secvente sunt identice: {secrets.compare_digest(secrets.token_hex(32), secrets.token_hex(32))}")

'''
Generează o  cheie  fluidă  binară  care ulterior să poată fi folosită pentru criptarea 
unui mesaj de 100 caractere.
# Utilizare: criptarea unui mesaj.
'''
print(f"Cheia generata este: {secrets.token_bytes(100)}")

'''
Stochează parole folosind un modul / o librărie care să ofere un nivel suficient de 
securitate. Ce ați folosit? De ce?
# Utilizare: prevenirea spargerii conturilor
'''
raw_password = "parola"
hashed_password = hashlib.sha256(raw_password.encode('utf-8')).hexdigest()
print(f"Parola criptata: {hashed_password}")
