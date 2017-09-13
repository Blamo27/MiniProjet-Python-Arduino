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


""" CONDITION INFERIEUR A 1V """

""" POPUP POUR ALERTE
from interfaces.popup import PopUp;  # popup
popup = PopUp();
popup.alert('Alerte : La tension deviens trop faible !');
"""

""" SEND MAIL """

""" CLIGNOTEMENT DES LEDS """
