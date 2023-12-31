import os
import tkinter as tk
import tkinter.ttk as TTK
from tkinter import messagebox, messagebox, filedialog
from tkcalendar import DateEntry
import hashlib
import datetime
import re

class Obj:
    def __init__(self, student, id, name, dob, dop, phone, cccd, active):
        self.student = student
        self.id = id
        self.name = name
        self.dob = dob
        self.dop = dop
        self.phone = phone
        self.cccd = cccd
        self.active = active
    def setId(self, id):
        self.id = id
    def setName(self, name):
        self.name = name
    def setDob(self, dob):
        self.dob = dob
    def setDop(self, dop):
        self.dop = dop
    def setPhone(self, phone):
        self.phone = phone
    def setCccd(self, cccd):
        self.cccd = cccd
    def setActive(self, active):
        self.active = active
    def getStudent(self):
        return self.student 
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getDob(self):
        return self.dob
    def getDop(self):
        return self.dop
    def getPhone(self):
        return self.phone
    def getCccd(self):
        return self.cccd
    def getActive(self):
        return self.active
    def getMyObj(self):
        print(self.student )
        print(self.id )
        print(self.name )
        print(self.dob )
        print(self.dop )
        print(self.phone )
        print(self.cccd )
        print(self.active )

salt_len = 8
def hash_password(password, salt_len):
    salt = os.urandom(salt_len)
    hashed_password = hashlib.sha256(password.encode()).digest() + salt
    return hashed_password.hex()
def get_digest(password_hex, salt_len):
    password_digest = bytes.fromhex(password_hex)
    return password_digest[:len(password_digest) - salt_len]
def validate_password(input, from_dir, salt_len):
    hashed_password = hashlib.sha256(input.encode()).digest()
    from_dir = get_digest(from_dir, salt_len)
    if hashed_password == from_dir:
        return True
    return False

def forget_old_widgets(frame: tk.Frame):
    if frame.children:
        for name, widget in list(frame.children.items()):
            if name != 'loginframe':
                widget.destroy()
def decimalToBinary(n): 
    return int(bin(n).replace("0b", ""))
