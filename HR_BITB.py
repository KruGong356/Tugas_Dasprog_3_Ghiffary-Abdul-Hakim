import math

ukuran = int(input())
LebarTotal = ukuran

if ukuran <= 8:
    print("Terlalu Kecil")
else: 
    if LebarTotal % 2 == 0:
        print(" " * ((LebarTotal // 2) - 1) + "*")
        for i in range(3):
            print(" " * ((LebarTotal // 2) - 2) + "|=|")
    else:
        print(" " * (LebarTotal // 2) + "*")
        for i in range(3):
            print(" " * ((LebarTotal // 2) - 1) + "|=|")
    
    TinggiSisa = LebarTotal - 4
    if (LebarTotal // 2) % 2 == 0: 
        Lebar2 = (LebarTotal // 2) + 1 
        print(" " * ((LebarTotal - Lebar2) // 2) + "-" * Lebar2)
        for i in range(math.ceil(TinggiSisa / 2)):
            print(" " * ((LebarTotal - Lebar2) // 2) + "|" + "=" * (Lebar2 - 2) + "|")
    else:
        Lebar2 = LebarTotal // 2
        print(" " * ((LebarTotal - Lebar2) // 2) + "-" * Lebar2)
        for i in range(math.ceil(TinggiSisa / 2)):
            print(" " * ((LebarTotal - Lebar2) // 2) + "|" + "=" * (Lebar2 - 2) + "|")
    
    print("-" * LebarTotal)
    for i in range(TinggiSisa // 2):
        print("|" + "=" * (LebarTotal - 2) + "|")
    print("-" * LebarTotal)



