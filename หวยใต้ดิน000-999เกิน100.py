def is_valid_number(number):
    """เช็กว่าเลขนั้นอยู่ในช่วง 000-999 และเป็นตัวเลข 3 หลัก"""
    return number.isdigit() and 0 <= int(number) <= 999 and len(number) == 3

def main():
    print("📌 ระบบเจ้ามือหวยใต้ดิน (เลข 000 - 999)")
    print("พิมพ์ 'exit' เพื่อออกจากระบบ\n")

    purchases = {}  # เก็บยอดซื้อของแต่ละเลข

    while True:
        number = input("กรอกเลข 3 หลัก (000-999): ").zfill(3)
        if number.lower() == 'exit':
            break
        if not is_valid_number(number):
            print("❌ กรุณากรอกเลข 3 หลัก ระหว่าง 000 ถึง 999 เท่านั้น\n")
            continue

        try:
            amount = float(input(f"กรอกยอดซื้อสำหรับเลข {number}: "))
            if amount <= 0:
                print("❌ กรุณากรอกยอดซื้อที่มากกว่า 0\n")
                continue
        except ValueError:
            print("❌ กรุณากรอกยอดซื้อเป็นตัวเลข\n")
            continue

        # อัปเดตยอดซื้อ
        if number not in purchases:
            purchases[number] = 0
        purchases[number] += amount

        # แจ้งเตือนหากยอดซื้อเลขนี้เกิน 100
        if purchases[number] > 100:
            print(f"⚠️ เตือน: ยอดซื้อเลข {number} รวมเกิน 100 บาทแล้ว ({purchases[number]:.2f} บาท)\n")
        else:
            print(f"✅ รับยอดซื้อเลข {number} แล้ว (รวม {purchases[number]:.2f} บาท)\n")

    # สรุปเมื่อจบ
    print("\n📊 รายงานยอดซื้อทั้งหมด:")
    for number, total in sorted(purchases.items()):
        print(f"เลข {number} : {total:.2f} บาท")

if __name__ == "__main__":
    main()
