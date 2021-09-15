from selenium import webdriver 

# options = webdriver.EdgeOptions()
# options.use_chromium = True
objektStronyChrome = webdriver.Chrome(r"C:\Users\kacpe\Documents\Programowanie\projekty_programowanie\hakowanie_internetu\chromedriver_win32\chromedriver.exe") 
objektStronyChrome.get(r"https://chromedriver.chromium.org/getting-started")
print("w tym momencie strona powinna być uruchomiona w edge")
input("naciśnij klawisz enter aby zakończyć program")