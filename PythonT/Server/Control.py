import socket, select, string, sys
import Server.Model as Model

class controller:
    def __init__(self):
        self.HOST = 'localhost'
        self.PORT = 8000
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen(5)
        self.conn, self.addr = self.s.accept()
        self.db=Model.DB()

    def fromClient(self):
        try:
            with self.conn:
                print("Connected by:", self.addr)
                while True:
                    data=self.conn.recv(1024)
                    Data=data.decode()

                    print(Data)
                    self.toClient(Data)
                    if not data:
                        break
        finally:
            self.s.close()


    def toClient(self,data):

        a=data.split(",")
        if a[0]=="SignIn":
            self.conn.sendall(self.db.SignIn(a[1],a[2]).encode())
        if a[0]=="SignUp":
            self.conn.sendall(self.db.SignUp(a[1],a[2],a[3],a[4]).encode())
        if a[0]=="SignOut":
            self.conn.sendall(self.db.SignOut().encode())
        if a[0]=="AddFr":
            self.conn.sendall(self.db.AddFr(a[1]).encode())
        if a[0]=="block":
            self.conn.sendall(self.db.Block(a[1]).encode())
        if a[0]=="Sendmess":
            self.conn.sendall(self.db.Sendmess(a[1],a[2]).encode())
        if a[0]=="Showmess":
            self.conn.sendall(self.db.Showmess().encode())
        if a[0]=="ShowFr":
            self.conn.sendall(self.db.ShowFr().encode())
c= controller()
c.fromClient()