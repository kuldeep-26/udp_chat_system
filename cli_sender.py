# Sender end for UDP communication.......

import socket
import datetime

sender = 'user1'
receiver = 'user2'
receiver_ip = "192.168.147.153"
port_no = 2525  # range 0-65353

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")
time = now.strftime("%I:%M %p")
with open(sender + '.txt', 'a+' ) as file :
        file.write('\n' + date + '\n')

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
receiver_address = (receiver_ip, port_no)

print("Ready to send message:")
while True :
    message = input(f"{sender} write your message: ")
    encrypt_message = message.encode()
    s.sendto(encrypt_message, receiver_address)

    with open(sender + '.txt', 'a+' ) as file :
        file.write(f"{sender} ({time}): " + message + '\n')

    message = s.recvfrom(100)             # (b'kuldeep', ('127.0.0.1', 56706))
    received_meassage, receiver_address = message
    decrypted_message = received_meassage.decode()
    print(f"message from {receiver} :", decrypted_message)

    with open(sender + '.txt', 'a+' ) as file :
        file.write(f"{receiver} ({time}): " + decrypted_message + '\n')