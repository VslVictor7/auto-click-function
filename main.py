import pyautogui
import time

intervalo = 7

try:
    while True:
        pyautogui.mouseDown(button='left')
        print("Botão pressionado.")
        time.sleep(1)
        pyautogui.mouseUp(button='left')
        print("Botão solto.")
        time.sleep(intervalo)
except KeyboardInterrupt:
    print("Execução interrompida pelo usuário.")