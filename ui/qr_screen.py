from tkinter import Toplevel, Label, Button
from PIL import Image, ImageTk
from handlers.payment_handler import generate_qr
from ui.status_screen import show_status

def show_qr_code(parent, amount):
    # สร้าง QR Code
    generate_qr(amount)

    # หน้าต่างใหม่
    qr_window = Toplevel(parent)
    qr_window.title("QR Code สำหรับชำระเงิน")

    # แสดง QR Code
    img = Image.open("assets/qr_code.png")
    qr_img = ImageTk.PhotoImage(img)
    Label(qr_window, image=qr_img).pack()

    # ปุ่มยืนยันหลังการชำระเงิน
    Button(qr_window, text="ยืนยันการชำระเงิน", command=lambda: show_status(qr_window, "จ่ายเหรียญสำเร็จ!")).pack()

    qr_window.mainloop()
