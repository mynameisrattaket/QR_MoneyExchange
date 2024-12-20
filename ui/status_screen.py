from tkinter import Toplevel, Label, Button

def show_status(parent, status):
    # หน้าต่างใหม่
    status_window = Toplevel(parent)
    status_window.title("สถานะการทำงาน")

    # ข้อความสถานะ
    Label(status_window, text=f"สถานะ: {status}").pack()

    # ปุ่มปิดหน้าจอ
    Button(status_window, text="ปิด", command=status_window.destroy).pack()
