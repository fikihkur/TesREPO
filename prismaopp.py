#menghitung volume prisma, kubus, dan balok

#class prisma
class prisma:
    
    def __init__(self, alas, tinggis, tinggip):
        self.alas = alas
        self.tinggis = tinggis
        self.tinggip = tinggip

    def hasil_volume(self):
        return 0.5 * self.alas * self.tinggis * self.tinggip

#class kubus
class kubus:
    def __init__(self, sisi):
        self.sisi = sisi

    def hasil_volume(self):
        return self.sisi * self.sisi * self.sisi

#class balok
class balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hasil_volume(self):
        return self.panjang * self.lebar * self.tinggi

#mempassing nilai parameter
prisma1 = prisma(5, 8, 10)
prisma2 = prisma(8, 9, 10)

kubus1 = kubus(10)
kubus2 = kubus(5)

balok1 = balok(5, 8, 10)
balok2 = balok(2, 8, 15)

#memunculkan output
print("Volume Prisma 1 adalah ", prisma1.hasil_volume())
print("Volume Prisma 2 adalah ", prisma2.hasil_volume(), "\n")

print("Volume Kubus 1 adalah ", kubus1.hasil_volume())
print("Volume Kubus 2 adalah ", kubus2.hasil_volume(), "\n")

print("Volume Balok 1 adalah ", balok1.hasil_volume())
print("Volume Balok 2 adalah ", balok2.hasil_volume(), "\n")