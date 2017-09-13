from interface import Simulateur; # Interface (Simulateur)
from ledtest import ledTest;      # Tests sur les LEDs
import serial;                    # pySerial
import time;

debug = False;   # Activer / Désactiver le mode débug (ledTest)

# arduino = serial.Serial('COM3');
# led = ledTest(debug, "sandbox");

debug = False;   # Activer / Désactiver le mode débug (Interface)
timeout = 4000;  # Actualisation de la tension actuelle

def loopVolt():
    root = volt.getRoot();
    root.after(timeout, loopVolt);

    if (debug == True): print(volt.getVolt());

volt = Simulateur(debug);
loopVolt();
