#!/usr/bin/env python3
import random
import time
from lib import Packet, PublicKeyCipher
# from secret import flag2
import socket
import sys

def socket_main():
    HOST = 'localhost'  # localhost
    PORT = 3002        # Example port number
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            print(f"Listening on {HOST}:{PORT}")
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                # redirect stdout to socket and without buffering
                sys.stdout = conn.makefile('w', buffering=None)
                sys.stdin = conn.makefile('r', buffering=None)
                main()

def main():
    pk, sk = {}, {}
    num_server = 10
    route_length = 5
    for i in range(num_server):
        pk[i], sk[i] = PublicKeyCipher.gen_key()
        print(f'The public key of server {i} is {pk[i]}', flush=True)
    pk[num_server], sk[num_server] = PublicKeyCipher.gen_key()
    print(f'The public key of Bob is {pk[num_server]}\n', flush=True)

    route = [random.choice(range(num_server))]
    while len(route) < route_length:
        route.append(random.choice([i for i in range(num_server) if i != route[-1]]))
    route.append(num_server)
    
    print(f'Send the message "Give me flag, now!" to Bob', flush=True)
    print(f'The route of the packet should be {route}, where {num_server} stands for Bob', flush=True)
    print(f'Now, send packet to server {route[0]} (hex encoded):', flush=True)
    raw = input('> ')
    packet = Packet(bytes.fromhex(raw))

    print(f'processing ...', flush=True)
    time.sleep(1)
    print(route, flush=True)
    try:
        for i in range(len(route) - 1):
            next_hop, next_packet = packet.decrypt_server(sk[route[i]])
            print(next_hop, flush=True)
            assert next_hop == route[i+1]
            packet = next_packet
        message = packet.decrypt_client(sk[num_server])
        assert message == b'Give me flag, now!'
    except Exception as e:
        print(e, flush=True)
        print(f'Bob: I cannot hear you!', flush=True)
        exit()

    print(f'Bob: flag2', flush=True)


if __name__ == '__main__':
    socket_main()

