import sqlite3 as sql

class Model:

    def __init__(self):
        self.conn= sql.connect("Bui.db")
        self.flag= 0
        self.nguoidung=" "

    def connectDB(self):
        self.conn=sql.connect("Bui.db")



    def disconnectDB(self):
        self.conn.close()



    def SignIn(self,username,password):
        self.connectDB()
        c=self.conn.cursor()
        c.execute("select * from Nguoidung where taiKhoan= ? and matKhau=?", (username,password))
        a=c.fetchall()
        if a.__len__()==0:
            result= "Pass or Username incorrect!!!!"
            self.disconnectDB()
            return result
        else :
            result= "SignIn Correct!!!"
            self.flag=1
            self.nguoidung=username
            self.disconnectDB()
            return result



    def SignUp(self,username, password,hoten,thanhpho):
        self.connectDB()
        try:
            c=self.conn.cursor()
            c.execute("insert into Nguoidung values(?,?,?,?)",(username,password,hoten,thanhpho))
        except:
            result="Fail!!"
            self.disconnectDB()
            return  result
        self.conn.commit()
        self.disconnectDB()
        result="SignUp Correct!!!!"
        return result



    def SignOut(self):
        self.flag=0
        self.nguoidung=""
        result = "SignOut Correct!!!"
        self.disconnectDB()
        return result

    def IsLogin(self,taikhoan):
        c=self.conn.cursor()
        c.execute("select * from Nguoidung where taiKhoan=?",(taikhoan,))
        a=c.fetchall()
        if a.__len__()==0:
            return 0
        return  1


    def isBlock(self,taikhoan):
        c=self.conn.cursor()
        trangThai1= "ban be"
        trangThai2= "block"
        c.execute("select * from Trangthai where Nguoidung1=? and nNguoidung2=? and trangThai=?",(self.nguoidung,taikhoan,trangThai1))
        a=c.fetchall()
        if a.__len__()==1:
            result ="ban be"
            return result
        c.execute("select * from Trangthai where Nguoidung1=? and Nguoidung2=? and trangThai=?",(self.nguoidung,taikhoan,trangThai2))
        a=c.fetchall()
        if a.__len__()==1:
            result="block"
            return result
        return 0    

    def AddFr(self,taikhoan):
        self.connectDB()
        trangThai="ban be"
        if self.flag==0:
            result= "Not SignIn!!!!"
            self.disconnectDB()
            return result
        if self.kiemtrataikhoan(taikhoan)==0:
            self.disconnectDB()
            result="Choose your patner: "
            return result
        if self.kiemtratrangthai(taikhoan)== "ban be":
            result="Correct!!!"
            self.disconnectDB()
            return result
        if self.kiemtratrangthai(taikhoan)=="block":
            c=self.conn.cursor()
            c.execute("update Trangthai set trangThai='ban be' where Nguoidung1=? and nNguoidung2=? ",(self.nguoidung,taikhoan))
            self.conn.commit()
            c.execute("update Trangthai set trangThai='ban be' where Nguoidung1=? and Nguoidung2=? ",(taikhoan,self.nguoidung))
            self.conn.commit()
            result="=> Friend!!!!"
            self.disconnectDB()
            return result
        if self.kiemtratrangthai(taikhoan)==0:
            c=self.conn.cursor()
            c.execute("insert into Trangthai values(?,?,?)",(self.nguoidung,taikhoan,trangThai))
            self.conn.commit()
            c.execute("insert into Trangthai values(?,?,?)",(taikhoan,self.nguoidung,trangThai))
            self.conn.commit()
            result="AddFrienf Correct!!!"
            self.disconnectDB()
            return result

    def Sendmess(self,taikhoan,noidung):
        if self.flag==0:
            result ="Not SignIn!!!"
            return  result
        self.connectDB()
        if self.kiemtrataikhoan(taikhoan)==0:
            result="Username not avaible!!"
            self.disconnectDB()
            return result
        if self.kiemtratrangthai(taikhoan)=="block":
            result="Username is Blocked!!!"
            self.disconnectDB()
            return result
        c=self.conn.cursor()
        trangthai="chua doc"
        c.execute("insert into Messenger values(?,?,?,?)",(self.nguoidung,taikhoan,noidung,trangthai))
        self.conn.commit()
        result="Send it!!!1"
        return result

    def Block(self, taikhoan):
        self.connectDB()
        trangThai = "block"
        if self.flag == 0:
            result = "Not SignIn!!!"
            self.disconnectDB()
            return result
        if self.kiemtrataikhoan(taikhoan) == 0:
            self.disconnectDB()
            result = "Tai khoan muon block ko ton tai"
            return result
        if self.kiemtratrangthai(taikhoan) == "block":
            result = "tai khoan nay da duoc block roi"
            self.disconnectDB()
            return result
        if self.kiemtratrangthai(taikhoan) == "ban be":
            c = self.conn.cursor()
            c.execute("update Trangthai set trangThai='block' where Nguoidung1=? and Nguoidung2=? ",(self.nguoidung, taikhoan))
            self.conn.commit()
            c.execute("update Trangthai set trangThai='block' where Nguoidung1=? and Nguoidung2=? ",(taikhoan, self.nguoidung))
            self.conn.commit()
            result = "Chuyen tu ban be sang block thanh cong"
            self.disconnectDB()
            return result
        if self.kiemtratrangthai(taikhoan) == 0:
            c = self.conn.cursor()
            c.execute("insert into Trangthai values(?,?,?)", (self.nguoidung, taikhoan, trangThai))
            self.conn.commit()
            c.execute("insert into Trangthai values(?,?,?)", (taikhoan, self.nguoidung, trangThai))
            self.conn.commit()
            result = "block thanh cong"
            self.disconnectDB()
            return result



    

    def Showmess(self):
        self.connectDB()
        if self.flag==0:
            result="Not SignIn !!!"
            self.disconnectDB()
            return result
        c=self.conn.cursor()
        c.execute("select * from Messenger where Nguoidung1=?",(self.nguoidung,))
        print("Cac tin nhan "+self.nguoidung+" da gui:")
        data=""
        for row in c:
            data=data+"Nguoi gui:"+row[0]+"\n"+"Nguoi nhan:"+row[1]+"\n"+"Noi dung tin nhan:"+row[2]+"\n"+"Trang thai tin nhan:"+row[3]+"\n"
        return data


    def ShowFr(self):
        if self.flag==0:
            result="Not SignIn!!!"
            return result
        self.connectDB()
        c=self.conn.cursor()
        c.execute("select * from Trangthai where Nguoidung1=? and trangThai='ban be'",(self.nguoidung,))
        print("Danh sach ban be cua:"+self.nguoidung)
        data=""
        for row in c:
           data=data+ row[1]+"\n"
        return data









