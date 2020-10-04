#   Bài8: 
#   def body_mass_index(m, h) để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
#   --------------------------------------------------------------------------------------------------------
#   def bmi_information(m, h)
#   để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
#   --------------------------------------------------------------------------------------------------------
#   giải

print("--tinh-toan-chi-so-BMI--")
def body_mass_index(m,h):
    BMI=m/math.pow(h,2)
    return BMI
def bmi_information(m,h):
    bmi=body_mass_index(m,h)
    if bmi > 30:
        print("Beo phi")
    elif bmi >=25:
        print("Thua can")
    elif bmi >=18.5:
        print("Binh thuong")
    else:
        print("Gay")
m=float(input("Nhap can nang: "))
h=float(input("Nhap chieu cao: "))
while m<0 or h<0:
    print("Du lieu khong hop le\n Nhap lai")
    print("Can nang la: ",end="")
    m=float(input())
    print("Chieu cao la: ",end="")
    h=float(input())
bmi_information(m,h)