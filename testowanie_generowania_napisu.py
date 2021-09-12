listaznakow = "abcdefghijklmnoprstuwz1234567890"

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

lista = wpisz_haslo(3)
for element in lista:
  print(element)