#  Bài9: 
#  def change_upper_lower(str) chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
#  giải

print("Chuyen chu hoa thanh chu thuong va nguoc lai")
def change_upper_lower(str):
    str=str.swapcase()
    print(f"Chuoi sau khi chuyen: {str}")
str=input("Nhap chuoi muon chuyen: ")
change_upper_lower(str)