from selenium import webdriver 

# options = webdriver.EdgeOptions()
# options.use_chromium = True
objektStronyEdge = webdriver.Edge("https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python") #wpisać randomową stronę internetową
print("w tym momencie strona powinna być uruchomiona w edge")
input("naciśnij klawisz enter aby zakończyć program")