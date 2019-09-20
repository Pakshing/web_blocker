import time
from datetime import datetime as dt
hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com"]

def blockWeb():
    print("It is working hours....( press Control C to exit.)")
    with open(hosts_path,'r+' ) as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect +" "+ website + "\n")

def recoverFile():
    with open(hosts_path,'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any (website in line for website in website_list):
                file.write(line)
                file.truncate()
        print("File has recovered.")

print("This is a beta version. This program only blocks facebook websites." + "\n"+"The list has: ")
for website in website_list:
    print (website +" ")

print("\n"+ "What period of time you want to block the listed websites?")
startTime = int (input( "(Military hours)From: " ) )
endTime = int ( input("(Military hours)To: ") )
recover = input("If you want to recover from the blocking, input y. Or input n for excute web blocker. ")

if recover is "n":
    while True:
        if dt( dt.now().year, dt.now().month, dt.now().day, startTime) < dt.now() < dt( dt.now().year, dt.now().month, dt.now().day,endTime) :
            blockWeb()
            time.sleep(30)
        else:
            print("The web blocker has stopped")
            recoverFile()
else:
    recoverFile()



