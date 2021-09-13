import pyautogui
from selenium import webdriver
import time
import pprint
listaznakow = "abcdefghijklmnoprstuwz1234567890"

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
    self.plikJakoLista = self.plik.readlines() 
    self.listaDoWyswietlenia = pprint.pformat(self.plikJakoLista) 
    return self.listaDoWyswietlenia
  
  def clear(self):
    self.plik = open(self.nazwaPliku, 'w') 
    self.plik.write("")  
    return


def sprawdzanie_czy_przeszlo():
	pass

def wpisz_przez_pyautogui(napisLogin, napisHaslo):
	return False

def wpisz_haslo(length, lista = Lista("lista_hasel.txt"), danyNapis = "", dlugosc = 0):
	dlugosc += 1

	if(dlugosc > length):
		lista.append(danyNapis) # zmiana na moją listę

		return lista # zmiana na moją listę

	for znak in listaznakow:
		nastepnyNapis = danyNapis[:]
		nastepnyNapis += znak 
		wpisz_haslo(length, lista, nastepnyNapis, dlugosc)

	return lista

	
lista_wszystkich_hasel = Lista("lista_hasel.txt")
for i in range(1, 10):
	lista_hasel = wpisz_haslo(i)	
  
powiodlo_sie = False
dane_do_zalogowania = ["login", "haslo"]
for element in lista_wszystkich_hasel:

	print("wpisywanie hasla nr. " + str(element))
	warrtosc_zwracana = wpisz_przez_pyautogui(element) #zmienić na dwa argumenty i je generować tak samo jak haslo
	if(type(wartosc_zwracana) == type(["login", "haslo"])):
		powiodlo_sie = True
		dane_do_zalogowania[0] = wartosc_zwracana[0]
		dane_do_zalogowania[1] = wartosc_zwracana[1]
		break

if(powiodlo_sie == True):
	print("operacja do logowania powiodla sie DANE: " + str(dane_do_zalogowania))
	
print("koniec")