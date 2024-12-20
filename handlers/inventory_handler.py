def check_inventory(denomination, count):
    inventory = {"10": 50, "20": 30, "100": 20}  # จำนวนเหรียญที่มีในเครื่อง

    if inventory[str(denomination)] < count:
        return False, f"{denomination} บาทไม่เพียงพอ (เหลือ {inventory[str(denomination)]} ชิ้น)"
    return True, "เพียงพอ"
