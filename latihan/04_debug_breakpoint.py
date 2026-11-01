def hitung_diskon(total, persen):
    diskon = total * persen / 100
    hasil = total - diskon
    return hasil

harga = 200000
potongan = 10

total_bayar = hitung_diskon(harga, potongan)

print("Harga awal:", harga)
print("Diskon:", potongan, "%")
print("Total bayar:", total_bayar)