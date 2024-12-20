import qrcode

def generate_qr(amount):
    qr = qrcode.make(f"promptpay://payment?amount={amount}")
    qr.save("assets/qr_code.png")
