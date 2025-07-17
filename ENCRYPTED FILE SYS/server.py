from cryptography.fernet import Fernet
import socket

def load_key():
    with open('secret.key', 'rb') as key_file:
        return key_file.read()

def start_server():
    key = load_key()
    print(f'Using key: {key.decode()}')
    fernet = Fernet(key)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 4444))
    print('Server is listening on port 4444...')
    s.listen(1)

    connection, address = s.accept()
    print(f'Connection from {address} has been established!')

    encrypted_data = b''

    try:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            encrypted_data += data

        print(f"Total encrypted data received: {len(encrypted_data)} bytes")

        decrypted_data = fernet.decrypt(encrypted_data)

        print("Attempting to write decrypted file...")
        with open('decrypted_file.txt', 'wb') as file:
            file.write(decrypted_data)
        print("File successfully written!")

        connection.send(b'Data received and decrypted successfully.')

    except Exception as e:
        print(f'An error occurred: {e.__class__.__name__}: {e}')
        try:
            connection.send(b'An error occurred while processing the data.')
        except:
            pass

    finally:
        connection.close()
        s.close()

start_server()
