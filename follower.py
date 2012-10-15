import SocketServer
from threading import Thread

class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024*9).strip()
        print self.data
        
def  server_up():
    HOST, PORT = "localhost", 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    print "SERVERUP"
    server.serve_forever()

thread = Thread(target = server_up)
thread.start()

