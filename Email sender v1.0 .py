from email.message import EmailMessage
import ssl
import smtplib
n = 0


mail_sender = 'ts.sandboxz4@gmail.com'
mail_pass = 'ozavpigxvksevkbc'
#ozavpigxvksevkbc

mail_rec = input('Receiver email')
body = input("Body of text?")
n = input('How many times would you like to send this email?')
subject = str(n)


for i in range (0, int(n)):
    subject = str(n)#
    em = EmailMessage()
    em['From'] = mail_sender
    em['To'] = mail_rec
    em['Subject'] = str(subject)
    em.set_content(body)

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(mail_sender, mail_pass)
        smtp.sendmail(mail_sender, mail_rec, em.as_string())
    
    n = int(n) + 1#
    print(i)
    
