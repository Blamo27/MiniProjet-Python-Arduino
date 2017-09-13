import serial;  # pySerial
import time;

class ledTest(object):

    def __init__(self, arduino, debug = False, mode = "NaN"):
        self.arduino = arduino;
        self.debug   = debug;
        
        if (mode == "sandbox"): self.test();

    def test(self):
        action = input("Entrez \"on\", \"off\" ou \"end\" : ");

        if (action == "on"): self.On();
        elif (action == "off"): self.Off();
        elif (action == "end"): self.endArduino();
        else: print("Commande inconnue");
        
    def On(self):
        if (self.debug == True): print("LED -> Allumé");
        time.sleep(1);
        self.arduino.write('H'.encode('ascii'));

    def Off(self):
        if (self.debug == True): print("LED -> Eteinte");
        time.sleep(1);
        self.arduino.write('L'.encode('ascii'));

    def endArduino(self):
        if (self.debug == True): print("Arrêt du programme");
        self.arduino.close();
