import smtplib
a = ['ravichandra178@gmail.com','amazonprm91@gmail.com','amazonprm92@gmail.com','amazonprm93@gmail.com']

for i in range(0,len(a)):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login('vegendlan@gmail.com','apppw')
	msg = "Hello This is smtp test mail"
	server.sendmail('vegendlan@gmail.com',a[i],msg)
	server.quit()

	print('Email Sent to {}'.format(a[i]))

