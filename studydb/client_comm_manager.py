# import SocketServer
# import socket
# import threading
#
# """ Client communication manager handles the communication between the database clients and the database.
#     It delegates authentication t
#
# TODO: implement this http://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client
# """
# class TCPClientHandler(SocketServer.StreamRequestHandler):
#
#     def handle(self):
#         # self.rfile is a file-like object created by the handler;
#         # we can now use e.g. readline() instead of raw recv() calls
#         self.data = self.rfile.readline().strip()
#         credentials = self.data.split(";")
#         print credentials
#         # TODO: Call here client manager thread to handle the client interaction with the database
#         print "{} wrote:".format(self.client_address[0])
#         print self.data
#         # Likewise, self.wfile is a file-like object used to write back
#         # to the client
#         self.wfile.write(">Connected to studyDB.\n>")
#
#
# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999
#
#     # Create the server, binding to localhost on port 9999
#     server = SocketServer.TCPServer((HOST, PORT), TCPClientHandler)
#
#     # Activate the server; this will keep running until you
#     # interrupt the program with Ctrl-C
#     server.serve_forever()

""" This is an implementation of the client communication manager component that manages \
        connections from the clients. It passes the execution of the queries to query parser and other components.
"""


from socket import *
import thread, threading

import query_parser

BUFF = 1024
HOST = '127.0.0.1'# must be input parameter @TODO
PORT = 9999 # must be input parameter @TODO
def response(content):
    """ Responder for the client """
    return ">{}\n>".format(content)

def handler(clientsock,addr):
    """ Main handler method for the thread """
    print  threading.current_thread()
    clientsock.send(">")
    while 1:
        data = clientsock.recv(BUFF)
        if not data:
            break
        print repr(addr) + ' recv:' + repr(data)
        clientsock.send(response(query_parser.parse(data)))
        print repr(addr) + ' sent:' + repr(response(data))
        if "exit;" == data.rstrip():
            break # type 'close' on client console to close connection from the server side

    clientsock.close()
    print addr, "- closed connection" #log on console

if __name__=='__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    while 1:
        print 'waiting for connection... listening on port', PORT
        clientsock, addr = serversock.accept()
        print '...connected from:', addr
        thread.start_new_thread(handler, (clientsock, addr))
