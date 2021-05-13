import socket
import collections
import time

def send( message, listeners ):
    #print( "the listeners listen..." )
    brokenListeners = []
    for listener in listeners:
        try:
            listener.send( message )
        except socket.timeout:
            pass
        except socket.error:
            brokenListeners.append( listener )
            listener.close()

    #   remove any broken connections
    for brokenListener in brokenListeners:
        listeners.remove( brokenListener )
        brokenListener.close()
        print( "LSTN left." )

    sendMessageToAllListeners( bytesFromSpeaker, listeners )

#   log new client joining to server terminal
def logNewClientJoining( clientType, newClientIPAddress ):
    print( time.strftime("%Y-%m-%d %H:%M"), " ", clientType, " joined. ", newClientIPAddress )

class Broadcaster:
    def __init__(self, host="127.0.0.1", port=8080):
        self.host = 
        self.port = 

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(5)
        # self.s.setblocking(0)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.HOST, self.PORT))

        self.connections = []

    def listen(self):
        self.s.listen(5)
        self.s.settimeout( 0.001 )
        while True:
            new_connection = None
            new_connection_address = None
            try:
                new_connection, new_connection_address = s.accept()
            except socket.timeout:
                pass
            if new_connection is not None:
                    new_connection.settimeout(1.0)
                    connections.append(new_connection)
                    timestamp = time.strftime("%Y-%m-%d %H:%M")
                    print( f"{timestamp}: {new_connection_address} joined.")
            checkForNewMessages( speakers, listeners )