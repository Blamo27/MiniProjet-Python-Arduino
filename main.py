# Interface (Simulateur)
from interfaces.simulateur import Simulateur;

from ledtest import ledTest;  # Tests sur les LEDs
import serial;                # pySerial

debug = True;    # Activer / Désactiver le mode débug (ledTest)

# arduino = serial.Serial('COM3');
# led = ledTest(arduino, debug, "sandbox");

debug = True;    # Activer / Désactiver le mode débug (Interface)
timeout = 4000;  # Actualisation de la tension actuelle

def loopVolt():
    root = volt.getRoot();
    root.after(timeout, loopVolt);

    if (debug == True): print(volt.getVolt(), "V");

volt = Simulateur(debug);
loopVolt();
