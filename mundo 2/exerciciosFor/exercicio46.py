import os
import time

print("CONTAGEM REGRESSIVA PARA OS FOGOS")
clear_cmd = "clear"
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
    os.system(clear_cmd)

print("=-=-=-=-=BOOOOOOOOMM!=-=-=-=-=-=")
