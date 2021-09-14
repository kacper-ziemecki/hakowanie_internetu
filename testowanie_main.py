import pyautogui
from selenium import webdriver
import time
import pprint
import sys 

listaznakow = "abcdefghijklmnoprstuwz1234567890_-"
	
KOORDYNATY_LOGIN = [-1, -1]
KOORDYNATY_HASLA = [-1, -1]

if(not sys.argv[1:]):
	KOORDYNATY_LOGIN[0] = input("wpisz lokalizację login na osi x") 
	KOORDYNATY_LOGIN[1] = input("wpisz lokalizację login na osi y") 
	KOORDYNATY_HASLA[0] = input("wpisz lokalizację hasła na osi x")
	KOORDYNATY_HASLA[1] = input("wpisz lokalizację hasła na osi y")
	plik_danych = open("lokalizacje.txt", 'w')
	plik_danych.write("KOORDYNATY_LOGIN[0] = " + str(KOORDYNATY_LOGIN[0]) + '\n')
	plik_danych.write("KOORDYNATY_LOGIN[1] = " + str(KOORDYNATY_LOGIN[1]) + '\n')
	plik_danych.write("KOORDYNATY_HASLA[0] = " + str(KOORDYNATY_HASLA[0]) + '\n')
	plik_danych.write("KOORDYNATY_HASLA[1] = " + str(KOORDYNATY_HASLA[1]) + '\n')
	print("dane do zlogkalizowanie elementow login i haslo zostaly podane do programu i zapisane na pliku lokalizaja.txt")
else:
	raise Exception("Nie podajemy rzadnych argumentow do programu (podajemy je poprzez sys.stidn lub pipe - | )")

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


def sprawdzanie_czy_przeszlo():
	pass

def wpisz_przez_pyautogui(napisLogin, napisHaslo):
  return False

def wpisz_haslo(length, lista = Lista("lista_hasel.txt"), danyNapis = "", dlugosc = 0):
	dlugosc += 1

	if(dlugosc > length):
		lista.append(danyNapis)

		return lista

	for znak in listaznakow:
		nastepnyNapis = danyNapis[:]
		nastepnyNapis += znak 
		wpisz_haslo(length, lista, nastepnyNapis, dlugosc)

	return lista

def wpisz_login(length, lista = Lista("lista_login.txt"), danyNapis = "", dlugosc = 0):
	dlugosc += 1

	if(dlugosc > length):
		lista.append(danyNapis) 

		return lista 

	for znak in listaznakow:
		nastepnyNapis = danyNapis[:]
		nastepnyNapis += znak 
		wpisz_login(length, lista, nastepnyNapis, dlugosc)

	return lista
	
lista_wszystkich_hasel = Lista("lista_hasel.txt")
for i in range(1, 2):
	lista_hasel = wpisz_haslo(i)	

lista_wszystkich_login = Lista("lista_wszystkich_login.txt")
for i in range(1, 2):
	lista_login = wpisz_login(i)

powiodlo_sie = False
dane_do_zalogowania = ["login", "haslo"]

for haslo in lista_wszystkich_hasel:
	for login in lista_wszystkich_login:

		print("wpisywanie login: " + str(login))
		print("wpisywanie hasla: " + str(haslo))

		warrtosc_zwracana = wpisz_przez_pyautogui(haslo, login) #zmienić na dwa argumenty i je generować tak samo jak haslo

		if(type(wartosc_zwracana) == type(["login", "haslo"])):
			powiodlo_sie = True
			dane_do_zalogowania[0] = wartosc_zwracana[0]
			dane_do_zalogowania[1] = wartosc_zwracana[1]
			break

if(powiodlo_sie == True):
	print("operacja do logowania powiodla sie DANE: " + str(dane_do_zalogowania))
	
print("koniec")
input()