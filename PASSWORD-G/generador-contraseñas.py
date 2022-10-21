import random
import sys
from pwn import *
from colorama import Fore,Back,Style
import pyperclip

def generador(x):
    caracteres="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    numeros="1234567890"
    caracteres_especiales="|!$%&/()=?¡+}{-[]@^#¿*"
    total=f'{caracteres}{numeros}{caracteres_especiales}'
    password=random.sample(total,x)
    final_password="".join(password)
    print(Fore.GREEN+Style.BRIGHT+" La contraseña generada fue : "+Style.RESET_ALL)
    print("\n")
    print(Fore.BLUE+Style.BRIGHT+" >>>"+Style.RESET_ALL,Fore.GREEN+Style.BRIGHT+final_password+Style.RESET_ALL)
    print("\n")
    print(Fore.GREEN+Style.BRIGHT+" [!] Contraseña copiada en la clipboard"+Style.RESET_ALL)
    print("\n")
    pyperclip.copy(final_password)
    pyperclip.paste()
    print(Fore.GREEN+Style.BRIGHT+" RECUERDE NO COMPARTIR SU CONTRASEÑA."+Style.RESET_ALL)

try:
    print("\n")    
    print(Fore.GREEN+Style.BRIGHT+"     ██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░░░░░░░██████╗░"+Style.RESET_ALL)
    print(Fore.GREEN+Style.BRIGHT+"     ██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗░░░░░░██╔════╝░"+Style.RESET_ALL)
    print(Fore.GREEN+Style.BRIGHT+"     ██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║█████╗██║░░██╗░"+Style.RESET_ALL)
    print(Fore.GREEN+Style.BRIGHT+"     ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║╚════╝██║░░╚██╗"+Style.RESET_ALL)
    print(Fore.GREEN+Style.BRIGHT+"     ██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝░░░░░░╚██████╔╝"+Style.RESET_ALL)
    print(Fore.GREEN+Style.BRIGHT+"     ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░░░░░╚═════╝░"+Style.RESET_ALL)
    print("\n")
    print(Fore.GREEN+Style.BRIGHT+"                             HECHO POR ANTONIO CAMPODÓNICO"+Style.RESET_ALL)
    print("\n")
    print(Fore.RED+Style.BRIGHT+" Digite el nivel de seguridad de su contraseña:"+Style.RESET_ALL)
    print("\n")
    print(Fore.GREEN+Style.BRIGHT+" [1] Debil"," [2] Normal"," [3] Segura"," [4] Bastante segura"," [5] Salir"+Style.RESET_ALL,sep="\n")
    print("\n")
    nivel_de_seguridad=int(input(Fore.RED+Style.BRIGHT+" >>> "+Style.RESET_ALL))
    print("\n")

    if nivel_de_seguridad==1:
        generador(6)
        sys.exit()

    elif nivel_de_seguridad==2:
        generador(8)
        sys.exit()

    elif nivel_de_seguridad==3:
        generador(10)
        sys.exit()

    elif nivel_de_seguridad==4:
        generador(15)
        sys.exit()

    elif nivel_de_seguridad==5:
        print("Adios!!!")
        sys.exit()

except KeyboardInterrupt:
    print("\n")
    sys.exit()