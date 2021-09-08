import pyautogui
from selenium import webdriver
import time

listaznakow = "abcdefghijklmnoprstuwz1234567890"

def sprawdzanie_czy_przeszlo():
	pass

def wpisz_przez_pyautogui(napisLogin, napisHaslo):
	objektStrony = webdriver.Edge("10.1.1.1")
	time.sleep(5)
	pyautogui.moveTo( ... ) # koordynaty login
	pyautogui.click()
	pyautogui.typewrite(napis)
	pyautogui.moveTo( ... ) #koordynaty hasła
	pyautogui.click()
	pyautogui.typewrite(napisHaslo)
	time.sleep(5)
	if(sprawdzanie_czy_przeszlo() == True):
		return [napisLogin, napisHaslo]
	else:
		return False
def wpisz_haslo(length, lista = [], danyNapis = "", dlugosc = 0):
	dlugosc += 1

	if(dlugosc > length):
		lista.append(danyNapis)

		return lista

	for znak in listaznakow:
		nastepnyNapis = danyNapis[:]
		nastepnyNapis += znak 
		wpisz_haslo(length, lista, nastepnyNapis, dlugosc)

	return lista

	
lista_wszystkich_hasel = []
for i in range(1, 10):
	lista_hasel = wpisz_haslo(i)	
	lista_wszystkich_hasel.append(lista_hasel)
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