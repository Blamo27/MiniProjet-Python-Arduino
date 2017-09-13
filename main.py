from interface import Simulateur; # Interface (Simulateur)
from ledtest import ledTest;      # Tests sur les LEDs
import serial;                    # pySerial
import time;

# arduino = serial.Serial('COM3');
# ledTest() TEST

debug = True;    # Activer / Désactive le mode débug
timeout = 4000;  # Actualisation de la tension actuelle

def loopVolt():
    root = volt.getRoot();
    root.after(timeout, loopVolt);

    if (debug == True): print(volt.getVolt());

volt = Simulateur(debug);
loopVolt();
