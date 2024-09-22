jmlh_brg = int(input())

daf_brg = []

for i in range(jmlh_brg):
    nama_brg, jmlh = input().split()
    daf_brg.append((nama_brg, int(jmlh)))

total_brg = int(input())

daf_total = []

for i in range(total_brg):
    nama, jmlh_total = input().split()
    daf_total.append((nama, int(jmlh_total)))
brg = {nama: jumlah for nama, jumlah in daf_brg}
brg_belian = {nama: jumlah for nama, jumlah in daf_total}
brg_total = []

for nama in brg:
    if nama in brg_belian:
        brg_total.append(nama)
        
if brg_total:
    print("CHARLIE")
print("Sisa stok")
for nama in brg:
    sisa_brg = abs(brg[nama] - brg_belian.get(nama, 0))
    print(f"{nama.capitalize()}: {sisa_brg}")