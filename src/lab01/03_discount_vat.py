price=float(input("price:"))#Исходная цена товара
discount=float(input("discount:"))#Процент скидки
vat=float(input("vat:"))#Процент НДС
base = price*(1-discount/100)#Цена товара после скидки
vat_amount = base*(vat/100)#Сумма ндс, начисляемая на цену со скидкой
total = base + vat_amount #Итоговая сумма к оплате
print(f"База после скидки:{base:.2f} ₽")
print(f"НДС:{vat_amount:.2f} ₽")
print(f"Итого к оплате:{total:.2f} ₽")


