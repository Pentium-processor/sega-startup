from colorama import Fore,Back
import time 
from playsound import playsound
import sys
import os
import random
font_colors=[Fore.BLUE,Fore.LIGHTCYAN_EX,Fore.CYAN,Fore.LIGHTRED_EX]
sega_logo=f'''
          
                                                                                                                                       ███████╗███████╗ ██████╗  █████╗ 
                                                                                                                                       ██╔════╝██╔════╝██╔════╝ ██╔══██╗
                                                                                                                                       ███████╗█████╗  ██║  ███╗███████║
                                                                                                                                       ╚════██║██╔══╝  ██║   ██║██╔══██║
                                                                                                                                       ███████║███████╗╚██████╔╝██║  ██║
                                                                                                                                       ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ 
'''
print(Back.WHITE)
os.system("cls")
for n in sega_logo:
    sys.stdout.flush()
    time.sleep(0.01)
    sys.stdout.write(Fore.BLUE+n)
else:
    time.sleep(0.1)
    playsound("sega.mp3")
    print(Back.RESET,Fore.RESET)
    os.system("cls")