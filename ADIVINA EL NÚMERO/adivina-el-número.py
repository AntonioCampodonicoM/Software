import sys
import random
import msvcrt
import time
from pwn import *
from colorama import Fore, Style

def ingresar():
    global cuenta
    x=None;t=0; starttime1=0
    print("\n")
    print(Fore.GREEN+Style.BRIGHT+"[*] Intenta adivinar el número :"+Style.RESET_ALL)
    print("\n")
    print(Fore.BLUE+Style.BRIGHT+">>> "+Style.RESET_ALL,end='')
    starttime = time.time()
    
    while time.time() - starttime< 30 and starttime1 - starttime+ cuenta< 30:
        starttime1= time.time()
        if msvcrt.kbhit():
            x=int(input())
            print("\n")
            t=time.time() - starttime
            break
    if x:
        return x, t
    else:
        return x, starttime1 - starttime
def funcionA():
    try:
        global cuenta
        print("\n")
        print(Fore.GREEN+Style.BRIGHT+"  ░█████╗░██████╗░██╗██╗░░░██╗██╗███╗░░██╗░█████╗░ ███████╗██╗░░░░░"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"  ██╔══██╗██╔══██╗██║██║░░░██║██║████╗░██║██╔══██╗ ██╔════╝██║░░░░░"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"  ███████║██║░░██║██║╚██╗░██╔╝██║██╔██╗██║███████║ █████╗░░██║░░░░░"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"  ██╔══██║██║░░██║██║░╚████╔╝░██║██║╚████║██╔══██║ ██╔══╝░░██║░░░░░"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"  ██║░░██║██████╔╝██║░░╚██╔╝░░██║██║░╚███║██║░░██║ ███████╗███████╗"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"  ╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝ ╚══════╝╚══════╝"+Style.RESET_ALL)
        print("\n")
        print(Fore.GREEN+Style.BRIGHT+"  ███╗░░██╗██╗░░░██╗███╗░░░███╗███████╗██████╗░░█████╗░"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"  ████╗░██║██║░░░██║████╗░████║██╔════╝██╔══██╗██╔══██╗"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"  ██╔██╗██║██║░░░██║██╔████╔██║█████╗░░██████╔╝██║░░██║"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"  ██║╚████║██║░░░██║██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░██║"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"  ██║░╚███║╚██████╔╝██║░╚═╝░██║███████╗██║░░██║╚█████╔╝"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"  ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░"+Style.RESET_ALL)
        print("\n")
        print(Fore.GREEN+Style.BRIGHT+"            HECHO POR ANTONIO CAMPODÓNICO"+Style.RESET_ALL)
        print("\n")
        
        print(Fore.RED+Style.BRIGHT+"[!] Elije el limite superior :"+Style.RESET_ALL)
        print("\n")
        limite=int(input(Fore.BLUE+Style.BRIGHT+">>> "+Style.RESET_ALL))
        
        numero_aleatorio=random.randint(1,limite)
        print("\n")
        print(Fore.RED+Style.BRIGHT+"[!] Tienes 30 segundos para adivinar!!!!!"+Style.RESET_ALL)
        
        a=-1
        while(a!=numero_aleatorio):
            a, aux= ingresar()
            cuenta=cuenta+aux
            if(a==None):
                print(Fore.GREEN+Style.BRIGHT+"[!] Perdiste , se acabo tu tiempo.")
                print("\n")
                print(Fore.GREEN+Style.BRIGHT+"[*] El número era "+Style.RESET_ALL,numero_aleatorio)
                sys.exit()
            if(cuenta>=30):
                print(Fore.GREEN+Style.BRIGHT+"[!] Perdiste , se acabo tu tiempo."+Style.RESET_ALL)
                print("\n")
                print(Fore.GREEN+Style.BRIGHT+"[*] El número era "+Style.RESET_ALL,numero_aleatorio)
                sys.exit()
            if(a==numero_aleatorio):
                print(Fore.GREEN+Style.BRIGHT+"[*] Felicitaciones!!!!!, has adivinado el número!!!!!!"+Style.RESET_ALL)
                print("\n")
                print(Fore.GREEN+Style.BRIGHT+"[*] El número era "+Style.RESET_ALL,numero_aleatorio)
                sys.exit()
            elif(a<numero_aleatorio):
                print(Fore.RED+Style.BRIGHT+">>> El número es mayor"+Style.RESET_ALL)
            elif(a>numero_aleatorio):
                print(Fore.RED+Style.BRIGHT+">>> El número es menor"+Style.RESET_ALL)

    except KeyboardInterrupt:
        print("\n")
        sys.exit()
cuenta=0
funcionA()