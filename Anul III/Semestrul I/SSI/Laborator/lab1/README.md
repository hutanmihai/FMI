# - Laboratorul 1 -

## Introducere în securitatea sistemelor informatice

### 1.Notiuni Generale

- (A) Adversar -> (3) O entitate (inclusiv un insider) care acționează rău intenționat pentru a compromite un sistem.
- (B) Securitate -> (1) O condiție care rezultă din stabilirea și menținerea măsurilor de protecție care permit unei
  organizații/sistem să își îndeplinească misiunea sau funcțiile critice, în ciuda riscurilor reprezentate de
  amenințări.
- (C) Risc -> (5) O măsură a gradului în care o entitate este amenințată de o eventuală circumstanță sau eveniment.
- (D) Vulnerabilitate -> (2) Slăbiciune într-un sistem informațional, proceduri de securitate ale sistemului, controale
  interne sau implementare care ar fi putea fi exploatate sau declanșate de o sursă de amenințare.
- (E) Securitate Cibernetica -> (4) Capacitatea de a proteja / apăra spațiul cibernetic de atacuri cibernetice.

### 2."The security Mindset"

Vizualizati interviul cu Bruce Schneier, "The security Mindset" [aici](https://youtu.be/eZNzMKS7zjo).

- Security is a mindest. You have to think about security all the time. You have to think about security when you are
  designing the system, when you are implementing the system, when you are using the system.

### 3.Sisteme de numeratie

Q1: Considerați ziua în care v-ați născut la care adăugați valoarea 10. Transformați în binar această valoare. Faceți
transformarea inversă.
A1:

```
7 + 10 = 17 -> (bin) 10001

17/2
8/2
4/2
2/2
1

1 0 0 0 1 -> 1 + 2^4 = 17
```

Q2: Considerați un număr hexazecimal oarecare de 4 cifre. Transformați în binar această valoare. Faceți transformarea
inversă.
A2:

```
ABCD -> 1010 1011 1100 1101

A -> 10 -> 1010
B -> 11 -> 1011
C -> 12 -> 1100
D -> 13 -> 1101

1010 1011 1100 1101 -> ABCD
```

- Tips: Căutați resurse online care vă permit conversia între diferite baze de numerație. Vă vor fi de folos pentru
  următoarele laboratoare.

### 4.Codul ASCII

Q1: Considerați prenumele dumneavoastră, scris cu majuscule. Ce îi corespunde conform codificării ASCII?
A1:

```
MIHAI-ALEXANDRU -> 77 73 72 65 73 45 65 76 69 88 65 78 68 82 85 
```

Q2: Se consideră codificarea ASCII 66 82 65 86 79. Ce cuvânt îi corespunde?
A2: BRAVO

- Tips: Căutați resurse online care vă permit conversia caracterelor în ASCII și invers. Vă vor fi de folos pentru
  următoarele laboratoare.

### 5.Base64

Q1: Considerați numele dumneavoastră, scris cu majuscule. Ce îi corespunde conform codificării Base64?
A1:

```
HUTAN -> SFVUQU4=
```

Q2: Se consideră codificarea Base64 dată de string-ul următor: U3VudCBzdHVkZW50IGxhIEZNSS4=. Ce îi corespunde?
A2: Sunt student la FMI.

- Tips: Căutați resurse online care vă permit conversia în/din Base64. Vă vor fi de folos pentru următoarele
  laboratoare.

### 6.Introducere in malware

Explicați pe scurt fiecare din termenii: malware, virus, dropper, downloader, trojan, spyware, riskware, ransomware,
adware, worm, obfuscare.

Pentru explicarea termenilor, vă puteți folosi de resurse online
precum [link1](https://csrc.nist.gov/glossary/), [link2](https://www.researchgate.net/publication/230674947_Springer_Encyclopedia_of_Cryptography_and_Security).

- malware - software that is specifically designed to disrupt, damage, or gain unauthorized access to a computer system
- virus - a piece of code which is capable of copying itself and corrupts/destroys data in a system
- dropper - a dropper is a kind of Trojan that has been designed to "install"  malware (virus, backdoor, etc.) to a
  computer. The malware code can be contained is contained within the dropper.
- downloader - a downloader is a type of trojan that installs itself to the system and waits until an Internet
  connection becomes available to connect to a remote server or website in order to download additional programs.
- trojan - a type of malicious code or software that looks legitimate but can take control of your computer
- spyware - software that enables a user to obtain covert information about another's computer activities by
  transmitting data secretly from their hard drive.
- riskware - riskware defines any legitimate programs that pose potential risks due to security vulnerability, software
  incompatibility, or legal violations.
- ransomware - a type of malicious software designed to block access to a computer system until a sum of money is paid.
- adware - software that automatically displays or downloads advertising material such as banners or pop-ups when a user
  is online.
- worm - a computer worm is a type of malware that spreads copies of itself from computer to computer.
- obfuscare - programming code is often obfuscated to protect intellectual property or trade secrets, and to prevent an
  attacker from reverse engineering a proprietary software program.

### 7.Masini virtuale

1. Descărcați și instalați un hipervizor (ex.: VirtualBox/VMWare).
2. Descărcați un fișier .iso aferent tipului de sistem de operare.
3. Creați o mașină virtuală și instalați sistemul de operare.
4. Instalați tool-urile pe care le considerați utile (ex.: Procmon, Process Explorer).
5. Setați rețeaua mașinii virtuale în modul Host-Only.
6. Faceți un snapshot la care veți putea reveni oricând.

- Configurați-vă o mașină virtuală cu Windows (orice începând cu Windows 7 este acceptat).

- Alternativă: Folosiți o mașină virtuală creată de Microsoft cu scopul testării IE și
  MSEdge [link](https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/). 
