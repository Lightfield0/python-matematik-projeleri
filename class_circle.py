a = float(input('Yari cap giriniz>> '))

class Circle:
    pi= 3.14

    def __init__(self, radius=1):
        self.radius = radius
        
    def perimeter(self):
        return 2*self.pi*self.radius

    def field(self):
        return self.pi*(self.radius**2)

c1 = Circle(a)

print(f'c1: alan = {c1.field()} çevre = {c1.perimeter()}')

sayi = int(input("Sayi giriniz>> "))
if sayi>1:
    for i in range(2,sayi):
        if sayi % i == 0:
            print("sayı asal değil")
            break
        else:
            print(sayi,"Asaldır")
else:
    print(sayi,"Birden büyük olmalıdır")

