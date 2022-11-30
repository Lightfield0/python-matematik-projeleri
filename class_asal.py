sayi = int(input("Sayi giriniz>> "))

class Prime:
    
    def __init__(self):
        self.sayi = sayi

    def isPrime(self, sayi):
        if self.sayi > 1:
            for i in range(2, self.sayi):
                if self.sayi % i == 0:
                    print(self.sayi," Sayısı asal değil")
                    break
            else:
                print(self.sayi," sayısı asaldır.")
        else:
            print(self.sayi," sayısı birden büyük olmalıdır.")

asal = Prime()
asal.isPrime(sayi)