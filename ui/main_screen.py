from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpinBox, QDialog, QDialogButtonBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR Money Exchange")  # ตั้งชื่อหน้าต่าง
        self.setGeometry(100, 100, 600, 400)  # ตั้งขนาดหน้าต่าง

        # สร้าง Layout หลัก
        self.main_layout = QVBoxLayout()

        # สร้างส่วนของคำอธิบาย (Label)
        self.title_label = QLabel("Welcome to QR Money Exchange", self)
        self.title_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)

        # ปุ่มเลือกเงิน
        self.denomination_button_10 = QPushButton("10 Baht", self)
        self.denomination_button_20 = QPushButton("20 Baht", self)
        self.denomination_button_100 = QPushButton("100 Baht", self)

        # การตั้งค่าปุ่ม
        self.denomination_button_10.setFixedSize(150, 50)
        self.denomination_button_20.setFixedSize(150, 50)
        self.denomination_button_100.setFixedSize(150, 50)

        # เพิ่มปุ่มเข้า Layout
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.denomination_button_10)
        self.button_layout.addWidget(self.denomination_button_20)
        self.button_layout.addWidget(self.denomination_button_100)

        # เพิ่ม label และ layout ของปุ่มลงใน layout หลัก
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addLayout(self.button_layout)

        # เพิ่มปุ่ม "ถัดไป" สำหรับไปหน้าเลือกจำนวน
        self.next_button = QPushButton("Next", self)
        self.next_button.setFixedSize(150, 50)
        self.main_layout.addWidget(self.next_button, alignment=Qt.AlignCenter)

        # ตั้งค่าของหน้าต่าง
        self.setLayout(self.main_layout)

        # เชื่อมโยงปุ่มกับฟังก์ชัน
        self.denomination_button_10.clicked.connect(self.select_10_baht)
        self.denomination_button_20.clicked.connect(self.select_20_baht)
        self.denomination_button_100.clicked.connect(self.select_100_baht)
        self.next_button.clicked.connect(self.open_quantity_dialog)

    def select_10_baht(self):
        print("Selected 10 Baht")

    def select_20_baht(self):
        print("Selected 20 Baht")

    def select_100_baht(self):
        print("Selected 100 Baht")

    def open_quantity_dialog(self):
        """ฟังก์ชันเปิดหน้าต่างเลือกจำนวน"""
        dialog = QuantityDialog(self)
        dialog.exec_()

class QuantityDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Select Quantity")
        self.setGeometry(200, 200, 300, 150)

        self.quantity_label = QLabel("Select Quantity:", self)
        self.quantity_label.setFont(QFont("Arial", 14))
        self.quantity_label.move(20, 20)

        self.quantity_spinbox = QSpinBox(self)
        self.quantity_spinbox.setMinimum(1)
        self.quantity_spinbox.setMaximum(100)
        self.quantity_spinbox.setValue(1)
        self.quantity_spinbox.move(150, 20)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.buttons.move(90, 80)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

    def get_quantity(self):
        return self.quantity_spinbox.value()

# ในกรณีที่ต้องการเรียกใช้ main
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    window = MainScreen()
    window.show()
    app.exec_()
