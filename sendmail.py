import smtplib;

class Mail(object):

    def __init__(self):
        self.mail = smtplib.SMTP('smtp.gmail.com',587);
        self.mail.ehlo();
        self.mail.starttls();

    def send(self, content):
        self.mail.login('lepreux95520@gmail.com','motdepasse123');
        self.mail.sendmail('lepreux95520@gmail.com', 'lepreux95520@gmail.com', content); 
        self.mail.close();
        print("Envoyé !");

# test
mail = Mail();
mail.send("Il y a un problème avec la barrière !".encode('UTF-8'));
