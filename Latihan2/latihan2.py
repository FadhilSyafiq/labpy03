modal = 100000000
laba = 0

for bulan in range(1, 9):
    if bulan <= 2:
        persentase = 0
    elif bulan <= 3:
        persentase = 0.01
    elif bulan <= 5:
        persentase = 0.05
    elif bulan == 8:
        persentase = 0.02
    else:
        persentase = 0.03
    
    laba_bulan = modal * persentase
    laba += laba_bulan
    print(f"Laba bulan ke-{bulan} sebesar: {laba_bulan}")

print(f"Total laba adalah: {laba}")