'''Nedovršeni projekt koji je trebao na temelju Imena i Prezimena osobe pronaći njihov broj s www.imenik.hr
U teoriji postojalo bi puno imena i prezimena koja su trebala biti spremljena u .xcel tablicu'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class App(Frame):
    def __init__(self):
        self.options = Options()
        self.postavke()     
        self.lokacijaTablice = ' '
        self.win = Tk()
        self.glavno()
        return
    
    def postavke(self):
        '''postavke chroma tokom pretraživanja'''
        self.options.add_argument("--headless")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})


    def novo (self):
        '''Stvara novi prozor'''
        self.win.destroy ()
        self.win = Tk ()
        self.win.title ('RADNI NASLOV')
        super().__init__ (self.win)
        self.grid()
        return
    
    def glavno(self):
        '''Glavni izbornik'''
        self.novo()
        self.grid(padx = 150, pady=20)
        self.odabir = Button (self, text = "Odaberite Excel tablicu", command = self.nadiTablicu)
        self.odabir.grid (row = 1, column = 2)

        self.ImeLabel = Label (self, text = self.lokacijaTablice)
        self.ImeLabel.grid (row = 2, column = 2)

        self.odabir = Button (self, text = "Provjeri Brojeve", command = self.provjeriTablicu)
        self.odabir.grid (row = 3, column = 2)

        self.win.mainloop()
        return

    def nadiTablicu(self):
        '''Pronalazi adresu dokumenta'''
        root = Tk()
        root.withdraw()
        self.lokacijaTablice = filedialog.askopenfilename()
        self.glavno()
        return

    def ucitavanje(self, imePrezime):
        '''Screen učitavanja'''
        self.novo()
        self.grid(padx = 150, pady=20)

        string = "pregledavanje brojeva za: " + imePrezime
        self.ImeLabel = Label (self, text = string)
        self.ImeLabel.grid (row = 2, column = 2)
        return

    def uLink(imePrezime):
        '''Funkcija prima ime i prezime i/ili adresu i vraća link za tu osobu na adresi imenik.hr'''
        link = "https://www.imenik.hr/imenik/trazi/1/" + imePrezime + ".html"
        return link

    def traziPodatke(self, link, imePrezimeAdresa):
        '''Trazi sve brojeve upisane pod prvu osobu na linku. 
        Vraća u obliku liste čiji je prvi element adresa, 
        a ostali elementi su pronađeni brojevi'''
        lista = list()

        driver = webdriver.Chrome(options= self.options)
        driver.get("link")

        driver.find_element(By.LINK_TEXT, imePrezimeAdresa).click()

        stranica = BeautifulSoup(driver.page_source, "html.parser")

        adresa = stranica.find("div", class_="adresa_detalj")
        lista.append(adresa)

        stranica = stranica.find_all("strong")

        for i in range(1, len(stranica) - 1):
            lista.append(stranica[i].text)

        return lista

    def provjeriTablicu(self):
        if ".xcel" not in self.lokacijaTablice:
            messagebox.showwarning(title="Greška", message="Niste odabrali .xcel datoteku")
            return
        else:
            for imePrezime in svaImena:
                self.ucitavanje()
                return

app = App()