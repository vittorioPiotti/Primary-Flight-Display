"""
Primary Flight Display v1.0.0 (https://github.com/vittorioPiotti/Primary-Flight-Display/releases/tag/1.0.0)
Copyright 2024 Vittorio Piotti, Diego Ciucaloni, Matteo Fabbioni, Luca Niccià
Licensed under GPL-3.0 (https://github.com/vittorioPiotti/Primary-Flight-Display/blob/main/LICENSE.md)
"""

"""
TKinter 8.6
-----------
TKinter is distributed as part of the Python Standard Library.

Python Software Foundation License Version 2

For the full license text, please visit:
https://docs.python.org/3/license.html
"""


import socket
import display
import json
import tkinter as tk

# Funzione per aggiornare i dati nella schermata Tkinter
def update_data(roll,pitch):
    pitch_label.config(text=roll)
    roll_label.config(text=pitch)


# Connessione al server
ipserver = "127.0.0.1"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ipserver, 8888))


root = tk.Tk()
root.title("Dati dal server")

pitch_label = tk.Label(root, text="Pitch: ")
pitch_label.pack()

roll_label = tk.Label(root, text="Rool: ")
roll_label.pack()

display = display.Display(600,600)
try:
    while True:
        msg = client_socket.recv(1024)
        msgs = msg.strip().decode('utf-8').split('\n')
        for msg in msgs:
            try:
                data = json.loads(msg)
                print(data)
                roll = float(data['roll'])
                pitch = float(data['pitch'])

                update_data(roll,pitch)

                display.update_components(roll,pitch)
                
                root.update()
            except json.decoder.JSONDecodeError as e:
                print("Errore di decodifica JSON:", e)

except KeyboardInterrupt:
    client_socket.close()

root.mainloop()

    
    
