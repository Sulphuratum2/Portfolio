from sqlite3 import *
from tkinter import *
from tkinter import messagebox

class App (Frame):
    def __init__(self):
        self.win = Tk()
        self.con()
        s = "SELECT name FROM sqlite_master WHERE type='table' AND name='Maturanti'"
        self.c.execute(s)
        if (len(self.c.fetchall()) == 0):
            print ('hi')
            s = '''CREATE TABLE Maturanti (
            Matbr INTEGER PRIMARY KEY, 
            Ime TEXT, 
            Prezime TEXT,
            GodRod TEXT,
            Nazivskole TEXT)
            '''
            self.c.execute(s)
            
            s = '''CREATE TABLE Ispiti (
            Sifra TEXT PRIMARY KEY,
            Naziv TEXT,
            Bodovi INTEGER)
            '''
            self.c.execute(s)

            s = '''CREATE TABLE MaturantiIspiti (
            Matbr INTEGER REFERENCES Maturanti (Matbr),
            Sifra TEXT REFERENCES Ispiti (Sifra))
            '''
            self.c.execute(s)
        self.glavno()
        return

    def con(self):
        self.conn = connect ('MaturaBaza.db')
        self.c = self.conn.cursor()
        return
        
    def novo (self):
        self.win.destroy ()
        self.win = Tk ()
        self.win.title ('Maturanti i ispiti')
        super().__init__ (self.win)
        self.grid()
        return
        
    def glavno(self):
        self.novo()
        self.grid(padx = 150, pady=20)
        self.dod = Button (self, text = "Upišite podatke o učeniku", command = self.upis_ucenika)
        self.dod.grid (row = 1, column = 2)
        self.look = Button (self, text = "Upišite podatke o ispitu", command = self.upis_ispita)
        self.look.grid (row = 2, column = 2)
        self.poc = Button (self, text = "Prijavite učeniku ispit", command = self.prijava_ispita)
        self.poc.grid (row = 3, column = 2)
        self.poc = Button (self, text = "Odjavite učeniku ispit", command = self.odjava_ispita)
        self.poc.grid (row = 4, column = 2)
        self.poc = Button (self, text = "Pregled ispita koje je prijavio neki maturant", command = self.pregledispita)
        self.poc.grid (row = 6, column = 2)
        self.poc = Button (self, text = "Pregled maturanata koji su prijavili neki ispit", command = self.pregledmaturanata)
        self.poc.grid (row = 7, column = 2)
        self.win.mainloop()
        return
        
    def upis_ucenika(self):
        self.novo()
        self.Ime = StringVar()
        self.Prezime = StringVar()
        self.Matbr = StringVar()
        self.GodRod = StringVar()
        self.NazivSkole = StringVar()
        
        self.ImeLabel = Label (self, text = "Ime učenika")
        self.ImeLabel.grid (row = 1, column = 1, sticky = E)
        self.ImeU = Entry (self,textvariable = self.Ime)
        self.ImeU.grid (row = 1, column = 2, sticky = W)
        
        self.PrezimeLabel = Label (self, text = "Prezime učenika")
        self.PrezimeLabel.grid (row = 2, column = 1, sticky = E)
        self.PrezimeU = Entry (self,textvariable = self.Prezime)
        self.PrezimeU.grid (row = 2, column = 2, sticky = W)

        self.MatbrLabel = Label (self, text = "Matični broj učenika")
        self.MatbrLabel.grid (row = 3, column = 1, sticky = E)
        self.MatbrU = Entry (self,textvariable = self.Matbr)
        self.MatbrU.grid (row = 3, column = 2, sticky = W)
        
        self.GodRodLabel = Label (self, text = "Godina rođenja")
        self.GodRodLabel.grid (row = 4, column = 1, sticky = E)
        self.GodRodU = Entry (self,textvariable = self.GodRod)
        self.GodRodU.grid (row = 4, column = 2, sticky = W)

        self.NazivSkLabel = Label (self, text = "Naziv škole")
        self.NazivSkLabel.grid (row = 5, column = 1, sticky = E)
        self.NazivSkU = Entry (self,textvariable = self.NazivSkole)
        self.NazivSkU.grid (row = 5, column = 2, sticky = W)

        self.finishUc = Button (self, text = "Dodajte učenika",command = self.dodaj_ucenika) 
        self.finishUc.grid (row = 6, column = 2, sticky = W)
        self.back = Button (self, text = "Natrag", command = self.glavno)
        self.back.grid (row = 7, column = 3)
        return
        
    def dodaj_ucenika(self):
        s = '''INSERT INTO Maturanti (Matbr, Ime, Prezime, GodRod, Nazivskole)
            VALUES ({0}, "{1}", "{2}", {3}, "{4}")'''.format(self.Matbr.get(),self.Ime.get(),self.Prezime.get(),self.GodRod.get(),self.NazivSkole.get())
        self.c.execute(s)
        self.spremi()
        self.upis_ucenika()
        return
        
    def spremi (self): 
        self.conn.commit()
        self.conn.close()
        self.con()
        return
        
    def upis_ispita(self):
        self.novo()
        self.Naziv = StringVar()
        self.Sifra = StringVar()
        self.BrBod = StringVar()
        
        self.NazivLabel = Label (self, text = "Naziv ispita")
        self.NazivLabel.grid (row = 1, column = 1, sticky = E)
        self.NazivU = Entry (self,textvariable = self.Naziv)
        self.NazivU.grid (row = 1, column = 2, sticky = W)
        
        self.SifraLabel = Label (self, text = "Šifra ispita")
        self.SifraLabel.grid (row = 2, column = 1, sticky = E)
        self.SifraU = Entry (self,textvariable = self.Sifra)
        self.SifraU.grid (row = 2, column = 2, sticky = W)

        self.BrBLabel = Label (self, text = "Moguć broj bodova")
        self.BrBLabel.grid (row = 3, column = 1, sticky = E)
        self.BrBU = Entry (self,textvariable = self.BrBod)
        self.BrBU.grid (row = 3, column = 2, sticky = W)
        
        self.finishIc = Button (self, text = "Dodajte ispit",command = self.dodaj_ispit)
        self.finishIc.grid (row = 4, column = 2, sticky = W)
        self.back = Button (self, text = "Natrag", command = self.glavno)
        self.back.grid (row = 5, column = 3)
        return
       
    def dodaj_ispit(self):
        s = '''INSERT INTO Ispiti (Sifra, Naziv, Bodovi)
        VALUES ("{0}", "{1}", {2})'''.format(self.Sifra.get(),self.Naziv.get(),self.BrBod.get())
        self.c.execute(s)
        self.spremi()
        self.upis_ispita()
        return
        
    def prijava_ispita(self):
        self.novo()
        self.back = Button (self, text = "Natrag", command = self.glavno)
        self.back.grid (row = 1, column = 4, padx = 100)
        s = 'SELECT Ime,Prezime,MatBr FROM Maturanti'
        self.c.execute(s)
        self.svimucenici = self.c.fetchall()
        self.ucenici = list()
        for k in self.svimucenici:
            self.ucenici.append('{0} {1}'.format(k[0], k[1]))
        
        s = 'SELECT Naziv,Sifra FROM Ispiti'
        self.c.execute(s)
        self.svispiti = self.c.fetchall()
        self.ispiti = list()
        for k in self.svispiti:
            self.ispiti.append(k[0])
        
        self.koj_ucenik = StringVar()
        self.koj_ucenik.set(self.ucenici [0])
        self.koj_ispiti = StringVar()
        self.koj_ispiti.set(self.ispiti [0])
        
        self.uctitle = Label (self, text = "Izaberite učenika")
        self.uctitle.grid (row = 1, column = 1, sticky = W)
        self.opuc = OptionMenu(self, self.koj_ucenik, *self.ucenici) 
        self.opuc.grid (row = 1, column = 3, sticky = W)

        self.istitle = Label (self, text = "Izaberite ispit")
        self.istitle.grid (row = 2, column = 1, sticky = W)
        self.opis = OptionMenu(self, self.koj_ispiti, *self.ispiti) 
        self.opis.grid (row = 2, column = 3, sticky = W)

        self.prij = Button (self, text = "Prijavite ispit", command = self.prijavi) 
        self.prij.grid(row = 3, column = 2)
        return
        
    def prijavi(self):
        s = '''INSERT INTO MaturantiIspiti (MatBr,Sifra)
        VALUES ("{}","{}")'''.format(self.svimucenici [self.ucenici.index(self.koj_ucenik.get())] [2], self.svispiti [self.ispiti.index(self.koj_ispiti.get())] [1])
        self.c.execute(s) 
        self.spremi() 
        return
        
    def odjava_ispita(self):
        self.novo()
        self.back = Button (self, text = "Natrag", command = self.glavno)
        self.back.grid (row = 1, column = 4, padx = 100)
        s = 'SELECT Ime,Prezime,MatBr FROM Maturanti'
        self.c.execute(s)
        self.svimucenici = self.c.fetchall()
        self.ucenici = list()
        for k in self.svimucenici:
            self.ucenici.append('{0} {1}'.format(k[0], k[1]))
            
        s = 'SELECT Naziv,Sifra FROM Ispiti'
        self.c.execute(s)
        self.svispiti = self.c.fetchall()
        self.ispiti = list()
        for k in self.svispiti:
            self.ispiti.append(k[0])
            
        self.koj_ucenik = StringVar()
        self.koj_ucenik.set(self.ucenici [0])
        self.koj_ispiti = StringVar()
        self.koj_ispiti.set(self.ispiti [0])
            
        self.uctitle = Label (self, text = "Izaberite učenika")
        self.uctitle.grid (row = 1, column = 1, sticky = W)
        self.opuc = OptionMenu(self, self.koj_ucenik, *self.ucenici) 
        self.opuc.grid (row = 1, column = 3, sticky = W)

        self.istitle = Label (self, text = "Izaberite ispit")
        self.istitle.grid (row = 2, column = 1, sticky = W)
        self.opis = OptionMenu(self, self.koj_ispiti, *self.ispiti) 
        self.opis.grid (row = 2, column = 3, sticky = W)
        
        self.prij = Button (self, text = "Odjavite ispit", command = self.odjavi) 
        self.prij.grid(row = 3, column = 2)
        return
        
    def odjavi(self):
        s = '''DELETE FROM MaturantiIspiti WHERE Matbr = {0} AND Sifra = {1}
        '''.format(self.svimucenici [self.ucenici.index(self.koj_ucenik.get())] [2], self.svispiti [self.ispiti.index(self.koj_ispiti.get())] [1])
        self.c.execute(s) 
        self.spremi() 
        return
        
    def pregledispita(self):
        self.novo()
        self.back = Button (self, text = "Natrag", command = self.glavno)
        self.back.grid (row = 1, column = 4, padx = 100)
        s = 'SELECT Ime,Prezime,MatBr FROM Maturanti'
        self.c.execute(s)
        self.svimucenici = self.c.fetchall()
        self.ucenici = list()
        for k in self.svimucenici:
            self.ucenici.append('{0} {1}'.format(k[0], k[1]))
            
        self.koj_ucenik = StringVar()
        self.koj_ucenik.set(self.ucenici [0])
        
        self.uctitle = Label (self, text = "Izaberite učenika")
        self.uctitle.grid (row = 1, column = 1, sticky = W)
        self.opuc = OptionMenu(self, self.koj_ucenik, *self.ucenici) 
        self.opuc.grid (row = 1, column = 3, sticky = W)
        
        self.isp = Button (self, text = "Pregled ispita koje je prijavio taj maturant", command = self.ispisispita) 
        self.isp.grid(row = 2, column = 2)
        return
     
    def ispisispita(self):
        s = '''SELECT Ispiti.Naziv FROM MaturantiIspiti
        INNER JOIN Maturanti ON MaturantiIspiti.MatBr = Maturanti.MatBr
        INNER JOIN Ispiti ON MaturantiIspiti.Sifra = Ispiti.Sifra
        WHERE Maturanti.MatBr = {0}'''.format(self.svimucenici [self.ucenici.index(self.koj_ucenik.get())] [2])
        self.c.execute(s)
        rez = self.c.fetchall()
        x = ''
        for k in rez:
            x += (str(k[0]) + '\n')
        messagebox.showinfo(title='Ispiti koje je prijavio taj maturant', message=x)
        return
        
    def pregledmaturanata(self):
        self.novo()
        self.back = Button (self, text = "Natrag", command = self.glavno)
        self.back.grid (row = 1, column = 4, padx = 100)
        s = 'SELECT Naziv,Sifra FROM Ispiti'
        self.c.execute(s)
        self.svispiti = self.c.fetchall()
        self.ispiti = list()
        for k in self.svispiti:
            self.ispiti.append(k[0])
            
        self.koj_ispiti = StringVar()
        self.koj_ispiti.set(self.ispiti [0])
        
        self.istitle = Label (self, text = "Izaberite ispit")
        self.istitle.grid (row = 1, column = 1, sticky = W)
        self.opis = OptionMenu(self, self.koj_ispiti, *self.ispiti) 
        self.opis.grid (row = 1, column = 3, sticky = W)
        
        self.isp = Button (self, text = "Pregled maturanata koji su prijavili taj ispit", command = self.ispismaturanata) 
        self.isp.grid(row = 2, column = 2)
        return
    
    def ispismaturanata(self):
        s = '''SELECT Maturanti.Ime, Maturanti.Prezime FROM MaturantiIspiti
        INNER JOIN Maturanti ON MaturantiIspiti.MatBr = Maturanti.MatBr
        INNER JOIN Ispiti ON MaturantiIspiti.Sifra = Ispiti.Sifra
        WHERE Ispiti.Sifra = {0}'''.format(self.svispiti [self.ispiti.index(self.koj_ispiti.get())] [1])
        self.c.execute(s)
        rez = self.c.fetchall()
        x = ''
        for k in rez:
            x += (str(k[0]) + ' ' + str(k[1]) + '\n')
        messagebox.showinfo(title='Maturanti koji su prijavili taj ispit', message=x)
        return

app = App()
