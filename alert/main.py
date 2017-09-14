from alert.mail import Mail;
from alert.popup import PopUp;
from alert.led import led;

class Alert(object):

    def __init__(self, arduino, debug = False):
        self.debug = debug;
        
        self.mail = Mail();
        self.mail.connect(); # Connexion au serveur SMTP
        
        self.popup = PopUp();

        self.LED = led(arduino);
        self.ledStatus = 0;

    def sendMail(self, message):
        self.mail.send(message);

    def popUp(self, message):
        self.popup.alert(message);

    def led(self):
        if (self.ledStatus == 0):
            self.LED.On();
            self.ledStatus = 1;
        if (self.ledStatus == 1):
            self.LED.Off();
            self.ledStatus = 0;
            
