# - Laboratorul 7 -

## Funcții hash

### 1. Noțiuni introductive

- (a) Amestecarea ingredientelor pentru realizarea unei prăjituri poate fi considerată one-way function -> A
- (b) Funcția hash MD5 este considerată sigură la coliziuni -> F
- (c) SHA256 este o funcție hash cu output pe 256 biți -> A
- (d) Valoarea hash SHA-1 pentru cuvantul „laborator” este 0x4bcc6eab9c4ecb9d12dcb0595e2aa5fbc27231f3 -> A
- (e) Este corect să afirmăm că „o funcție hash criptează” -> F
- (f) O funcție hash folosită pentru stocarea parolelor trebuie să fie rapidă (i.e., să se calculeze rapid H(x) pentru x
  dat) -> F
- (g) Hash-ul (fără salt)-095b2626c9b6bad0eb89019ea6091bd9–corespunde unei parole sigure, care nu ar fi susceptibilă
  spre exemplu la un atac de tip dicționar -> F (parola123 -> decodata folosind MD5)

### 2.Securitatea funcției hash PHOTON-80/20/16

- Generare fisier input.txt cu 1000000 de linii, fiecare linie avand valoarea "test" + numarul liniei
  ```python
  def generate_input_txt_file(number: int, word: str) -> None:
      with open("input.txt", "w") as w:
          for i in range(number):
              w.write(word + str(i) + "\n")
  
  
  if __name__ == '__main__':
      generate_input_txt_file(1000000, "test")
  ```

- Verificare coliziuni
  ```python
  def get_output_lines() -> list:
      with open("output.txt", "r") as r:
          lines = [x.replace("\n", "") for x in r.readlines()][1:]
          lines = [x.split("::::: ")[1] for x in lines]
      return lines
  
  
  def get_output_test_lines() -> list:
      with open("output_test.txt", "r") as r:
          lines = [x.replace("\n", "") for x in r.readlines()][1:]
          lines = [x.split("::::: ")[1] for x in lines]
      return lines
  
  
  if __name__ == '__main__':
      lines = get_output_lines()
      test_lines = get_output_test_lines()
      used = set(test_lines)
      has_collisions = False
      for line in lines:
          if line in used:
              has_collisions = True
              print(line + " has a collision")
          used.add(line)
      if has_collisions:
          print("Collisions found")
      else:
          print("No collisions found")
  ```

Nu a fost gasita nicio coliziune.

### 3. Stocarea parolelor

- 1 -> Nu vom putea determina ulterior ce parola corespunde carui user.
- 2 -> Numele si parola sunt salvate sub forma de hash, lucru care poate duce la coliziuni in cazul in care mai multi
  useri au acelasi username.
- 3 -> Salt-ul ar trebui generat aleatoriu pentru fiecare criptare in parte.
- 4 -> Salt-ul este static, salvat intr-un fisier, ceea ce poate duce la compromiterea parolelor prin atacuri de tip
  rainbow table.
- 5 -> Algoritmul MD5 nu este destinat criptarii parolelor, datorita multiplelor vulnerabilitati gasite in algoritm.
