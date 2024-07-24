# Receiver end for UDP communication.......

import socket
import datetime

sender = 'user1'            # user names can be changed accordingly
receiver = 'user2'           
sender_ip = "192.168.147.153"     
port_no = 2525              # select any port range(0-65535) expect the reserved one's

now = datetime.datetime.now()       # object creation 
date = now.strftime("%d-%m-%Y")     # date variable
time = now.strftime("%I:%M %p")     # time variable
with open(receiver + '.txt', 'a+' ) as file :       # creating a txt file to save chat for receiver end
        file.write('\n' + date + '\n')              # firstly saving current date in txt file

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # creating object for socket 
sender_address = (sender_ip, port_no)               # proper sender address as a TUPLE
s.bind(sender_address)                  # Binding address with the object

print("Ready to receive messages ...")
while True :
    message = s.recvfrom(100)                # (b'kuldeep', ('127.0.0.1', 56706))
    received_meassage, sender_address = message
    decrypted_message = received_meassage.decode()
    print(f"message from {sender} :", decrypted_message)

    with open(receiver + '.txt', 'a+' ) as file :
        file.write(f"{sender} ({time}): " + decrypted_message + '\n')

    response = input(f"{receiver} write your response: ")
    encrypt_response = response.encode()
    s.sendto(encrypt_response, sender_address)

    with open(receiver + '.txt', 'a+' ) as file :
        file.write(f"{receiver} ({time}): " + response + '\n')