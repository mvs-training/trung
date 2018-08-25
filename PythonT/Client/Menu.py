import socket, select, string, sys

s= SOCKET.Socket()

while(True):
    print("1.Sign in")
    print("2.Sign up")
    print("3.Sign out")
    print("4.Add friends")
    print("5.Block")
    print("6.Send mess")
    print("7.Show mess")
    print("8.Show friends")
    print("9.exit")
    select=input()
    if select==int("9"):
        break
    elif (1<=int (select) and int (select)<=8):
        s.toServer(int(select))
        print(s.fromServer())
    else:
        print("Nhap lai")
class Socket:

    def __init__(self):
        self.HOST="localhost"
        self.PORT=8000
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.HOST,self.PORT))


    def toServer(self,select):
        if select==1:
            self.s.sendall(self.Signin().encode())
        if select==2:
            self.s.sendall(self.Signup().encode())
        if select==3:
            self.s.sendall(self.Signout().encode())
        if select==4:
            self.s.sendall(self.Addfr().encode())
        if select==5:
            self.s.sendall(self.Block().encode())
        if select==6:
            self.s.sendall(self.sendmess().encode())
        if select==7:
            self.s.sendall(self.showmess().encode())
        if select==8:
            self.s.sendall(self.showFr().encode())
    def fromServer(self):
        data=self.s.recv(1024)
        return data.decode()



    def Signin(self):
        print("Tai khoan:")
        taikhoan=input()
        print("Mat khau:")
        matkhau=input()
        data=""
        data=data+"dangnhap"+","+taikhoan+","+matkhau
        return data



    def Signup(self):
        print("Tai khoan:")
        taikhoan=input()
        print("Mat khau:")
        matkhau=input()
        print("Ho va ten:")
        hoten=input()
        print("Thanh pho:")
        thanhpho=input()
        data=""
        data=data+"dangky"+","+taikhoan+","+matkhau+","+hoten+","+thanhpho
        return data



    def Signout(self):
        data="dangxuat"
        return data


    def Addfr(self):
        print("Muon ket ban voi tai khoan:")
        taikhoan=input()
        data=""
        data=data+"ketban"+","+taikhoan
        return data



    def Block(self):
        print("Muon block tai khoan:")
        taikhoan=input()
        data=""
        data=data+"block"+","+taikhoan
        return data



    def sendmess(self):
        print("Gui tin nhan den tai khoan:")
        taikhoan=input()
        print("Noi dung tin nhan")
        noidung=input()
        data=""
        data=data+"guitinnhan"+","+taikhoan+","+noidung
        return data



    def showmess(self):
        result="xemtinnhan"
        return result


    def showFr(self):
        result="danhsachbanbe"
        return result