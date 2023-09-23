import sys
import time
from colorama import Fore
#import random
#for x in range(11):
#    print("{}%".format (x))
#    sys.stdout.write("\033[F")
#    time.sleep(0.5)

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

for x in opcoes:
    print("\033[K", x.strip(), end = "\r")
    time.sleep(1.2)
    
print(Fore.RED + 'Teste')