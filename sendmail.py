import smtplib;

class Mail:

    def __init__(self):
        self.mail = smtplib.SMTP('smtp.gmail.com',587);
        self.mail.ehlo();
        self.mail.starttls();

    def send(self):
        mail.login('lepreux95520@gmail.com','motdepasse123');
        mail.sendmail('lepreux95520@gmail.com', 'lepreux95520@gmail.com', content); 
        mail.close();
        print("Sent");

# test
mail = Mail();
mail.send('Il y\'a un problème avec la barrière');
