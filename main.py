# Interface (Simulateur)
from interfaces.simulateur import Simulateur;

from alert.led import led;    # Tests sur les LEDs
import serial;                # pySerial
import time;                  # Time

from alert.main import Alert; # include alert Class

alertMsgs = {
    'low': "Batterie faible",
    'very_low': "Batterie très faible",
    'no_battery': "Plus de signal"
};

mode  = "sandbox"; # mode simulation (sandbox) ou arduino
debug = True;      # Activer / Désactiver le mode débug (ledTest)

arduino = serial.Serial('COM3');
# led = ledTest(arduino, debug, mode);

debug = True;           # Activer / Désactiver le mode débug (Interface)
timeout = 5000;         # Actualisation de la tension actuelle

alert = Alert(arduino); # instance de Alert

class Main(object):
    def __init__(self, debug = False):
        self.debug = debug;
        self.obj = {
            'low': 0,
            'very_low': 0,
            'no_battery': 0
        };
    
    def volt(self):
        root = volt.getRoot();
        root.after(timeout, self.volt);

        # -0.1 toutes les 5 secondes
        v = volt.getVolt();
        v = float(v);
        
        if (v > 0 and v > 0.2): volt.decrease(0.1); 
        if (self.debug == True): print(v, "V");

        if (v > 2.0):
            self.obj['low']        = 0;
            self.obj['very_low']   = 0;
            self.obj['no_battery'] = 0;

        # Conditions si batterie inférieur à 2V
        if (v < 2.0 and v > 1.0):
            self.alert('low');
        elif (v <= 1.0 and v >= 0.5):
            self.alert('very_low');
        elif (v < 0.5):
            self.alert('no_battery');

    def alert(self, status):
        if (self.obj[status] == 0):
            self.obj[status] = 1;
            self.led(status);
            alert.sendMail(alertMsgs[status].encode('UTF-8'));
            alert.popUp(alertMsgs[status]);

    def led(self, status):
        Max = 0;
        i = 0;
        if (status == 'low'):        Max = 2;
        if (status == 'very_low'):   Max = 5;
        if (status == 'no_battery'): Max = 10;
        while (i < Max):
            i += 1;
            alert.led();
        

# instance de Simulateur
volt = Simulateur(debug);
loop = Main();
loop.volt();