def create_arrays(address, name, size):
    file_path = address + "/" + name
    size_bytes = size * 1024 * 1024 
    with open(file_path, 'wb') as fileList:
        fileList.seek(0)
        size_in_byte = size_bytes.to_bytes(4, byteorder='big')
        fileList.write(size_in_byte)
        fileList.seek(4)
        name_in_byte = bytes(name, 'utf-8')
        fileList.write(name_in_byte)
        now = datetime.datetime.now()
        fileList.seek(101)
        
        time_in_bin = format(decimalToBinary(now.hour),'#05') + format(decimalToBinary(now.minute),'#06') + format(decimalToBinary(int(now.second/2)),'#05')
        time_in_byte = int(time_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(time_in_byte)

        date_in_bin = format(decimalToBinary(now.year-1980),'#07') + format(decimalToBinary(now.month),'#04') + format(decimalToBinary(now.day), '#05')
        date_in_byte = int(date_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(date_in_byte)
        
        fileList.seek(111)
        posTeacher = 512
        fileList.write(posTeacher.to_bytes(2, byteorder='big'))
        fileList.seek(115)
        posStudent = 32512
        fileList.write(posStudent.to_bytes(2, byteorder='big'))
        
        fileList.write(b'\0' * (int(size_bytes)))
    return True  

def format_arrays(arrays, name):
    with open(arrays, 'rb') as fileList:
        default_data = fileList.read()
        fileList.seek(0)
        size = int.from_bytes(fileList.read(4),byteorder='big')
    with open(arrays, 'wb') as fileList:
        fileList.seek(0)
        fileList.write(default_data) 
        fileList.seek(4)
        name_in_byte = bytes(name, 'utf-8')
        fileList.write(name_in_byte)
        now = datetime.datetime.now()
        fileList.write(b'\0' * (size))
        
        fileList.seek(101)
        time_in_bin = format(decimalToBinary(now.hour),'#05') + format(decimalToBinary(now.minute),'#06') + format(decimalToBinary(int(now.second/2)),'#05')
        time_in_byte = int(time_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(time_in_byte)

        date_in_bin = format(decimalToBinary(now.year-1980),'#07') + format(decimalToBinary(now.month),'#04') + format(decimalToBinary(now.day), '#05')
        date_in_byte = int(date_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(date_in_byte)

        fileList.seek(111)
        posTeacher = 512
        fileList.write(posTeacher.to_bytes(2, byteorder='big'))
        fileList.seek(115)
        posStudent = 32512
        fileList.write(posStudent.to_bytes(2, byteorder='big'))

    filename = str(arrays)
    elements = filename.split('/')
    addr = '/'.join(elements[:-1])
    name = addr + '/' + name
    os.rename(filename, name)
    return True  

def setpass_arrays(arrays, oldpw, newpw):
    check = hash_password(oldpw, int(salt_len))
    isPass = b'\x00'
    with open(arrays, 'rb') as fileList:
        default_data = fileList.read()
        fileList.seek(20)
        isPass = fileList.read(1)
        fileList.seek(21)
        passhase = fileList.read(len(check))
        pass_hashed = passhase[:len(check)].decode()
    
    with open(arrays, 'wb') as fileList:
        if (isPass != b'\x00'):
            if validate_password(oldpw, pass_hashed, int(salt_len)):
                fileList.seek(0)
                fileList.write(default_data)
                fileList.seek(20)
                c = 1
                fileList.write(c.to_bytes(c, byteorder='big'))
                newpw_in_byte = bytes(hash_password(newpw, salt_len),'utf-8')
                fileList.seek(21)
                fileList.write(newpw_in_byte)
                fileList.seek(105)
                now = datetime.datetime.now()
                time_in_bin = format(decimalToBinary(now.hour),'#05') + format(decimalToBinary(now.minute),'#06') + format(decimalToBinary(int(now.second/2)),'#05')
                time_in_byte = int(time_in_bin, 2).to_bytes(2, byteorder='big')
                fileList.write(time_in_byte)

                date_in_bin = format(decimalToBinary(now.year-1980),'#07') + format(decimalToBinary(now.month),'#04') + format(decimalToBinary(now.day), '#05')
                date_in_byte = int(date_in_bin, 2).to_bytes(2, byteorder='big')
                fileList.write(date_in_byte)
            else: 
                fileList.seek(0)
                fileList.write(default_data)
                messagebox.showerror(title='LỖI', message='Mật khẩu cũ list không đúng!')
                return False
        else:
            fileList.seek(0)
            fileList.write(default_data)
            fileList.seek(20)
            c = 1
            fileList.write(c.to_bytes(c, byteorder='big'))
            newpw_in_byte = bytes(hash_password(newpw, salt_len),'utf-8')
            fileList.seek(21)
            fileList.write(newpw_in_byte)

            fileList.seek(105)
            now = datetime.datetime.now()
            time_in_bin = format(decimalToBinary(now.hour),'#05') + format(decimalToBinary(now.minute),'#06') + format(decimalToBinary(int(now.second/2)),'#05')
            time_in_byte = int(time_in_bin, 2).to_bytes(2, byteorder='big')
            fileList.write(time_in_byte)

            date_in_bin = format(decimalToBinary(now.year-1980),'#07') + format(decimalToBinary(now.month),'#04') + format(decimalToBinary(now.day), '#05')
            date_in_byte = int(date_in_bin, 2).to_bytes(2, byteorder='big')
            fileList.write(date_in_byte)
    
    return True   

def open_arrays(arrays):
    mytuple = []
    listTeacher = []
    listStudent = []
    with open(arrays, 'rb') as fileList:
        all = fileList.read()
        fileList.seek(101)
        d1 = fileList.read(2)
        d2 = fileList.read(2)
        d3 = fileList.read(2)
        d4 = fileList.read(2)
        timefile = printtime(d1, d2, d3, d4)
        fileList.seek(109)
        nTeacher = 0
        nTeacher = int.from_bytes(fileList.read(2),byteorder='big')
        posTeacher = int.from_bytes(fileList.read(2),byteorder='big')
        nStudent = 0
        nStudent = int.from_bytes(fileList.read(2),byteorder='big')
        posStudent = int.from_bytes(fileList.read(2),byteorder='big')
        
        def getObj(student, id_in_byte, name_in_byte, 
                   dob_in_byte, dop_in_byte, 
                   phone_in_byte, cccd_in_byte, 
                   active_in_byte):
            
            id_in_bin = (decimalToBinary(int(id_in_byte.hex(), 16)))
            a = (format(id_in_bin, '#024'))
            id = str(int(a[:7],2)) + str(int(a[7:14],2)) + str(int(a[14:],2)) 
            #print(id)
            name = name_in_byte.decode('utf-8').replace('\x00','')
            #print(name)
            dob_in_bin = (decimalToBinary(int(dob_in_byte.hex(), 16)))
            a = (format(dob_in_bin, '#016'))
            dob = str(int(a[-5:],2)) + '-' + str(int(a[-9:-5],2)) + '-'+ str(int(a[:7],2)+1980)
            #print(dob)
            dop_in_bin = (decimalToBinary(int(dop_in_byte.hex(), 16)))
            a = (format(dop_in_bin, '#016'))
            dop = str(int(a[-5:],2)) + '-' + str(int(a[-9:-5],2)) + '-'+ str(int(a[:7],2)+1980)
            #print(dop)
            phone_in_bin =(decimalToBinary(int(phone_in_byte.hex(), 16)))
            a = (format(phone_in_bin, '#032'))
            phone = format(int(a[:8],2),'#03')  + format(int(a[8:18],2),'#03') + format(int(a[18:],2),'#04')
            #print(phone)
            cccd_in_bin = (decimalToBinary(int(cccd_in_byte.hex(), 16)))
            a = (format(cccd_in_bin, '#032'))
            cccd = format(int(a[:6],2),'#03')  + format(int(a[6:14],2),'#03') + format(int(a[14:],2),'#06')
            #print(cccd)
            active = int(active_in_byte.hex(), 16)
            o = Obj(student, id, name, dob, dop, phone, cccd, active)
            return o
        
        fileList.seek(posTeacher)
        if nTeacher != 0:
            for i in range(nTeacher):
                id_in_byte = fileList.read(3)
                name_in_byte = fileList.read(16)
                dob_in_byte = fileList.read(2)
                dop_in_byte = fileList.read(2)
                phone_in_byte = fileList.read(4)
                cccd_in_byte = fileList.read(4)
                active_in_byte = fileList.read(1)
                oT = getObj(0, id_in_byte, name_in_byte, 
                    dob_in_byte, dop_in_byte, 
                    phone_in_byte, cccd_in_byte, 
                    active_in_byte)
                listTeacher.append(oT)
        fileList.seek(posStudent)
        if nStudent != 0:
            for i in range(nStudent):
                ids_in_byte = fileList.read(3)
                names_in_byte = fileList.read(16)
                dobs_in_byte = fileList.read(2)
                dops_in_byte = fileList.read(2)
                phones_in_byte = fileList.read(4)
                cccds_in_byte = fileList.read(4)
                actives_in_byte = fileList.read(1)
                oS = getObj(1, ids_in_byte, names_in_byte, 
                    dobs_in_byte, dops_in_byte, 
                    phones_in_byte, cccds_in_byte, 
                    actives_in_byte)
                listStudent.append(oS)
    mytuple.append(nTeacher)        # 0 
    mytuple.append(posTeacher)      # 1
    mytuple.append(listTeacher)       # 2
    mytuple.append(nStudent)         # 3
    mytuple.append(posStudent)        # 4
    mytuple.append(listStudent)      # 5
    mytuple.append(timefile)        # 6
    return mytuple 

def import_obj_in(arrays, obj):
    mytuple = open_arrays(arrays)
    with open(arrays, 'rb') as fileList:
        default_data = fileList.read() 
        fileList.seek(0)
        arrayssize = int.from_bytes(fileList.read(4),byteorder='big')

    with open(arrays, 'wb') as fileList:
        fileList.seek(0)
        fileList.write(default_data) 

        if (obj.getStudent() == 0):
            fileList.seek(109)
            nTeacher = len(mytuple[2]) + 1
            fileList.write(nTeacher.to_bytes(2, byteorder='big'))
            curPos = mytuple[1] + 32*len(mytuple[2])
            
        else:
            fileList.seek(113)
            nStudent = len(mytuple[5]) + 1
            fileList.write(nStudent.to_bytes(2, byteorder='big'))
            curPos = mytuple[4] + 32*len(mytuple[5])
        
        ##mã số
        fileList.seek(curPos)
        id_in_bin = format(decimalToBinary(int(obj.getId()[:2])),'#07') + format(decimalToBinary(int(obj.getId()[2:5])),'#07') + format(decimalToBinary(int(obj.getId()[5:])),'#010')
        id_in_byte = int(id_in_bin, 2).to_bytes(3, byteorder='big')
        fileList.write(id_in_byte)
        ##họ và tên
        name_in_byte = bytes(obj.getName(), 'utf-8')
        fileList.write(name_in_byte)
        ##ngày sinh
        fileList.seek(curPos+19)
        dob = str(obj.getDob())
        #print(dob)
        day = dob.split('-')[2]
        month = dob.split('-')[1]
        year = dob.split('-')[0]
        dob_in_bin = format(decimalToBinary(int(year)-1980),'#07') + format(decimalToBinary(int(month)),'#04') + format(decimalToBinary(int(day)), '#05')
        dob_in_byte = int(dob_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(dob_in_byte)
        ##ngày tham gia
        dop = str( obj.getDop())
        day = dop.split('-')[2]
        month = dop.split('-')[1]
        year = dop.split('-')[0]
        dop_in_bin = format(decimalToBinary(int(year)-1980),'#07') + format(decimalToBinary(int(month)),'#04') + format(decimalToBinary(int(day)), '#05')
        dop_in_byte = int(dop_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(dop_in_byte)
        ##số đt
        phone_in_bin = format(decimalToBinary(int(obj.getPhone()[:3])),'#08') + format(decimalToBinary(int(obj.getPhone()[3:6])),'#010') + format(decimalToBinary(int(obj.getPhone()[6:])),'#014')
        phone_in_byte = int(phone_in_bin, 2).to_bytes(4, byteorder='big')
        fileList.write(phone_in_byte)
        ##số cccd
        cccd_in_bin = format(decimalToBinary(int(obj.getCccd()[:3])),'#07') + format(decimalToBinary(int(obj.getCccd()[3:6])),'#07') + format(decimalToBinary(int(obj.getCccd()[6:])),'#018')
        cccd_in_byte = int(cccd_in_bin, 2).to_bytes(4, byteorder='big')
        fileList.write(cccd_in_byte)
        ##trạng thái
        active = 1
        active_in_byte = active.to_bytes(1, byteorder='big')
        fileList.write(active_in_byte)

        fileList.seek(105)
        now = datetime.datetime.now()
        time_in_bin = format(decimalToBinary(now.hour),'#05') + format(decimalToBinary(now.minute),'#06') + format(decimalToBinary(int(now.second/2)),'#05')
        time_in_byte = int(time_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(time_in_byte)

        date_in_bin = format(decimalToBinary(now.year-1980),'#07') + format(decimalToBinary(now.month),'#04') + format(decimalToBinary(now.day), '#05')
        date_in_byte = int(date_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(date_in_byte)
        
    return True

def deleObj(arrays, id, isStudent):
    mytuple = open_arrays(arrays)
    if isStudent:
        k = 3
    else:
        k = 0
    numlist = mytuple[k]
    poslist = mytuple[k+1]
    j = 0
    for i in mytuple[k+2]:
        if i.getId() == id:
            break
        j = j + 1 
    with open(arrays, 'rb') as fileList:
        default_data = fileList.read() 
        #arrayssize = int.from_bytes(fileList.read(4),byteorder='big')

    with open(arrays, 'wb') as fileList:
        fileList.seek(0)
        fileList.write(default_data) 
        fileList.seek(poslist + j*32 + 31)
        active = 0
        active_in_byte = active.to_bytes(1, byteorder='big')
        fileList.write(active_in_byte)
        
        fileList.seek(105)
        now = datetime.datetime.now()
        time_in_bin = format(decimalToBinary(now.hour),'#05') + format(decimalToBinary(now.minute),'#06') + format(decimalToBinary(int(now.second/2)),'#05')
        time_in_byte = int(time_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(time_in_byte)

        date_in_bin = format(decimalToBinary(now.year-1980),'#07') + format(decimalToBinary(now.month),'#04') + format(decimalToBinary(now.day), '#05')
        date_in_byte = int(date_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(date_in_byte)
    return True

def recoverObj(arrays, id, isStudent):
    mytuple = open_arrays(arrays)
    if isStudent:
        k = 3
    else:
        k = 0
    numlist = mytuple[k]
    poslist = mytuple[k+1]
    j = 0
    for i in mytuple[k+2]:
        if i.getId() == id:
            break
        j = j + 1 
    with open(arrays, 'rb') as fileList:
        default_data = fileList.read() 
        #arrayssize = int.from_bytes(fileList.read(4),byteorder='big')

    with open(arrays, 'wb') as fileList:
        fileList.seek(0)
        fileList.write(default_data) 
        fileList.seek(poslist + j*32 + 31)
        active = 1
        active_in_byte = active.to_bytes(1, byteorder='big')
        fileList.write(active_in_byte)
        
        fileList.seek(105)
        now = datetime.datetime.now()
        time_in_bin = format(decimalToBinary(now.hour),'#05') + format(decimalToBinary(now.minute),'#06') + format(decimalToBinary(int(now.second/2)),'#05')
        time_in_byte = int(time_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(time_in_byte)

        date_in_bin = format(decimalToBinary(now.year-1980),'#07') + format(decimalToBinary(now.month),'#04') + format(decimalToBinary(now.day), '#05')
        date_in_byte = int(date_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(date_in_byte)
    return True

def editObj(arrays, obj, vitri):

    mytuple = open_arrays(arrays)
    with open(arrays, 'rb') as fileList:
        default_data = fileList.read() 
        fileList.seek(0)

    with open(arrays, 'wb') as fileList:
        fileList.seek(0)
        fileList.write(default_data) 

        if (obj.getStudent() == 0):
            curPos = mytuple[1] + 32*vitri
        else:
            curPos = mytuple[4] + 32*vitri
        
        ##mã số
        fileList.seek(curPos)
        id_in_bin = format(decimalToBinary(int(obj.getId()[:2])),'#07') + format(decimalToBinary(int(obj.getId()[2:5])),'#07') + format(decimalToBinary(int(obj.getId()[5:])),'#010')
        id_in_byte = int(id_in_bin, 2).to_bytes(3, byteorder='big')
        fileList.write(b'\0' * (3))
        fileList.seek(curPos)
        fileList.write(id_in_byte)
        ##họ và tên
        name_in_byte = bytes(obj.getName(), 'utf-8')
        fileList.write(b'\0' * (16))
        fileList.seek(curPos+3)
        fileList.write(name_in_byte)
        ##ngày sinh
        fileList.seek(curPos+19)
        fileList.write(b'\0' * (2))
        dob = str(obj.getDob())
        #print(dob)
        year = dob.split('-')[0]
        day = dob.split('-')[2]
        if len(dob.split('-')[2]) == 4:
            year = dob.split('-')[2]
            day = dob.split('-')[0]
        month = dob.split('-')[1]
        dob_in_bin = format(decimalToBinary(int(year)-1980),'#07') + format(decimalToBinary(int(month)),'#04') + format(decimalToBinary(int(day)), '#05')
        dob_in_byte = int(dob_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.seek(curPos+19)
        fileList.write(dob_in_byte)
        ##ngày tham gia
        dop = str(obj.getDop())
        #print(dob)
        year = dop.split('-')[0]
        day = dop.split('-')[2]
        if len(dop.split('-')[2]) == 4:
            year = dop.split('-')[2]
            day = dop.split('-')[0]
        month = dop.split('-')[1]
        dop_in_bin = format(decimalToBinary(int(year)-1980),'#07') + format(decimalToBinary(int(month)),'#04') + format(decimalToBinary(int(day)), '#05')
        dop_in_byte = int(dop_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(b'\0' * (2))
        fileList.seek(curPos+21)
        fileList.write(dop_in_byte)
        ##số đt
        phone_in_bin = format(decimalToBinary(int(obj.getPhone()[:3])),'#08') + format(decimalToBinary(int(obj.getPhone()[3:6])),'#010') + format(decimalToBinary(int(obj.getPhone()[6:])),'#014')
        phone_in_byte = int(phone_in_bin, 2).to_bytes(4, byteorder='big')
        fileList.write(b'\0' * (4))
        fileList.seek(curPos+23)
        fileList.write(phone_in_byte)
        ##số cccd
        cccd_in_bin = format(decimalToBinary(int(obj.getCccd()[:3])),'#07') + format(decimalToBinary(int(obj.getCccd()[3:6])),'#07') + format(decimalToBinary(int(obj.getCccd()[6:])),'#018')
        cccd_in_byte = int(cccd_in_bin, 2).to_bytes(4, byteorder='big')
        fileList.write(b'\0' * (4))
        fileList.seek(curPos+27)
        fileList.write(cccd_in_byte)
        ##trạng thái
        active = 1
        active_in_byte = active.to_bytes(1, byteorder='big')
        fileList.write(b'\0' * (1))
        fileList.seek(curPos+31)
        fileList.write(active_in_byte)

        fileList.seek(105)
        now = datetime.datetime.now()
        time_in_bin = format(decimalToBinary(now.hour),'#05') + format(decimalToBinary(now.minute),'#06') + format(decimalToBinary(int(now.second/2)),'#05')
        time_in_byte = int(time_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(time_in_byte)

        date_in_bin = format(decimalToBinary(now.year-1980),'#07') + format(decimalToBinary(now.month),'#04') + format(decimalToBinary(now.day), '#05')
        date_in_byte = int(date_in_bin, 2).to_bytes(2, byteorder='big')
        fileList.write(date_in_byte)
        
    return True

def printtime(timec_in_byte, datec_in_byte, timeu_in_byte, dateu_in_byte):
    l = []
    datec_in_bin = (decimalToBinary(int(datec_in_byte.hex(), 16)))
    a = (format(datec_in_bin, '#016'))
    datec = str(int(a[-5:],2)) + '-' + str(int(a[-9:-5],2)) + '-'+ str(int(a[:7],2)+1980)
    l.append(datec)
    timec_in_bin = (decimalToBinary(int(timec_in_byte.hex(), 16)))
    a = (format(timec_in_bin, '#016'))
    timec = str(int(a[:5],2)) +  ':' + str(int(a[-11:-5],2)) + ':' + str(int(a[-5:],2)*2) 
    l.append(timec)
    dateu_in_bin = (decimalToBinary(int(dateu_in_byte.hex(), 16)))
    a = (format(dateu_in_bin, '#016'))
    dateu = str(int(a[-5:],2)) + '-' + str(int(a[-9:-5],2)) + '-'+ str(int(a[:7],2)+1980)
    l.append(dateu)
    timeu_in_bin = (decimalToBinary(int(timeu_in_byte.hex(), 16)))
    a = (format(timeu_in_bin, '#016'))
    timeu = str(int(a[:5],2)) +  ':' + str(int(a[-11:-5],2)) + ':' + str(int(a[-5:],2)*2) 
    l.append(timeu)
    return l

def getArraysize(list):
    with open(list, 'rb') as fileList:
        fileList.read()
        return fileList.tell()

def swap_cont(data):
    data = bytearray(data)
    data[0], data[1] = data[1], data[0]
    return bytes(data)