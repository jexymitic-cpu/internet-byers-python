ime=input("Unesi ime")
prezime=input("Unesi prezime")

print(ime,prezime)
broj_kupovina=int(input("Unesi broj kupovina:"))
print(broj_kupovina)
iznos1=float(input("Unesi iznos kupovine:"))
iznos2=float(input("Unesi iznos kupovine:"))
ukupno=iznos1+iznos2
print("Ukupan iznos:",ukupno)



while True:
    odgovor = input("Da li zelis novu kupovinu? ")
    if odgovor == "ne":
        break

    novi_iznos = float(input("Unesi iznos kupovine: "))
    ukupno = ukupno + novi_iznos
    broj_kupovina = broj_kupovina + 1


    print("Konačan iznos:", ukupno)

if broj_kupovina >= 20:
    print("Cest kupac")
else:
    print("Kupac nema 20 kupovina")

if ukupno > 100000 and broj_kupovina > 10:
    print("VIP kupac")
else:
    print("Standard kupac")