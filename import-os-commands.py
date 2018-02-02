# Script ifconfig
# Futura implementação de iw dev / airmon-ng /
# feito e analizado dia 01/02/2018 Matheus Silva

import os

print("desativando interface de rede eth0 ")


os.system("ifconfig")

os.system("ifconfig eth0 down")

print("eth0 desativada")
