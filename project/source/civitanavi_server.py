import time
import socket
import json
import random

# Funzione per inviare i dati al client
def send_data(client_socket, data):
    message = json.dumps(data).encode('utf-8')
    client_socket.send(message)

# Inizializzazione del server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8888))
server_socket.listen(1)

print("Server in ascolto...")

# Accetta la connessione
client_socket, client_address = server_socket.accept()
print("Connessione accettata da:", client_address)

try:
    pitchInizio = random.randint(-20, 20)
    rollInizio = random.randint(-20, 20)
    yawInizio = random.randint(-20, 20)
    
    while True:
        x = 1
        while x == 1:       
            pitch = random.randint(pitchInizio - 1, pitchInizio + 1) 
            roll = random.randint(rollInizio - 1, rollInizio + 1) 
            yaw = random.randint(yawInizio - 1, yawInizio + 1)
            if (pitch < 20 and pitch > -20) and (roll < 20 and roll > -20) and (yaw < 20 and yaw > -20): 
                x = 0  
            if (roll == 0):
                roll = 1
                
        pitchInizio = pitch
        rollInizio = roll
        yawInizio = yaw

        # Invia i dati al client
        data = {'pitch': pitch, 'roll': roll, 'yaw': yaw}
        send_data(client_socket, data)
        time.sleep(0.1)  # Attendi 100 millisecondi tra l'invio di ogni messaggio

except KeyboardInterrupt:
    print("Connessione interrotta.")
    client_socket.close()
    server_socket.close()
