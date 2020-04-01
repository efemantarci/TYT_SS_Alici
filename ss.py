import pyautogui
import os
import keyboard
# başlangıç
if not os.path.isdir("Türkçe"):
    os.mkdir("Türkçe")
if not os.path.isdir("Sosyal"):
    os.mkdir("Sosyal")
if not os.path.isdir("Matematik"):
    os.mkdir("Matematik")
if not os.path.isdir("Fen"):
    os.mkdir("Fen")
soru = 1
def ss_al():
    global soru
    ss = pyautogui.screenshot()
    if soru <= 40:
        ss.save("Türkçe/soru{a}.png".format(a = soru))
    elif soru <= 60:
        ss.save("Sosyal/soru{a}.png".format(a = soru))
    elif soru <= 100:
        ss.save("Matematik/soru{a}.png".format(a = soru))
    elif soru <= 120:
        ss.save("Fen/soru{a}.png".format(a = soru))
    else:
        ss.save("soru{a}.png".format(a = soru))
    soru += 1 
def soru_degis():
    global soru
    soru = int(input("Hangi Sorudasın : "))
keyboard.add_hotkey('a', ss_al)
keyboard.add_hotkey('shift+b', soru_degis)
keyboard.wait('esc')
