#  Bài2: 
#  def reverse_string(str) trả lại chuỗi đảo ngược của chuỗi str
#  giải

def reverse_string(str):
    return str[::-1]
str=input("Nhập số nghịch đảo: ")
print(f"Sau khi nghich đao: {reverse_string(str)}")