#   Bài7: 
#   def create_matrix(n, m) xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j
#   giải

print("--ma-tran--")
def create_matrix(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(i*j,end="\t")
        print()
n=int(input("So hang la: "))
m=int(input("So cot la: "))
create_matrix(n,m)
