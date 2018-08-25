
from Menu import Socket
s= SOCKET.Socket()

while(True):
    print("1.Sign in")
    print("2.Sign up")
    print("3.sign out")
    print("4.add friends")
    print("5.Block")
    print("6.send mess")
    print("7.show mess")
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


