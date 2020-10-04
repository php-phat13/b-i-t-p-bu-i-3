#   Bài5: 
#   def count_upper_lower(str) trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
#   giải

print("--dem-chu-so-hoa-va-so-thuong--")
def count_upper_lower(str):
    upper=lower=0
    for i in str:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print(f"So chu hoa: {upper}|So chu thuong: {lower}")
str=input("Nhap chuoi: ")
count_upper_lower(str)

