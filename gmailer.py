import smtplib
fromaddr = 'me@gmail.com'
toaddrs = 'niceperson@gmail.com'
msg = 'Womens hockey at 7pm...bring a stick.'
#gmail user name and password
username = 'whologsin'
password = 'sekret'
# send an email
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

