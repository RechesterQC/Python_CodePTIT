import math


class PhanSo:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
    def toigian(self):
        ucln = math.gcd(self.tu,self.mau)
        self.tu //= ucln
        self.mau //= ucln
    def __str__(self):
        return f'{self.tu}/{self.mau}'

if __name__ == "__main__":
    tu,mau = map(int,input().split())
    p = PhanSo(tu,mau)
    p.toigian()
    print(p)

