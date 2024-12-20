# main.py
import sys
from PyQt5.QtWidgets import QApplication
from ui.main_screen import MainScreen  # นำเข้าคลาส MainScreen จากไฟล์ main_screen.py

if __name__ == "__main__":
    app = QApplication(sys.argv)  # เริ่มต้นแอพพลิเคชั่น
    window = MainScreen()  # สร้างออบเจ็กต์ของ MainScreen
    window.show()  # แสดงหน้าต่าง
    sys.exit(app.exec_())  # เริ่มต้น loop ของแอพ
