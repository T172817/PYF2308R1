soTien = int(input("Nhap vao so tien chi: "))
tienThanhToan = 0
if soTien >= 150:
    tienThanhToan = soTien - 50
    print(f"So tien thanh toan la: {tienThanhToan} $")
elif soTien >= 100:
    tienThanhToan = soTien - 25
    print(f"So tien thanh toan la: {tienThanhToan} $")
elif soTien >= 75:
    tienThanhToan = soTien - 15
    print(f"So tien thanh toan la: {tienThanhToan} $")
else:
    print(f"So tien thanh toan la: {soTien} $")