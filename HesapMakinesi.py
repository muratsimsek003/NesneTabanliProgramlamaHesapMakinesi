"Hesap makinesi programı"
"Nesne tabanlı programlama uygulaması"


class HesapMakinesi:
    # init metodu
    def __init__(self, a, b):
        # attribute
        self.value1 = a
        self.value2 = b

    def toplama(self):
        return self.value1 + self.value2

    def carpma(self):
        return self.value1 * self.value2

    def bolme(self):
        return self.value1 / self.value2,

    def cikarma(self):
        return self.value1 - self.value2


print("Birini secin toplama(1), carpma(2), bolme(3), cikarma(4)")
selection = input("1,2,3,4 seceneklerinden birini secin:")

v1 = int(input("ilk deger:"))
v2 = int(input("ikinci deger:"))

c1 = HesapMakinesi(v1, v2)
if selection == "1":
    add_result = c1.toplama()
    print("Toplama: {}".format(add_result))
elif selection == "2":  # else if = elif
    multiply_result = c1.carpma()
    print("Carpma: {}".format(multiply_result))
elif selection == "3":
    div_result = c1.bolme()
    print("Bolme: {}".format(div_result))
elif selection == "4":
    div_result = c1.cikarma()
    print("Cikarma: {}".format(div_result))
else:
    print("Error there is no proper selection")