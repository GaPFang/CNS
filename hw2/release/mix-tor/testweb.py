import socket
import sys

def socket_main():
    HOST = 'localhost'  # localhost
    PORT = 12345        # Example port number
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
    while True:
        data = input("Enter message: ")
        if not data:
            break
        print(f'from server: {data}', flush=True)

if __name__ == "__main__":
    socket_main()