
premena = True
while premena:
    import math




    print ("======Vitaj v kalkulačke======")
    print ("vyber si matematicku operaciu")
    print ("1.===sčítanie===")
    print ("2.===odčítani===")
    print ("3.===násobenie===")
    print ("4.===delenie===")
    print ("5.===celociselne delenie===")
    print("6.===porovnavanie===")
    print ("7.===cosinus===")
    print ("8.===sinus===")
    print ("9.===tangens===")








    x= int(input("Zadaj operaciu:"))
    if x <7:
       a= float(input("Zadaj prve číslo: "))
       b= float(input("Zadaj druhe číslo: "))




    if x == 1:
        print("Vysledok je:" , a+b)
    if x == 2:
        print ("Vysledok je:" , a-b)
    if x == 3:
        print ("Vysledok je:" , a*b)
    if x == 4:
        print ("Vysledok je:" , a/b)
    if x == 5:
        print ("Vysledok je:" , a//b)
    if x == 6:
        veciii = True
        mensii = False
        if True:
            print ("veciii")
        if False:
            print ("mensii")
        if a < b:
            print(bool(a<b))
        if a > b:
            print(bool(b<a))
    if x == 7:
        a=float(input("Zadaj cislo: "))
        print("Vysledok je:" , math.cos(a))
    if x == 8:
        a=float(input("Zadaj cislo: "))
        print("Vysledok je:" , math.sin(a))
    if x == 9:
        a=float(input("Zadaj cislo: "))
        print("Vysledok je:" , math.tan(a))

    premena = input("Chces pokracovat ano alebo nie: ")
    if premena == "nie" :
        print("tak cau")
        break





