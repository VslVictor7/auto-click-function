import pyautogui
import time

# Intervalo em segundos
intervalo = 3.8

try:
    while True:
        pyautogui.click(button='left')
        print("Clique realizado.")
        time.sleep(intervalo)
except KeyboardInterrupt:
    print("Execução interrompida pelo usuário.")
