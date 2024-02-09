# - Laboratorul 2 -

## Introducere în securitatea criptologie

### 1. Notiuni Generale

- (A) Criptologie ->  (4) Știința care se ocupă de criptanaliză și criptografie.
- (B) Criptografie -> (2) Disciplina care studiază principiile, mijloacele și metodele de transformare a datelor pentru
  a ascunde conținutul lor semantic, a preveni utilizarea lor neautorizată sau a preveni modificarea lor nedetectată.
- (C) Criptanaliza -> (5) Încercarea de a înfrânge protecția criptografice fără o cunoaștere inițială a cheii utilizate
  în furnizarea protecției.
- (D) Confidentialitate -> (1) Asigurarea că informațiile nu sunt dezvăluite entităților neautorizate.
- (E) Integritate -> (6) Protejarea împotriva modificării sau distrugerii necorespunzătoare a informațiilor.
- (F) Disponibilitate -> (3) Asigurarea accesului și utilizării informațiilor în timp util și fiabil.

### 2. Triada Confidentiality, Integrity, Availability (CIA)

- 1 -> C
- 2 -> D
- 3 -> I
- 4 -> C
- 5 -> I

### 3. Adversar Probabilistic Polinomial în Timp (PPT)

- 1 -> Fals
- 2 -> Adevarat
- 3 -> Fals

### 4. Funcții neglijabile

- 1 -> neneglijabila
- 2 -> neneglijabila
- 3 -> neneglijabila
- 4 -> neglijabila
- 5 -> neglijabila
- 6 -> neneglijabila

### 5. Securitate computațională

Dați câteva argumente pentru care preferăm să utilizăm securitatea computațională în practică. De ce nu avem ca scop
securitatea perfectă (i.e., indiferent de resursele adversarului un sistem să nu poată fi spart)? Discuție.

- Uneori, implementarea unor măsuri de securitate extrem de riguroase poate limita funcționalitățile unui sistem.
- Obținerea unei securități perfecte este de obicei ineficientă și costisitoare. Resursele necesare pentru a asigura o
  securitate perfecta ar fi uriașe și ar depăși adesea beneficiile obținute din aceasta.

### 6. Atac prin forță brută/căutare exhaustivă

- Câte chei posibile distincte există? -> 2^512 (Cheie de criptare pe 512 biti.)
- Cât timp îi va lua unui adversar găsirea cheii corecte (cazul cel mai nefavorabil) dacă are la dispoziție un
  calculator care testează 2^30 chei pe secundă? -> 2^482 (2^30 chei pe secunda => timp 2^(512-30)=2^482)
- Considerați că este un atac eficient? -> Nu este un atac eficient datorita timpului.
