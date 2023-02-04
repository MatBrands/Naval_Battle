from socket import *

class ClientServer:
    def __init__(self, status: str, host='localhost', port=55552) -> None:
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.status = status
        self.host = host
        self.port = port
        self.setup()
        
    def setup(self):
        try:
            if self.status in 'client':
                self.socket.connect((self.host, self.port))
            else:
                self.socket.bind((self.host, self.port))
                self.socket.listen(1)
        except:
            print('Erro !')
            exit()
            
    