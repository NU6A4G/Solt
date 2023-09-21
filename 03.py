# Jövedelemszámítás
print("Jövedelemszámítás\n")
kor = int(input("Hány éves vagy?"))
if kor > 25:
    gyerek = input("Három gyerekes anyuka vagy? (igen/nem)")
    while gyerek not in ["igen", "Igen", "i", "IGEN", "I", "nem", "NEM", "n", "N", "Nem"]:
        gyerek = input("HIBA \nVan 3 gyereked és nő vagy? (igen/nem)")
brutto = int(input("Mennyi a bruttó jövedelmed?"))
if kor <= 25 or gyerek in ["igen", "Igen", "i", "IGEN", "I"]:
    if brutto > 500000:
        szja = (brutto-500000) * 0.15
    else:
        szja = 0
else:
    szja = brutto * 0.15

print("SZJA:".ljust(20, "_"), str(int(szja)).rjust(10, "_"), " Ft",  sep="")
print("Nyugdíj:".ljust(20, "_"), str(int(brutto * 0.1)).rjust(10, "_"), " Ft", sep="")
print("EÜ:".ljust(20, "_"), str(int(brutto * 0.07)).rjust(10, "_"), " Ft", sep="")
print("MunkaN:".ljust(20, "_"), str(int(brutto * 0.015)).rjust(10, "_"), " Ft", sep="")
print("")
print("Nettó:".ljust(20, "_"), str(int(brutto - (brutto * 0.185) - szja)).rjust(10, "_"), " Ft", sep="")

