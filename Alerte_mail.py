import smtplib;

class envoimail:

    def __init__(self):
    
        content = ("Il y'a un problème avec la barrière !");

        mail = smtplib.SMTP('smtp.gmail.com',587);

        mail.ehlo();

        mail.starttls();

        mail.login('lepreux95520@gmail.com','motdepasse123');

        mail.sendmail('lepreux95520@gmail.com','lepreux95520@gmail.com',content) ;

        mail.close();

        print("Sent");
