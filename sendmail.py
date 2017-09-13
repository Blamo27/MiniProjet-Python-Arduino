import smtplib;

class envoimail:

    def __init__(self, mail):
        mail = smtplib.SMTP('smtp.gmail.com',587);
        mail.ehlo();
        mail.starttls();

    def sendmail(self):
        mail.login('lepreux95520@gmail.com','motdepasse123');
        mail.sendmail('lepreux95520@gmail.com','lepreux95520@gmail.com','Il y\'a un problème avec la barrière'); 
        mail.close();
        print("Sent");
