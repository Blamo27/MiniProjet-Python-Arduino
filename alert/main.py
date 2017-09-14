from alert.mail import Mail;
from alert.popup import PopUp;

class Alert(object):

    def __init__(self, debug = False):
        self.debug = debug;
        
        self.mail = Mail();
        self.mail.connect(); # Connexion au serveur SMTP
        
        self.popup = PopUp();

    def sendMail(self, message):
        self.mail.send(message);

    def popUp(self, message):
        self.popup.alert(message);
