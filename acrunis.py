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
    sys.stdout.write(font_colors[0]+n)
else:
    time.sleep(1)
    while len(font_colors)>1:
        random_color=random.choice(font_colors[1:])
        os.system("cls")
        print(random_color+sega_logo)
        time.sleep(1)
        if random_color in font_colors:
            font_colors.remove(random_color)
        else:
            pass
    playsound("sega.mp3")
    print(Back.RESET,Fore.RESET)
    os.system("cls")
