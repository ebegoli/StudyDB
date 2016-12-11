import socket
import sys

HOST, PORT = "localhost", 9999
host, port = "", None
username, password = "",""
data = " ".join(sys.argv[1:])


def connect():
    print("\t**********************************************")
    print("\t***  StudyDB client - welcome              ***")
    print("\t**********************************************")
    host = input("host (default: localhost):")
    if host is None:
        host = HOST
    port = input("port (default: 9999):")
    if port is None:
        port = PORT
    username = input("username:")
    password = input("password:")

def communicate():
    response = "ebegoli;ebegoli;default."
    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((host, port))
        while (True):
            sock.sendall(response + "\n")
            # Receive data from the server and shut down
            received = sock.recv(1024)
            response = input(received)
    finally:
        print "Connection failed."
        sock.close()


if __name__ == '__main__':
    connect()
    communicate()
