import smtplib as s

ob=s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('malikzain909192@gmail.com', 'xtgw gqtu kjev mmuq')
subject="Testing "
body="Hi, myself Zain Ali. "
message="subject:{}\n\n{}".format(subject,body)
recivers=[
            'zaini90ali1@gmail.com',
            '19011598-130@uog.edu.pk',
            'ahsanjee13574@gmail.com'
]
ob.sendmail('malikzain909192@gmail.com',
            recivers,message)
print("Mail sended")
ob.quit()