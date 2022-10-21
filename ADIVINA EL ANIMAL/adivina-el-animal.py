import random
import string
import sys
from pwn import *
from colorama import Fore, Style

lista_palabras = ["perro","gato","zorro","gorila","jirafa","venado","manati","delfin","tiburon","mono","chimpance","oruga","halcon","cienpies","cocodrilo","tigre","panda","bisonte","avestruz","ballena","bufalo","caballo","camaleon","camello","castor","cebra","cerdo","colibri","gallina","comadreja","hiena","hipopotamo","jaguar","jabali","mapache","nutria","murcielago","pato","pavo","pinguino","reno","rinoceronte","serpiente","tejon","salamandra","vaca","ornitorrinco","topo","elefante","jaguar","mariposa","cangrejo","escorpion","calamar","langosta","pulpo","libelula"]
def escoger_palabra():
    palabra_random=random.choice(lista_palabras)
    return palabra_random.upper()

def dashboard():
    try:
        print("\n")
        print(Fore.GREEN+Style.BRIGHT+"     ░█████╗░██████╗░██╗██╗░░░██╗██╗███╗░░██╗░█████╗░ ███████╗██╗░░░░░"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"     ██╔══██╗██╔══██╗██║██║░░░██║██║████╗░██║██╔══██╗ ██╔════╝██║░░░░░"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"     ███████║██║░░██║██║╚██╗░██╔╝██║██╔██╗██║███████║ █████╗░░██║░░░░░"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"     ██╔══██║██║░░██║██║░╚████╔╝░██║██║╚████║██╔══██║ ██╔══╝░░██║░░░░░"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"     ██║░░██║██████╔╝██║░░╚██╔╝░░██║██║░╚███║██║░░██║ ███████╗███████╗"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"     ╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝ ╚══════╝╚══════╝"+Style.RESET_ALL)
        print("\n")
        print(Fore.GREEN+Style.BRIGHT+"               ░█████╗░███╗░░██╗██╗███╗░░░███╗░█████╗░██╗░░░░░"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"               ██╔══██╗████╗░██║██║████╗░████║██╔══██╗██║░░░░░"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"               ███████║██╔██╗██║██║██╔████╔██║███████║██║░░░░░"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"               ██╔══██║██║╚████║██║██║╚██╔╝██║██╔══██║██║░░░░░"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"               ██║░░██║██║░╚███║██║██║░╚═╝░██║██║░░██║███████╗"+Style.RESET_ALL)
        print(Fore.GREEN+Style.BRIGHT+"               ╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝"+Style.RESET_ALL)
        print("\n")
        print(Fore.GREEN+Style.BRIGHT+"                       HECHO POR ANTONIO CAMPODÓNICO"+Style.RESET_ALL)
        print("\n")
        palabra_escogida=escoger_palabra()
        caracteres_palabra=set(palabra_escogida)
        caracteres_adivinados=set()
        abecedario=set(string.ascii_uppercase)
        vidas=5
        while len(caracteres_palabra)>0 and vidas>0:
            print(Fore.RED+Style.BRIGHT+f" Letras usadas : {' '.join(caracteres_adivinados)} ---> Tienes {vidas} vidas."+Style.RESET_ALL)
            print("\n")
            palabra_lista=[letra if letra in caracteres_adivinados else '-' for letra in palabra_escogida]
            print(Fore.GREEN+Style.BRIGHT+f" ¿Qué animal es? : {' '.join(palabra_lista)}"+Style.RESET_ALL)
            print("\n")
            letra_faltante=input(Fore.RED+Style.BRIGHT+" Adivina una letra >>> "+Style.RESET_ALL).upper()
            print("\n",end="")
            if letra_faltante in abecedario-caracteres_adivinados:
                caracteres_adivinados.add(letra_faltante)
                if letra_faltante in caracteres_palabra:
                    caracteres_palabra.remove(letra_faltante)
                    print("")
                else:
                    vidas-=1
                    print(Fore.GREEN+Style.BRIGHT+f"\n La letra {letra_faltante} no esta en el nombre del animal."+Style.RESET_ALL)
                    print("\n")
            
            elif letra_faltante in caracteres_adivinados:
                print(Fore.YELLOW+Style.BRIGHT+"\n Ya escogiste esta letra , intenta con otra."+Style.RESET_ALL)
            else:
                print(Fore.YELLOW+Style.BRIGHT+"\n Caracter invalido."+Style.RESET_ALL)
                print("\n")
        
        if vidas==0:
            print(Fore.BLUE+Style.BRIGHT+f" Perdiste!!!!!! , el animal era: {palabra_escogida}"+Style.RESET_ALL)
        else:
            print(Fore.BLUE+Style.BRIGHT+f" Muy bien!!! , adivinaste el animal >>> {palabra_escogida}"+Style.RESET_ALL)

    except KeyboardInterrupt:
        print("\n")
        sys.exit()

dashboard()