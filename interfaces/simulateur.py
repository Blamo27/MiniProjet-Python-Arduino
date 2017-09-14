from tkinter import *

volt = 0;

class Simulateur(object):

    def __init__(self, debug = False):

        self.debug = debug;
        
        self.root = Tk();
        self.root.title("Régulateur de Tension");

        # Attribution par défaut
        self.Valeur = StringVar();
        self.Valeur.set(5.0);

        # Création d'un widget Scale
        echelle = Scale(self.root,from_=0,to=5,resolution=0.1,orient=HORIZONTAL,\
        length=500,width=20,label="Tension",tickinterval=0.5,variable=self.Valeur,command=1)
        echelle.pack(padx=1,pady=1);

        # Création d'un widget Button (bouton +) 
        Button(self.root,text="+",command=self.add).pack(padx=1,pady=1);
        # Création d'un widget Button (bouton -)
        Button(self.root,text="-",command=self.rem).pack(padx=1,pady=1);
        
    def add(self):
        self.Valeur.set(str(float(self.Valeur.get())+0.1));
        if (self.debug == True): print("Changement à", self.Valeur.get(), "V");

    def rem(self):
        self.Valeur.set(str(float(self.Valeur.get())-0.1));
        if (self.debug == True): print("Changement à", self.Valeur.get(), "V");

    def decrease(self, i):
        self.Valeur.set(str(float(self.Valeur.get())-i));
        if (self.debug == True): print("Déchargement de", i,"V");

    def getVolt(self):
        return self.Valeur.get();

    def getRoot(self):
        return self.root;






