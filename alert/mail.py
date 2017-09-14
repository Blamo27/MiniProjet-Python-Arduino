import smtplib;

class Mail(object):

    def __init__(self, debug = False):
        self.debug = debug;
        if (debug == True): print('mail class init');

    def connect(self):
        self.mail = smtplib.SMTP('smtp.gmail.com',587);
        self.mail.ehlo();
        self.mail.starttls();

        self.mail.login('field.watcher.p10@gmail.com','motdepasse123');

    def send(self, content):
        self.connect(); # Connexion au serveur SMTP avant envoi
        
        self.mail.sendmail('field.watcher.p10@gmail.com', 'lepreux95520@gmail.com',content); 
        if (self.debug): print("Envoyé !");
