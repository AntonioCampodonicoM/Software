import sys
from functools import reduce
from pwn import *
import pyperclip
from colorama import Fore, Back, Style

opcion=0
caracteres = "0123456789abcdef"


banner=["███████╗███╗░░██╗░█████╗░░█████╗░██████╗░███████╗░░░░░░░░███╗░░░█████╗░",
        "██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝░░░░░░░████║░░██╔═══╝░",
        "█████╗░░██╔██╗██║██║░░╚═╝██║░░██║██║░░██║█████╗░░█████╗██╔██║░░██████╗░",
        "██╔══╝░░██║╚████║██║░░██╗██║░░██║██║░░██║██╔══╝░░╚════╝╚═╝██║░░██╔══██╗",
        "███████╗██║░╚███║╚█████╔╝╚█████╔╝██████╔╝███████╗░░░░░░███████╗╚█████╔╝",
        "╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═════╝░╚══════╝░░░░░░╚══════╝░╚════╝░",
        "\n",
        "                     HECHO POR ANTONIO CAMPODÓNICO                   "]        


print("\n")
for i in banner:
    print(Fore.GREEN+Style.BRIGHT+i.center(230," ")+Style.RESET_ALL)
print("\n")


def menu():
    print(Fore.BLUE+Style.BRIGHT+"[1] Codificar"+Style.RESET_ALL)
    print(Fore.BLUE+Style.BRIGHT+"[2] Decodificar"+Style.RESET_ALL)
    print(Fore.BLUE+Style.BRIGHT+"[3] Salir"+Style.RESET_ALL)
    print("\n")
    seleccion=int(input("---> "))
    print("\n")
    return seleccion

def conversor_palabra_a_hex(palabra):
    lista=[]
    for letra in palabra:
        temporal=hex(ord(letra)).replace('0x','')
        lista.append(temporal)
    return reduce(lambda i, j:i+j,lista)

def revisar_la_cadena(palabra, pasos):
    letra = []
    for caracter in palabra:
        letra.append(caracter)
        if len(letra) == pasos:
            yield letra
            letra = []
    if letra:
        yield letra

def decodificador(cadena_codificada):
    enumerar = {y:x for x, y in enumerate(caracteres)}
    lista_caracteres = []
    for primer_paso, segundo_paso in revisar_la_cadena(cadena_codificada, 2):
        primer_paso = enumerar[primer_paso]
        segundo_paso = enumerar[segundo_paso]
        byte = primer_paso << 4 | segundo_paso
        lista_caracteres.append(byte)
    return bytes(lista_caracteres)

try:
    while opcion!=3:
        opcion=menu()
        if opcion==1:
            palabra_sin_codificar=input(Fore.RED+Style.BRIGHT+"[*] Ingrese la cadena que quiere encriptar : "+Style.RESET_ALL)
            print("\n")
            barra=log.progress(Fore.GREEN+Style.BRIGHT+"Encriptando..."+Style.RESET_ALL)
            time.sleep(1)
            print("\n")
            proceso_final=conversor_palabra_a_hex(palabra_sin_codificar)
            print(Fore.RED+Style.BRIGHT+"[*] La codificación es :"+Style.RESET_ALL)
            print("\n")
            print(">>> ",proceso_final)
            print("\n")
            print(Fore.GREEN+Style.BRIGHT+"[!] Elemento copiado en la clipboard"+Style.RESET_ALL)
            print("\n")
            pyperclip.copy(proceso_final)
            pyperclip.paste()
            

        elif opcion==2:
            palabra_codificada=input(Fore.RED+Style.BRIGHT+"[*] Ingrese la cadena codificada : "+Style.RESET_ALL)
            print("\n")
            barra=log.progress(Fore.GREEN+Style.BRIGHT+"Desencriptando..."+Style.RESET_ALL)
            time.sleep(1)
            print("\n")
            proceso_final=decodificador(palabra_codificada).decode("ISO 8859-1")
            print(Fore.RED+Style.BRIGHT+"[*] La cadena decodifica sería :"+Style.RESET_ALL)
            print("\n")
            print(">>> ",proceso_final)
            print("\n")
            print(Fore.GREEN+Style.BRIGHT+"[!] Elemento copiado en la clipboard"+Style.RESET_ALL)
            print("\n")
            pyperclip.copy(proceso_final)
            pyperclip.paste()
            

except KeyboardInterrupt:
    print("\n")
    sys.exit()