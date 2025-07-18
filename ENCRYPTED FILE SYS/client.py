from cryptography.fernet import Fernet
import socket
import os
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="file_path", help="File to encrypt")
    (options, arguments) = parser.parse_args()
    
    if not options.file_path:
        parser.error("[-] Please specify a file to encrypt. Use --help for more info.")
    
    return options.file_path

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path, fernet):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        print(f"Read {len(file_data)} bytes from {file_path}")
        encrypted = fernet.encrypt(file_data)
        print(f"Encrypted data size: {len(encrypted)} bytes")
        return encrypted

def start_encryption(filepath):
    key = load_key()
    fernet = Fernet(key)

    data = encrypt_file(filepath, fernet)

    with open(filepath, 'wb') as file:
        file.write(data)
        print(f"Encrypted data written to {filepath}")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 4444))
    print("Connected to server. Sending data...")
    s.sendall(data)
    s.shutdown(socket.SHUT_WR) 
    print("Data sent. Waiting for server response...")
    response = s.recv(1024)
    print("Server says:", response.decode())
    s.close()
    print("Connection closed.")

option = get_arguments()
start_encryption(option)
