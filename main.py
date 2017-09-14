# Interface (Simulateur)
from interfaces.simulateur import Simulateur;

from ledtest import ledTest;   # Tests sur les LEDs
import serial;                 # pySerial

from alert.main import Alert; # include alert Class

alertMsgs = {
    'low': "Batterie faible",
    'very_low': "Plus de batterie",
    'no_battery': "Plus de signal"
};

mode  = "sandbox"; # mode simulation (sandbox) ou arduino
debug = True;      # Activer / Désactiver le mode débug (ledTest)

# arduino = serial.Serial('COM3');
# led = ledTest(arduino, debug, mode);

debug = True;    # Activer / Désactiver le mode débug (Interface)
timeout = 5000;  # Actualisation de la tension actuelle

alert = Alert(); # instance de Alert


class Main(object):
    def __init__(self, i, debug = False):
        self.i = i;
        self.debug = debug;
    
    def volt(self):
        root = volt.getRoot();
        root.after(timeout, self.volt);

        if (self.i == 30): self.i = 0; 
        if (self.debug == True): print("i:", self.i);

        v = volt.getVolt();
        v = float(v);
        if (debug == True): print(v, "V");

        # Conditions si batterie inférieur à 2V
        message = None;
        if (v < 2.0 and v > 1.0):
            message = alertMsgs['low'];
            self.i += 1;
        elif (v <= 1.0 and v >= 0.5):
            message = alertMsgs['very_low'];
            self.i += 1;
        elif (v < 0.5):
            message = alertMsgs['no_battery'];
            self.i += 1;

        if (message != None and self.i == 1):
            alert.sendMail(message);
            alert.popUp(message);

# instance de Simulateur
volt = Simulateur(debug);
loop = Main(0);
loop.volt();

""" CLIGNOTEMENT DES LEDS """
