from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QStackedWidget, QSizePolicy, QSpacerItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
import qrcode

class MainScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR Money Exchange")
        self.setGeometry(100, 100, 600, 400)

        # ใช้ฟอนต์ปกติในระบบ
        self.default_font = QFont("Segoe UI", 14)  # สำหรับ Windows
        # หากใช้ Mac หรือ Linux สามารถเปลี่ยนชื่อฟอนต์ เช่น "System", "Ubuntu"

        # สร้าง StackedWidget สำหรับจัดการหน้า
        self.pages = QStackedWidget(self)

        # สร้างหน้าแรก
        self.page1 = QWidget()
        self.create_main_page()

        # สร้างหน้าเลือกจำนวน
        self.page2 = QWidget()
        self.create_quantity_page()

        # สร้างหน้าแสดง QR Code
        self.page3 = QWidget()
        self.create_qr_code_page()

        # เพิ่มหน้าใน StackedWidget
        self.pages.addWidget(self.page1)
        self.pages.addWidget(self.page2)
        self.pages.addWidget(self.page3)

        # ตั้ง Layout หลัก
        layout = QVBoxLayout(self)
        layout.addWidget(self.pages)
        self.setLayout(layout)

        # เก็บค่าเงินที่เลือกและจำนวน
        self.selected_denomination = None
        self.selected_quantity = 1

    def create_main_page(self):
        """สร้างหน้าแรก"""
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # คำอธิบาย
        title_label = QLabel("QR Money Exchange", self)
        title_label.setFont(QFont("Segoe UI", 20))
        title_label.setAlignment(Qt.AlignCenter)

        # ปุ่มเลือกเงิน
        denomination_buttons = [
            self.create_button("10 บาท", lambda: self.go_to_quantity_page("10")),
            self.create_button("20 บาท", lambda: self.go_to_quantity_page("20")),
            self.create_button("100 บาท", lambda: self.go_to_quantity_page("100")),
        ]
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)  # เพิ่มระยะห่างระหว่างปุ่ม
        for btn in denomination_buttons:
            button_layout.addWidget(btn)

        # เพิ่ม widget ใน Layout
        layout.addWidget(title_label)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # เพิ่มระยะด้านบน
        layout.addLayout(button_layout)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # เพิ่มระยะด้านล่าง
        self.page1.setLayout(layout)

    def create_quantity_page(self):
        """สร้างหน้าเลือกจำนวน"""
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # คำอธิบาย
        title_label = QLabel("เลือกจำนวนที่ต้องการ", self)
        title_label.setFont(QFont("Segoe UI", 20))
        title_label.setAlignment(Qt.AlignCenter)

        # Layout สำหรับปุ่มเพิ่ม/ลดจำนวน
        quantity_layout = QHBoxLayout()
        self.quantity_label = QLabel("1", self)
        self.quantity_label.setFont(QFont("Segoe UI", 16))
        self.quantity_label.setAlignment(Qt.AlignCenter)
        self.quantity_label.setFixedSize(80, 50)

        decrease_button = self.create_button("-", self.decrease_quantity, button_size=(50, 50))
        increase_button = self.create_button("+", self.increase_quantity, button_size=(50, 50))

        quantity_layout.addWidget(decrease_button)
        quantity_layout.addWidget(self.quantity_label)
        quantity_layout.addWidget(increase_button)

        # ปุ่มยืนยันและกลับ
        action_layout = QHBoxLayout()
        action_layout.setSpacing(20)  # เพิ่มระยะห่างระหว่างปุ่ม
        back_button = self.create_button("ย้อนกลับ", self.go_to_main_page, button_size=(120, 50))
        confirm_button = self.create_button("ยืนยัน", self.go_to_qr_code_page, button_size=(120, 50))

        action_layout.addWidget(back_button)
        action_layout.addWidget(confirm_button)

        # เพิ่ม widget ใน Layout
        layout.addWidget(title_label)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # ระยะด้านบน
        layout.addLayout(quantity_layout)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # ระยะด้านล่าง
        layout.addLayout(action_layout)
        self.page2.setLayout(layout)

    def create_qr_code_page(self):
        """สร้างหน้าแสดง QR Code"""
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # คำอธิบาย
        title_label = QLabel("สเเกน QR Code เพื่อจ่ายเงิน", self)
        title_label.setFont(QFont("Segoe UI", 20))
        title_label.setAlignment(Qt.AlignCenter)

        # Placeholder สำหรับ QR Code
        self.qr_code_label = QLabel(self)
        self.qr_code_label.setAlignment(Qt.AlignCenter)

        # เพิ่ม label สำหรับแสดงจำนวนเงินที่ต้องจ่าย
        self.payment_info_label = QLabel(self)
        self.payment_info_label.setFont(QFont("Segoe UI", 16))
        self.payment_info_label.setAlignment(Qt.AlignCenter)

        # ปุ่มกลับไปหน้าแรก
        back_button = self.create_button("กลับไปยังหน้าแรก", self.go_to_main_page, button_size=(200, 50))

        # เพิ่ม widget ใน Layout
        layout.addWidget(title_label)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # ระยะด้านบน
        layout.addWidget(self.qr_code_label)  # แสดง QR Code
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # ระยะด้านล่าง
        layout.addWidget(self.payment_info_label)  # แสดงจำนวนเงินที่ต้องจ่าย
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # ระยะด้านล่าง
        layout.addWidget(back_button)
        self.page3.setLayout(layout)


    def create_button(self, text, callback, button_size=(135, 60)):
        """สร้างปุ่มพร้อมฟังก์ชัน callback"""
        button = QPushButton(text, self)
        button.setFont(self.default_font)
        button.setFixedSize(*button_size)  # ขนาดปุ่ม
        button.clicked.connect(callback)
        return button

    def go_to_quantity_page(self, denomination):
        """ไปยังหน้าเลือกจำนวน"""
        self.selected_denomination = denomination
        self.selected_quantity = 1
        self.quantity_label.setText(str(self.selected_quantity))
        self.pages.setCurrentWidget(self.page2)

    def go_to_qr_code_page(self):
        """ไปยังหน้าแสดง QR Code"""
        total_amount = int(self.selected_denomination) * self.selected_quantity

        # สร้างข้อความแสดงจำนวนเงินที่ต้องจ่าย
        payment_info = f"จำนวนทั้งหมด: {total_amount} บาท"
        self.payment_info_label.setText(payment_info)  # ตั้งค่าข้อความใหม่

        # สร้าง QR Code
        qr = qrcode.QRCode()
        qr.add_data(f"Pay {total_amount} Baht")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # แปลงภาพ QR Code ให้ใช้ใน QLabel
        img_path = "assets/images/qr_code.png"
        img.save(img_path)
        pixmap = QPixmap(img_path)
        self.qr_code_label.setPixmap(pixmap)

        self.pages.setCurrentWidget(self.page3)


    def decrease_quantity(self):
        """ลดจำนวน"""
        if self.selected_quantity > 1:
            self.selected_quantity -= 1
            self.quantity_label.setText(str(self.selected_quantity))

    def increase_quantity(self):
        """เพิ่มจำนวน"""
        self.selected_quantity += 1
        self.quantity_label.setText(str(self.selected_quantity))

    def go_to_main_page(self):
        """กลับไปยังหน้าแรก"""
        self.pages.setCurrentWidget(self.page1)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainScreen()
    window.show()
    sys.exit(app.exec_())
