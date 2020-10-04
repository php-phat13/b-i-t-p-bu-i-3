#   Bài6: 
#   def is_pangram(str, alphabet) đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
#   giải

print("Chuoi pangram")
def is_pangram(str, alphabet):
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
str=input("Nhap chuoi kiem tra: ")
alphabet="ABCDEFGHIKLMNOPQRSTUWXYZ"
if is_pangram(str,alphabet):
    print(f" \"{str}\" True")
else:
    print(f" \"{str}\" False")