import tkinter as tk
from components.utils import *

window_height = 400
window_width = 600

def page(mainframe: tk.Frame):

    mainframe.children['loginframe'].forget()

    user_page_frame = tk.Frame(
        mainframe,
        name='userpage',
        width=window_width,
        height=window_height
    )

    user_page_frame.pack(fill='both', expand=1)

    user_page_header_frame = tk.Frame(
        user_page_frame,
        name='header_frame',
        padx = 70,
        highlightthickness=3,
        highlightbackground='black'
    )
    
    user_page_header_frame.pack(fill='both')
    
    # Menu panel
    user_page_content_frame_left = tk.Frame(
        user_page_frame,
        name='menu_content_frame',
        width=50
    )
    func_label = tk.Label(
        user_page_content_frame_left,
        text='MENU',
        font=('Verdana',18,'bold')
    )
    
    create_list_button = tk.Button(
        user_page_content_frame_left,
        text='Tạo danh sách',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    format_list_button = tk.Button(
        user_page_content_frame_left,
        text='Định dạng danh sách',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    pass_list_button = tk.Button(
        user_page_content_frame_left,
        text='Mật khẩu danh sách',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    open_list_button = tk.Button(
        user_page_content_frame_left,
        text='Xem danh sách',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    import_button = tk.Button(
        user_page_content_frame_left,
        text='Thêm đối tượng',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    dele_button = tk.Button(
        user_page_content_frame_left,
        text='Xóa đối tượng',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    recover_button = tk.Button(
        user_page_content_frame_left,
        text='Khôi phục đối tượng đã xóa',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    edit_button = tk.Button(
        user_page_content_frame_left,
        text='Sửa đối tượng',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    about_button = tk.Button(
        user_page_content_frame_left,
        text='Thông tin ứng dụng',
        width=25, bg='#ffffff', activebackground='#00ff00'
    )
    
    user_page_content_frame_left.pack(fill='both',side = 'left', padx=20, pady=10)

    func_label.grid(row=0, column=0, columnspan=3)
    create_list_button.grid(row=1, column=0, pady=5)
    format_list_button.grid(row=2, column=0, pady=5)
    pass_list_button.grid(row=3, column=0, pady=5)
    open_list_button.grid(row=4, column=0, pady=5)
    import_button.grid(row=5, column=0, pady=5)
    dele_button.grid(row=6, column=0, pady=5)
    recover_button.grid(row=7, column=0, pady=5)
    edit_button.grid(row=8, column=0, pady=5)
    about_button.grid(row=9, column=0, pady=5)
    
    # Content panel
    
    user_page_content_frame_right = tk.Frame(
        user_page_frame,
        name='content_frame',
        highlightthickness=2,
        bg='white',
        highlightbackground='black',
        width=360,
        height=290
    )
    user_page_content_frame_right.pack(pady=10, side='left', ipady=40)
    user_page_content_frame_right.grid_propagate(False)
    user_page_content_frame_right.pack_propagate(False)
    mess = '''
        ĐỒ ÁN CUỐI KỲ - An toàn và phục hồi dữ liệu - 20_22
        
        SINH VIÊN THỰC HIỆN:
        1. Bùi Nguyên Nghĩa - 19120600@student.hcmus.edu.vn
        2. Trà Như Khuyên - 20120310@student.hcmus.edu.vn
        
        GIẢNG VIÊN HƯỚNG DẪN:
        Thầy Thái Hùng Văn - thvan@fit.hcmus.edu.vn
        '''
    welcome_label = tk.Label(
            user_page_content_frame_right,
            text='Welcome!',
            bg='white',
            font=('Arial', 55)
        )
    welcome_label.grid(row=0, column=0, pady=5, sticky='w')
    welcome_label.place(x=175, y=150, anchor="center")
    
    def create_list():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        address_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )

        address_frame.pack(side='left', fill='both')
        address_frame.grid_propagate(False)
        
        address_choose_label = tk.Label(
            address_frame,
            text='Chọn vị trí: ',
            font=('Verdana',8),
        )
        address_display = tk.Label(
            address_frame,
            wraplength=150,
            bg='white'
        )
        addr = tk.StringVar(address_frame)
        def get_address():
            get_address = filedialog.askdirectory(
                title='Chọn vị trí',
                initialdir=user_dir
            )
            addr.set(get_address)
            address_display['textvariable']=addr

        file_choose_button = tk.Button(
            address_frame,
            text='Chọn vị trí',
            command=get_address,
            anchor='w'
        )

        name_function_label = tk.Label(
            address_frame,
            text='TẠO danh sách',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        address_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        file_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        address_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')

        user_frame = tk.Frame(
            user_page_content_frame_right,
            name='user_pick_frame',
            bg='white',
            width=190,
            height=290
        )

        user_frame.pack(side='left')
        user_frame.grid_propagate(False)

        
        setname_label = tk.Label(
            user_frame,
            text='Đặt tên:',
            font=('Verdana',8)
        )
        setname_entry = tk.Entry(
            user_frame,
            width=25,
            font=('Verdana',8)
        )

        setsize_label = tk.Label(
            user_frame,
            text='Chọn kích thước (MB):',
            font=('Verdana',8)
        )
        n = tk.StringVar()
        size_menu = TTK.Combobox(user_frame, width = 27,  textvariable = n) 
        size_menu['values'] = ('5', '10', '50','100', '500', '1000', '2000') 
        
        size_menu.grid(column = 1, row = 15) 
    
        size_menu.current(0)  
        
        def submit():
            name = setname_entry.get().strip()
            size = int(size_menu.get().strip())
            if create_arrays(addr.get(), name, size):
                messagebox.showinfo(title='CHÚC MỪNG', message='Tạo list thành công')
            else: messagebox.showerror(title='LỖI', message='Tạo list không thành công')
        submit_button = tk.Button(
            user_frame,
            text='Xác nhận',
            width=10,
            command=submit
        )
        
        
        setname_label.grid(row=0, column=0, pady=5)
        setname_entry.grid(row=1, column=0, pady=5)
        setsize_label.grid(row=3, column=0, pady=5)
        size_menu.grid(row=4, column=0, pady=5)
        submit_button.grid(row=5,column=0, pady=5)

    def format_list():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        list_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )

        user_frame = tk.Frame(
                user_page_content_frame_right,
                name='user_pick_frame',
                bg='white',
                width=190,
                height=290
            )

        list_frame.pack(side='left', fill='both')
        list_frame.grid_propagate(False)

        list_choose_label = tk.Label(
            list_frame,
            text='Chọn list: ',
            font=('Verdana',8),
        )
        list_display = tk.Label(
            list_frame,
            wraplength=150,
            bg='white'
        )
        list = tk.StringVar(list_frame)
        
        def get_list():
            get_list = filedialog.askopenfilename(
                title='Chọn list',
                initialdir=user_dir
            )
            list.set(get_list)
            list_display['textvariable']=list

        file_choose_button = tk.Button(
            list_frame,
            text='Chọn list',
            command=get_list,
            anchor='w'
        )

        pass_label = tk.Label(
            list_frame,
            text='Nhập mật khẩu:',
            font=('Verdana',8)
        )
        pass_entry = tk.Entry(
            list_frame,
            width=10,
            font=('Verdana',8), show='*'
        )
        checkpass_button = tk.Button(
            list_frame,
            text='Kiểm tra',
            anchor='w'
        )
        name_function_label = tk.Label(
            list_frame,
            text='ĐỊNH DẠNG danh sách',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        list_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        file_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        list_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')
        pass_label.grid(row=4, column=0, pady=5, sticky='w')
        pass_entry.grid(row=5, column=0, pady=5, sticky='w')
        checkpass_button.grid(row=6, column=0, pady=5, sticky='w')
        
        def showright():
            user_frame.pack(side='left')
            user_frame.grid_propagate(False)

            setname_label = tk.Label(
                user_frame,
                text='Đặt tên:',
                font=('Verdana',8)
            )
            setname_entry = tk.Entry(
                user_frame,
                width=25,
                font=('Verdana',8)
            )

            def submit():
                name = setname_entry.get().strip()
                if format_arrays(list.get(), name):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Định dạng list thành công')
                else: messagebox.showerror(title='LỖI', message='Định dạng list không thành công')
            submit_button = tk.Button(
                user_frame,
                text='Xác nhận',
                width=10,
                command=submit
            )
            setname_label.grid(row=0, column=0, pady=5)
            setname_entry.grid(row=1, column=0, pady=5)
            submit_button.grid(row=5,column=0, pady=5) 
        
        def check():
            pw = pass_entry.get().strip()
            arrays = list.get()
            check = hash_password(pw, int(salt_len))
            isPass = b'\x00'
            with open(arrays, 'rb') as fileList:
                default_data = fileList.read()
                fileList.seek(20)
                isPass = fileList.read(1)
                fileList.seek(21)
                passhase = fileList.read(len(check))
                pass_hashed = passhase[:len(check)].decode()
            if (isPass != b'\x00'):
                if validate_password(pw, pass_hashed, int(salt_len)):    
                    showright()
                    checkpass_button.grid_remove()
                else: messagebox.showerror(title='LỖI', message='Mật khẩu sai!')
            else:
                showright()
                checkpass_button.grid_remove()
                pass_label.grid_remove()
                pass_entry.grid_remove()
        checkpass_button['command'] = check
        
    def pass_list():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        list_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )

        list_frame.pack(side='left', fill='both')
        list_frame.grid_propagate(False)

        list_choose_label = tk.Label(
            list_frame,
            text='Chọn list: ',
            font=('Verdana',8),
        )
        list_display = tk.Label(
            list_frame,
            wraplength=150,
            bg='white'
        )
        list = tk.StringVar(list_frame)
        def get_list():
            get_list = filedialog.askopenfilename(
                title='Chọn list',
                initialdir=user_dir
            )
            list.set(get_list)
            list_display['textvariable']=list

        file_choose_button = tk.Button(
            list_frame,
            text='Chọn list',
            command=get_list,
            anchor='w'
        )

        name_function_label = tk.Label(
            list_frame,
            text='ĐẶT mật khẩu',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        list_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        file_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        list_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')

        user_frame = tk.Frame(
            user_page_content_frame_right,
            name='user_pick_frame',
            bg='white',
            width=190,
            height=290
        )

        user_frame.pack(side='left')
        user_frame.grid_propagate(False)

        oldpass_label = tk.Label(
            user_frame,
            text='Nhập mật khẩu cũ:',
            font=('Verdana',8)
        )
        oldpass_entry = tk.Entry(
            user_frame,
            width=25,
            font=('Verdana',8),  show='*'
        )

        setpass_label = tk.Label(
            user_frame,
            text='Nhập mật khẩu mới:',
            font=('Verdana',8)
        )
        setpass_entry = tk.Entry(
            user_frame,
            width=25,
            font=('Verdana',8),  show='*'
        )

        def submit():
            oldpw = oldpass_entry.get().strip()
            newpw = setpass_entry.get().strip()
            
            if setpass_arrays(list.get(), oldpw, newpw):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Đặt mật khẩu list thành công')
            else: messagebox.showerror(title='LỖI', message='Đặt mật khẩu list không thành công')
           
        submit_button = tk.Button(
            user_frame,
            text='Xác nhận',
            width=10,
            command=submit
        )

        oldpass_label.grid(row=0, column=0, pady=5)
        oldpass_entry.grid(row=1, column=0, pady=5)
        setpass_label.grid(row=3, column=0, pady=5)
        setpass_entry.grid(row=4, column=0, pady=5)
        submit_button.grid(row=5,column=0, pady=5)
    
    def open_list():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        list_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )

        list_frame.pack(side='left', fill='both')
        list_frame.grid_propagate(False)

        list_choose_label = tk.Label(
            list_frame,
            text='Chọn list: ',
            font=('Verdana',8),
        )
        list_display = tk.Label(
            list_frame,
            wraplength=150,
            bg='white'
        )
        list = tk.StringVar(list_frame)
        def get_list():
            get_list = filedialog.askopenfilename(
                title='Chọn list',
                initialdir=user_dir
            )
            list.set(get_list)
            list_display['textvariable']=list

        list_choose_button = tk.Button(
            list_frame,
            text='Chọn list',
            command=get_list,
            anchor='w'
        )
        
        name_function_label = tk.Label(
            list_frame,
            text='LIỆT KÊ danh sách',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        list_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        list_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        list_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')

        user_frame = tk.Frame(
            user_page_content_frame_right,
            name='user_pick_frame',
            bg='white',
            width=190,
            height=290
        )

        user_frame.pack(side='left')
        user_frame.grid_propagate(False)

        pass_label = tk.Label(
            user_frame,
            text='Nhập mật khẩu:',
            font=('Verdana',8)
        )
        pass_entry = tk.Entry(
            user_frame,
            width=25,
            font=('Verdana',8), show='*'
        )
        
        radio = tk.IntVar()
        r1 = tk.Radiobutton(user_frame, text="Hiện", variable=radio, value=1)
        r2 = tk.Radiobutton(user_frame, text="Ẩn", variable=radio, value=0)
        
        
        

        def submit():
            pw = pass_entry.get().strip()
            arrays = list.get()
            check = hash_password(pw, int(salt_len))
            isPass = b'\x00'
            with open(arrays, 'rb') as fileList:
                fileList.seek(20)
                isPass = fileList.read(1)
                fileList.seek(21)
                passhase = fileList.read(len(check))
                pass_hashed = passhase[:len(check)].decode()
            if ((isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len))) or isPass == b'\x00'):   
                    listfile = open_arrays(list.get())

                    timec_label = tk.Label(
                        user_frame,
                        text='Giờ tạo:',
                        font=('Verdana',8)
                    )
                    timeu_label = tk.Label(
                        user_frame,
                        text='Giờ cập nhật:',
                        font=('Verdana',8)
                    )
                    stimec_label = tk.Label(
                                    user_frame,
                                    text=listfile[6][0] + ', ' + listfile[6][1],
                                    font=('Verdana',8)
                                )
                    stimeu_label = tk.Label(
                                    user_frame,
                                    text=listfile[6][2] + ', ' + listfile[6][3],
                                    font=('Verdana',8)
                                )
                    timec_label.grid(row=5,column=0, pady=5)
                    stimec_label.grid(row=6,column=0, pady=5)
                    timeu_label.grid(row=7,column=0, pady=5)
                    stimeu_label.grid(row=8,column=0, pady=5)
                    winTeacher = tk.Tk()
                    winTeacher.title('DANH SÁCH GIÁO VIÊN/GIẢNG VIÊN')
                    tree0 = TTK.Treeview(winTeacher, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=5)
                    def setTree(tree):
                        tree.column("# 1", anchor=tk.CENTER); tree.heading("# 1", text="Mã số")
                        tree.column("# 2", anchor=tk.CENTER); tree.heading("# 2", text="Họ tên")
                        tree.column("# 3", anchor=tk.CENTER); tree.heading("# 3", text="Ngày sinh")
                        tree.column("# 4", anchor=tk.CENTER); tree.heading("# 4", text="Ngày tham gia")
                        tree.column("# 5", anchor=tk.CENTER); tree.heading("# 5", text="SĐT")
                        tree.column("# 6", anchor=tk.CENTER); tree.heading("# 6", text="CCCD")
                        return tree
                    def hidedata(tree, listfile, k):
                        for i in listfile[k]:
                            if i.getActive() == 1:
                                t = ()
                                t = t + (i.getId(),) + (i.getName(),) + (i.getDob(),) + (i.getDop(),)
                                t = t + (re.sub(r'\d', '*', i.getPhone()),) + (re.sub(r'\d', '*', i.getCccd()),) 
                                tree.insert('', 'end', values=t)
                        return tree
                    def showdata(tree, listfile, k):
                        for i in listfile[k]:
                            if i.getActive() == 1:
                                t = ()
                                t = t + (i.getId(),) + (i.getName(),) + (i.getDob(),) + (i.getDop(),)
                                t = t + (i.getPhone(),) + (i.getCccd(),) 
                                tree.insert('', 'end', values=t)
                        return tree
                    
                    winStudent = tk.Tk()
                    winStudent.title('DANH SÁCH HỌC SINH/SINH VIÊN')
                    tree1 = TTK.Treeview(winStudent, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=5)
                    if (radio.get() == 0):
                        hidedata(setTree(tree0), listfile, 2).pack()
                        hidedata(setTree(tree1), listfile, 5).pack()
                    else:
                        showdata(setTree(tree0), listfile, 2).pack()
                        showdata(setTree(tree1), listfile, 5).pack()
            if (isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len)) == False):
                messagebox.showerror(title='LỖI', message='Mật khẩu sai!')
        submit_button = tk.Button(
            user_frame,
            text='Danh sách các đối tượng',
            width=20,
            command=submit
        )

        pass_label.grid(row=0, column=0, pady=5)
        pass_entry.grid(row=1, column=0, pady=5)
        r1.grid(row=2,column=0, pady=5)
        r2.grid(row=3,column=0, pady=5)
        submit_button.grid(row=4,column=0, pady=5)
    
    def import_obj():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        list_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )

        list_frame.pack(side='left', fill='both')
        list_frame.grid_propagate(False)

        list_choose_label = tk.Label(
            list_frame,
            text='Chọn list: ',
            font=('Verdana',8),
        )
        list_display = tk.Label(
            list_frame,
            wraplength=150,
            bg='white'
        )
        list = tk.StringVar(list_frame)
        def get_list():
            get_list = filedialog.askopenfilename(
                title='Chọn list',
                initialdir=user_dir
            )
            list.set(get_list)
            list_display['textvariable']=list
        
        list_choose_button = tk.Button(
            list_frame,
            text='Chọn list',
            command=get_list,
            anchor='w'
        )

        pass_label = tk.Label(
            list_frame,
            text='Nhập mật khẩu:',
            font=('Verdana',8)
        )
        pass_entry = tk.Entry(
            list_frame,
            width=10,
            font=('Verdana',8), show='*'
        )
        checkpass_button = tk.Button(
            list_frame,
            text='Kiểm tra',
            anchor='w'
        )

        name_function_label = tk.Label(
            list_frame,
            text='THÊM đối tượng',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        list_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        list_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        list_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')
        pass_label.grid(row=4, column=0, pady=5, sticky='w')
        pass_entry.grid(row=5, column=0, pady=5, sticky='w')
        checkpass_button.grid(row=6, column=0, pady=5, sticky='w')
        
        def showright():
            newWindow = tk.Toplevel(mainframe)
            newWindow.title("Nhập thông tin")
            newWindow.geometry("400x400")
            newWindow.resizable(False, False)
    
            infor_label = tk.Label(
                newWindow,
                text='Nhập thông tin cá nhân: ',
                font=('Verdana',8),
            )
            
            radio = tk.IntVar()
            r1 = tk.Radiobutton(newWindow, text="Học sinh/sinh viên", variable=radio, value=1)
            r2 = tk.Radiobutton(newWindow, text="Giáo viên/giảng viên", variable=radio, value=0)

            inputid_label = tk.Label(
                newWindow,
                text='Nhập mã số:',
                font=('Verdana',8)
                )
            inputid_entry = tk.Entry(
                newWindow,
                width=25,
                font=('Verdana',8)
            )
            inputname_label = tk.Label(
                newWindow,
                text='Nhập họ và tên:',
                font=('Verdana',8)
                )
            inputname_entry = tk.Entry(
                newWindow,
                width=25,
                font=('Verdana',8)
            )
            inputdob_label = tk.Label(
                newWindow,
                text='Nhập ngày sinh:',
                font=('Verdana',8)
                )
            caldob = DateEntry(newWindow, date_pattern="yyyy-mm-dd", year = 2000, month = 1, day = 1)
            inputdop_label = tk.Label(
                newWindow,
                text='Nhập ngày tham gia:',
                font=('Verdana',8)
                )
            caldop = DateEntry(newWindow, date_pattern="yyyy-mm-dd", year = 2018, month = 1, day = 1)
            inputphone_label = tk.Label(
                newWindow,
                text='Nhập số điện thoại:',
                font=('Verdana',8)
                )
            inputphone_entry = tk.Entry(
                newWindow,
                width=25,
                font=('Verdana',8)
            )
            inputcccd_label = tk.Label(
                newWindow,
                text='Nhập số CCCD:',
                font=('Verdana',8)
                )
            inputcccd_entry = tk.Entry(
                newWindow,
                width=25,
                font=('Verdana',8)
            )
            
            infor_label.grid(row=1, column=0, pady=5, sticky='w')
            r1.grid(row=2,column=0, pady=5)
            r2.grid(row=2,column=1, pady=5)
            inputid_label.grid(row=3,column=0, pady=5)
            inputid_entry.grid(row=3,column=1, pady=5)
            inputname_label.grid(row=4,column=0, pady=5)
            inputname_entry.grid(row=4,column=1, pady=5)
            inputdob_label.grid(row=5,column=0, pady=5)
            caldob.grid(row=5,column=1, pady=5)
            inputdop_label.grid(row=6,column=0, pady=5)
            caldop.grid(row=6,column=1, pady=5)
            inputphone_label.grid(row=7,column=0, pady=5)
            inputphone_entry.grid(row=7,column=1, pady=5)
            inputcccd_label.grid(row=8,column=0, pady=5)
            inputcccd_entry.grid(row=8,column=1, pady=5)
            
            def submit():
                if (radio.get() == 1):
                    isStudent = 1
                else:
                    isStudent = 0
                obj = Obj(isStudent,
                        inputid_entry.get().strip(), 
                        inputname_entry.get().strip(), 
                        caldob.get_date(),
                        caldop.get_date(),
                        inputphone_entry.get().strip(), 
                        inputcccd_entry.get().strip(),
                        1)
                if import_obj_in(list.get(), obj):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Nhập đối tượng vào thành công')
                    newWindow.destroy()
                else: messagebox.showerror(title='LỖI', message='Nhập đối tượng vào không thành công')
            submit_button = tk.Button(
                    newWindow,
                    text='Hoàn tất',
                    width=10,
                    command=submit
                )
            submit_button.grid(row=9,column=1, pady=5)

        def check():
                pw = pass_entry.get().strip()
                arrays = list.get()
                check = hash_password(pw, int(salt_len))
                isPass = b'\x00'
                with open(arrays, 'rb') as fileList:
                    fileList.seek(20)
                    isPass = fileList.read(1)
                    fileList.seek(21)
                    passhase = fileList.read(len(check))
                    pass_hashed = passhase[:len(check)].decode()
                
                if ((isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len))) or isPass == b'\x00'):   
                    showright()
                    checkpass_button.grid_remove()
                    pass_label.grid_remove()
                    pass_entry.grid_remove()
                if (isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len)) == False):
                    messagebox.showerror(title='LỖI', message='Mật khẩu sai!')
                
        checkpass_button['command'] = check

    def delete_obj():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        list_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )
        user_frame = tk.Frame(
                user_page_content_frame_right,
                name='user_pick_frame',
                bg='white',
                width=190,
                height=290
            )
        list_frame.pack(side='left', fill='both')
        list_frame.grid_propagate(False)
        radio = tk.IntVar()
        r1 = tk.Radiobutton(list_frame, text="Học sinh/sinh viên", variable=radio, value=1)
        r2 = tk.Radiobutton(list_frame, text="Giáo viên/giảng viên", variable=radio, value=0)
        list_choose_label = tk.Label(
            list_frame,
            text='Chọn list: ',
            font=('Verdana',8),
        )
        list_display = tk.Label(
            list_frame,
            wraplength=150,
            bg='white'
        )
        list = tk.StringVar(list_frame)
        def get_list():
            get_list = filedialog.askopenfilename(
                title='Chọn list',
                initialdir=user_dir
            )
            list.set(get_list)
            list_display['textvariable']=list

        list_choose_button = tk.Button(
            list_frame,
            text='Chọn list',
            command=get_list,
            anchor='w'
        )

        pass_label = tk.Label(
            list_frame,
            text='Nhập mật khẩu:',
            font=('Verdana',8)
        )
        pass_entry = tk.Entry(
            list_frame,
            width=10,
            font=('Verdana',8), show='*'
        )
        find_file_button = tk.Button(
                list_frame,
                text='Danh sách các đối tượng',
                width=20
            )

        name_function_label = tk.Label(
            list_frame,
            text='XÓA đối tượng',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        list_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        list_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        list_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')
        pass_label.grid(row=4, column=0, pady=5, sticky='w')
        pass_entry.grid(row=5, column=0, pady=5, sticky='w')
        r1.grid(row=6,column=0, pady=5)
        r2.grid(row=7,column=0, pady=5)
        find_file_button.grid(row=8,column=0, pady=5)

        def showright():
            user_frame.pack(side='left')
            user_frame.grid_propagate(False)
            
            type_label = tk.Label(
                user_frame,
                text='Nhập mã số cần xóa:',
                font=('Verdana',8)
            )
            type_entry = tk.Entry(
                user_frame,
                width=25,
                font=('Verdana',8)
            )
            
            def submit():
                id = type_entry.get().strip()
                if deleObj(list.get(), id, radio.get()):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Xóa đối tượng thành công')
                else: messagebox.showerror(title='LỖI', message='Xóa đối tượng  không thành công')
            submit_button = tk.Button(
                user_frame,
                text='Xóa',
                width=10,
                command=submit
            )
            type_label.grid(row=0,column=0, pady=5)
            type_entry.grid(row=1,column=0, pady=5)
            submit_button.grid(row=4,column=0, pady=5)
        
        def find_obj():
            pw = pass_entry.get().strip()
            vol = list.get()
            check = hash_password(pw, int(salt_len))
            isPass = b'\x00'
            with open(vol, 'rb') as fileVol:
                fileVol.seek(20)
                isPass = fileVol.read(1)
                fileVol.seek(21)
                passhase = fileVol.read(len(check))
                pass_hashed = passhase[:len(check)].decode()

            if ((isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len))) or isPass == b'\x00'):   
                        namefiles=[]
                        listfile =  open_arrays(list.get())
                        if (radio.get() == 1):
                            s = 5
                            r2.grid_remove()
                        else:
                            s = 2
                            r1.grid_remove()
                        for i in listfile[s]:
                            if i.getActive():
                                namefiles.append(i.getId())
                        var = tk.Variable(value=namefiles)

                        listbox = tk.Listbox(
                            list_frame,
                            listvariable=var,
                            height=6,
                            selectmode=tk.EXTENDED
                        )
                        showright()
                        find_file_button.grid_remove()
                        pass_label.grid_remove()
                        pass_entry.grid_remove()
                        listbox.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
                        listbox.grid(row=4, column=0, pady=5)

            if (isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len)) == False):
                        messagebox.showerror(title='LỖI', message='Mật khẩu sai!')

        find_file_button['command']=find_obj 
    
    def recover_obj():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        list_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )
        user_frame = tk.Frame(
                user_page_content_frame_right,
                name='user_pick_frame',
                bg='white',
                width=190,
                height=290
            )
        list_frame.pack(side='left', fill='both')
        list_frame.grid_propagate(False)
        radio = tk.IntVar()
        r1 = tk.Radiobutton(list_frame, text="Học sinh/sinh viên", variable=radio, value=1)
        r2 = tk.Radiobutton(list_frame, text="Giáo viên/giảng viên", variable=radio, value=0)
        list_choose_label = tk.Label(
            list_frame,
            text='Chọn list: ',
            font=('Verdana',8),
        )
        list_display = tk.Label(
            list_frame,
            wraplength=150,
            bg='white'
        )
        list = tk.StringVar(list_frame)
        def get_list():
            get_list = filedialog.askopenfilename(
                title='Chọn list',
                initialdir=user_dir
            )
            list.set(get_list)
            list_display['textvariable']=list

        list_choose_button = tk.Button(
            list_frame,
            text='Chọn list',
            command=get_list,
            anchor='w'
        )

        pass_label = tk.Label(
            list_frame,
            text='Nhập mật khẩu:',
            font=('Verdana',8)
        )
        pass_entry = tk.Entry(
            list_frame,
            width=10,
            font=('Verdana',8), show='*'
        )
        find_file_button = tk.Button(
                list_frame,
                text='Danh sách các đối tượng',
                width=20
            )

        name_function_label = tk.Label(
            list_frame,
            text='KHÔI PHỤC đối tượng',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        list_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        list_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        list_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')
        pass_label.grid(row=4, column=0, pady=5, sticky='w')
        pass_entry.grid(row=5, column=0, pady=5, sticky='w')
        r1.grid(row=6,column=0, pady=5)
        r2.grid(row=7,column=0, pady=5)
        find_file_button.grid(row=8,column=0, pady=5)

        def showright():
            user_frame.pack(side='left')
            user_frame.grid_propagate(False)
            
            type_label = tk.Label(
                user_frame,
                text='Nhập mã số cần khôi phục:',
                font=('Verdana',8)
            )
            type_entry = tk.Entry(
                user_frame,
                width=25,
                font=('Verdana',8)
            )
            
            def submit():
                id = type_entry.get().strip()
                if recoverObj(list.get(), id, radio.get()):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Khôi phục đối tượng thành công')
                else: messagebox.showerror(title='LỖI', message='Khôi phục đối tượng  không thành công')
            submit_button = tk.Button(
                user_frame,
                text='Khôi phục',
                width=10,
                command=submit
            )
            type_label.grid(row=0,column=0, pady=5)
            type_entry.grid(row=1,column=0, pady=5)
            submit_button.grid(row=4,column=0, pady=5)
        
        def find_obj():
            pw = pass_entry.get().strip()
            vol = list.get()
            check = hash_password(pw, int(salt_len))
            isPass = b'\x00'
            with open(vol, 'rb') as fileVol:
                fileVol.seek(20)
                isPass = fileVol.read(1)
                fileVol.seek(21)
                passhase = fileVol.read(len(check))
                pass_hashed = passhase[:len(check)].decode()

            if ((isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len))) or isPass == b'\x00'):   
                        namefiles=[]
                        listfile =  open_arrays(list.get())
                        if (radio.get() == 1):
                            s = 5
                            r2.grid_remove()
                        else:
                            s = 2
                            r1.grid_remove()
                        for i in listfile[s]:
                            if i.getActive() == 0:
                                namefiles.append(i.getId())
                        var = tk.Variable(value=namefiles)

                        listbox = tk.Listbox(
                            list_frame,
                            listvariable=var,
                            height=6,
                            selectmode=tk.EXTENDED
                        )
                        showright()
                        find_file_button.grid_remove()
                        pass_label.grid_remove()
                        pass_entry.grid_remove()
                        listbox.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
                        listbox.grid(row=4, column=0, pady=5)

            if (isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len)) == False):
                        messagebox.showerror(title='LỖI', message='Mật khẩu sai!')

        find_file_button['command']=find_obj    

    def edit_obj():
        user_dir = 'data/' 

        forget_old_widgets(user_page_content_frame_right)

        list_frame = tk.Frame(
            user_page_content_frame_right,
            name='address_pick_frame',
            bg='white',
            width=170,
            height=290
        )
        user_frame = tk.Frame(
                user_page_content_frame_right,
                name='user_pick_frame',
                bg='white',
                width=190,
                height=290
            )
        list_frame.pack(side='left', fill='both')
        list_frame.grid_propagate(False)
        radio = tk.IntVar()
        r1 = tk.Radiobutton(list_frame, text="Học sinh/sinh viên", variable=radio, value=1)
        r2 = tk.Radiobutton(list_frame, text="Giáo viên/giảng viên", variable=radio, value=0)
        list_choose_label = tk.Label(
            list_frame,
            text='Chọn list: ',
            font=('Verdana',8),
        )
        list_display = tk.Label(
            list_frame,
            wraplength=150,
            bg='white'
        )
        list = tk.StringVar(list_frame)
        def get_list():
            get_list = filedialog.askopenfilename(
                title='Chọn list',
                initialdir=user_dir
            )
            list.set(get_list)
            list_display['textvariable']=list

        list_choose_button = tk.Button(
            list_frame,
            text='Chọn list',
            command=get_list,
            anchor='w'
        )

        pass_label = tk.Label(
            list_frame,
            text='Nhập mật khẩu:',
            font=('Verdana',8)
        )
        pass_entry = tk.Entry(
            list_frame,
            width=10,
            font=('Verdana',8), show='*'
        )
        find_file_button = tk.Button(
                list_frame,
                text='Danh sách các đối tượng',
                width=20
            )

        name_function_label = tk.Label(
            list_frame,
            text='SỬA đối tượng',
            font=('Verdana',8, 'bold'),
            bg='yellow'
        )
        name_function_label.grid(row=0, column=0, pady=5, sticky='w')
        list_choose_label.grid(row=1, column=0, pady=5, sticky='w')
        list_choose_button.grid(row=2, column=0, pady=5, sticky='w')
        list_display.grid(row=3, column=0, columnspan=1, pady=5, sticky='w')
        pass_label.grid(row=4, column=0, pady=5, sticky='w')
        pass_entry.grid(row=5, column=0, pady=5, sticky='w')
        r1.grid(row=6,column=0, pady=5)
        r2.grid(row=7,column=0, pady=5)
        find_file_button.grid(row=8,column=0, pady=5)



        def showright():
            user_frame.pack(side='left')
            user_frame.grid_propagate(False)
            
            type_label = tk.Label(
                user_frame,
                text='Nhập mã số cần sửa:',
                font=('Verdana',8)
            )
            type_entry = tk.Entry(
                user_frame,
                width=25,
                font=('Verdana',8)
            )

            def in4():
                id = type_entry.get().strip()
                mytuple = open_arrays(list.get())
                if radio.get():
                    k = 3
                else:
                    k = 0
                j = 0
                for i in mytuple[k+2]:
                    if i.getId() == id:
                        obj = i
                        break
                    j = j + 1 

                global newdata
                newdata = obj
                showEdit(obj)
                
            in4_button = tk.Button(
                user_frame,
                text='Xem',
                width=10,
                command=in4
            )
            type_label.grid(row=0,column=0, pady=5)
            type_entry.grid(row=1,column=0, pady=5)
            in4_button.grid(row=4,column=0, pady=5)

        def showEdit(obj):
            newWindow = tk.Toplevel(mainframe)
            newWindow.title("Nhập thông tin")
            newWindow.geometry("400x400")
            newWindow.resizable(False, False)
    
            infor_label = tk.Label(
                newWindow,
                text='Nhập thông tin cá nhân: ',
                font=('Verdana',8),
            )
            
            text1 = tk.StringVar(); text1.set(obj.getId()); oldid = obj.getId()
            text2 = tk.StringVar(); text2.set(obj.getName())
            text3 = tk.StringVar(); text3.set(obj.getPhone()) 
            text4 = tk.StringVar(); text4.set(obj.getCccd()) 

            inputid_label = tk.Label(
                newWindow,
                text='Nhập mã số:',
                font=('Verdana',8)
                )
            inputid_entry = tk.Entry(
                newWindow,
                width=25,
                textvariable = text1,
                font=('Verdana',8)
            )
            inputname_label = tk.Label(
                newWindow,
                text='Nhập họ và tên:',
                font=('Verdana',8)
                )
            inputname_entry = tk.Entry(
                newWindow,
                width=25,
                textvariable = text2,
                font=('Verdana',8)
            )
            inputdob_label = tk.Label(
                newWindow,
                text='Nhập ngày sinh:',
                font=('Verdana',8)
                )
            
            date = obj.getDob().split('-')
            year = date[0]
            day = date[2]
            if len(date[2]) == 4:
                year = date[2]
                day = date[0]
            month = date[1]
            caldob = DateEntry(newWindow, date_pattern="yyyy-mm-dd", 
                               year = int(year), 
                               month = int(month), 
                               day = int(day))
            inputdop_label = tk.Label(
                newWindow,
                text='Nhập ngày tham gia:',
                font=('Verdana',8)
                )
            date = obj.getDop().split('-')
            year = date[0]
            day = date[2]
            if len(date[2]) == 4:
                year = date[2]
                day = date[0]
            month = date[1]
            caldop = DateEntry(newWindow, date_pattern="yyyy-mm-dd", 
                               year = int(year), 
                               month = int(month), 
                               day = int(day))
            inputphone_label = tk.Label(
                newWindow,
                text='Nhập số điện thoại:',
                font=('Verdana',8)
                )
            inputphone_entry = tk.Entry(
                newWindow,
                width=25,
                textvariable = text3,
                font=('Verdana',8)
            )
            inputcccd_label = tk.Label(
                newWindow,
                text='Nhập số CCCD:',
                font=('Verdana',8)
                )
            inputcccd_entry = tk.Entry(
                newWindow,
                width=25,
                textvariable = text4,
                font=('Verdana',8)
            )
            
            def submit():
                if (radio.get() == 1):
                    isStudent = 1
                else:
                    isStudent = 0
                obj = Obj(isStudent,
                        inputid_entry.get().strip(), 
                        inputname_entry.get().strip(), 
                        caldob.get_date(),
                        caldop.get_date(),
                        inputphone_entry.get().strip(), 
                        inputcccd_entry.get().strip(),
                        1)
                
                mytuple = open_arrays(list.get())
                if isStudent == 1:
                    k = 3
                else:
                    k = 0
                j = 0

                for i in mytuple[k+2]:
                    if str(i.getId()) == str(oldid):
                        break
                    j = j + 1 
                if editObj(list.get(), obj, j):
                    messagebox.showinfo(title='CHÚC MỪNG', message='Sửa đối tượng thành công')
                    newWindow.destroy()
                else: messagebox.showerror(title='LỖI', message='Sửa đối tượng không thành công')
            submit_button = tk.Button(
                    newWindow,
                    text='Hoàn tất',
                    width=10,
                    command=submit
                )
            infor_label.grid(row=1, column=0, pady=5, sticky='w')
            inputid_label.grid(row=3,column=0, pady=5)
            inputid_entry.grid(row=3,column=1, pady=5)
            inputname_label.grid(row=4,column=0, pady=5)
            inputname_entry.grid(row=4,column=1, pady=5)
            inputdob_label.grid(row=5,column=0, pady=5)
            caldob.grid(row=5,column=1, pady=5)
            inputdop_label.grid(row=6,column=0, pady=5)
            caldop.grid(row=6,column=1, pady=5)
            inputphone_label.grid(row=7,column=0, pady=5)
            inputphone_entry.grid(row=7,column=1, pady=5)
            inputcccd_label.grid(row=8,column=0, pady=5)
            inputcccd_entry.grid(row=8,column=1, pady=5)
            submit_button.grid(row=9,column=1, pady=5)
        
        def find_obj():
            pw = pass_entry.get().strip()
            vol = list.get()
            check = hash_password(pw, int(salt_len))
            isPass = b'\x00'
            with open(vol, 'rb') as fileVol:
                fileVol.seek(20)
                isPass = fileVol.read(1)
                fileVol.seek(21)
                passhase = fileVol.read(len(check))
                pass_hashed = passhase[:len(check)].decode()

            if ((isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len))) or isPass == b'\x00'):   
                        namefiles=[]
                        listfile =  open_arrays(list.get())
                        if (radio.get() == 1):
                            s = 5
                            r2.grid_remove()
                        else:
                            s = 2
                            r1.grid_remove()
                        for i in listfile[s]:
                            if i.getActive() == 1:
                                namefiles.append(i.getId())
                        var = tk.Variable(value=namefiles)

                        listbox = tk.Listbox(
                            list_frame,
                            listvariable=var,
                            height=6,
                            selectmode=tk.EXTENDED
                        )
                        showright()
                        find_file_button.grid_remove()
                        pass_label.grid_remove()
                        pass_entry.grid_remove()
                        listbox.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
                        listbox.grid(row=4, column=0, pady=5)

            if (isPass != b'\x00' and validate_password(pw, pass_hashed, int(salt_len)) == False):
                        messagebox.showerror(title='LỖI', message='Mật khẩu sai!')

        find_file_button['command']=find_obj       

    def about():
        messagebox.showinfo(title='Thông tin đồ án', message=mess)

    create_list_button['command']=create_list
    format_list_button['command']=format_list
    open_list_button['command']=open_list
    pass_list_button['command']=pass_list
    import_button['command']=import_obj
    dele_button['command']=delete_obj
    recover_button['command']=recover_obj
    edit_button['command']=edit_obj
    about_button['command']=about
