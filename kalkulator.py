
angka_1 = float(input("Masukkan Angka 1 = "))
operator = input("operator (+,-,x,:) : ")
angka_2 = float(input("Masukkan Angka 2 = "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "x":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == ":":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("Masukkan angka yang bener dong")