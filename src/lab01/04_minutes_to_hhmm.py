m=int(input("Минуты:"))
hours=m//60
minutes=m%60
print(f"{hours}:{minutes:02d}") # 02d - если число от 0 до 9, то добавл слева незначащ 0