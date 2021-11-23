class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        self.complex = complex(real, imag)

    def __str__(self):
        return f'{self.complex}'

    def __add__(self, other):
        return (self.real + other.real) + (self.imag + other.imag) * 1j

    def __mul__(self, other):
        return (self.real * other.real - self.imag * other.imag) + (
                    self.imag * other.real + self.real * other.imag) * 1j


cn_1 = ComplexNumber(4, 5)
cn_2 = ComplexNumber(2, 7)
cn_3 = ComplexNumber(3, 1)

print(f'Сложение: {cn_2} и {cn_3}')
print(cn_2 + cn_3)
print(f'Умножение: {cn_1} и {cn_3}')
print(cn_1 * cn_3)
