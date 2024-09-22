batas = 1000000 
bil_prima = []

count = 0  
for num in range(2, batas):
    prima = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prima = False  
            break
    if prima:
        bil_prima.append(num) 
        count += 1  
    
    if count == 78498:  
        break

T = int(input())

output = []  

for t in range(T):
    A, B = map(int, input().split())
    output.append(f"Test Case #{t+1} :")
    for i in range(A-1, B):
        output.append(str(bil_prima[i]))

print("\n".join(output))

