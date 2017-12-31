import smtplib

content = 'Example email stuff here'

mail = smtplib.SMTP('smtp.gmail.com', port=587)

mail.ehlo()

mail.starttls()

# mail.login('email', 'password')
mail.login('shyam.padia930@gmail.com', 'xxx')

# mail.sendmail('fromemail', 'receiver', content)
mail.sendmail('padia.shyam@awesome.com', 'shyam.padia@gmail.com', content)


mail.close()

