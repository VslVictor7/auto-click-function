import pyautogui
import time

intervalo = 4

try:
    while True:
        pyautogui.click(button='left')
        print("Clique realizado.")
        time.sleep(intervalo)
except KeyboardInterrupt:
    print("Execução interrompida pelo usuário.")
