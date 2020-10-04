#   Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
#   Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
#   giải

print("Đe quy đem va tra ve so luong chu so le cua so nguyen duong n cho truoc")
i=0
def count_odd(n,i):
    if i==len(n) or n[i].isnumeric==False:
        return 0
    if int(n[i])%2!=0:
        return 1+count_odd(n,i+1)
    else:
        return 0+count_odd(n,i+1)

n=input("Nhap so kiem tra: ")
print(count_odd(n,i))
