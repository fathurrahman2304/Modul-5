a = 0
b = 0
harga = 0
print("\n======================================")
print("PROGRAM INI AKAN MENGHITUNG  HARGA TIKET")
print("ENTER -1 TO CALCULATE")
print("======================================")
while b == 0:
    umur = int(input("Masukkan umur: "))
    if umur == -1:
        break
    elif umur <= 2 and umur >= 0:
        print("Tiket gratis")
    elif umur >= 3 and umur <= 12:
        harga += 14
    elif umur >= 65:
        harga += 18
    else:
        harga +=23
jumlah = harga
print(f"Jumlah totalnya adalah: {jumlah} dollar")
while a == 0:
    d = int(input("Silahkan bayar: "))
    total = d - jumlah
    if total <= -1 :
        print("Uang yang anda bayar masih kurang")
    else:
        print(f"Kembalian: {total} dollar")
        break
print("Terima kasih telah menggunakan program saya")
