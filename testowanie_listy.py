class Lista():
  def __init__(self, nazwaPliku, elementy = []):
    self.nazwaPliku = nazwaPliku
    self.plik = open(nazwaPliku, 'a') 
    for element in elementy:
      self.plik.write(str(element) + "\n")
  
  def __getitem__(self, klucz):
    self.plik = open(self.nazwaPliku)
    self.plikJakoLista = self.plik.readlines() 
    return self.plikJakoLista[klucz]

  def __setitem__(self, klucz, wartosc):
    self.plik = open(self.nazwaPliku, 'r')
    self.plikJakoLista = self.plik.readlines() 
    self.plikJakoLista[klucz] = str(wartosc) + '\n' 
    self.plik = open(self.nazwaPliku, 'w')
    self.plik.writelines(self.plikJakoLista)
    return

  def append(self, element):
    self.plik = open(self.nazwaPliku, 'a')
    self.plik.write(str(element) + '\n')
    return

  def __str__(self):
    self.plik = open(self.nazwaPliku)
    self.plikJakoLista = plik.readlines() 
    self.listaDoWyswietlenia = pprint.pformat(self.plikJakoLista) 
    return self.listaDoWyswietlenia
  
  def clear(self):
    self.plik = open(self.nazwaPliku, 'w') 
    self.plik.write("")  
    return

lista = Lista("lista_hasel.txt", ["kacper", "jest", "zajebisty"]) 
lista.clear()
lista.append("dodawany element") 
print(lista[2])
lista[2] = "najlepszy"  