#   Bài3: 
#   def is_perfect(n) để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
#   giải

print("--So-hoan-hao--")
def is_perfect(n):
    if(n<=0):
        return False
    if sum(i for i in range(1, n//2+1) if n%i==0)==n:
        return True
    else:
        return False
print("So muon kien tra: ",end="")
n=int(input())
print(f"{n} True ") if is_perfect(n) else print(f"{n} False")
