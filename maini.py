print("Функции программы:")
print("a) Вычисление дискриминанта")
print()

a="a"
b="b"

vibor = str(input("Введите букву функции: "))

if vibor == a:
    print("Вводите a, b, c : ")
    ashka = float(input("a: "))
    beshka = float(input("b: "))
    ceshka = float(input("c: "))
    koren1 =float((beshka**2)-(4*ashka*ceshka))
    print()

    if beshka > 0:
        beshka = (beshka*-1)
    else:
        beshka = (beshka*-1)

    if koren1 < 0:
        print("Нет решений.")
        print("D= "+str(int(koren1)))
    if koren1 != (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225,256,289,324,361,400):
        print(str(("x1= "+str(int(beshka))+"-√"+str(int(koren1)))+"/2*"+str(int(ashka))))
        print(str(("x2= "+str(int(beshka))+"+√"+str(int(koren1)))+"/2*"+str(int(ashka))))
        print("Ответ:")
    if koren1 == 0:
        print("X1= "+ str(float(beshka/(2*ashka))))
    if koren1 == 1:
        print("x1: " + str(float((beshka - 1) / (2 * ashka))))
        print("x2: " + str(float((beshka + 1) / (2 * ashka))))
    if koren1 == 4:
        print("x1: " + str(float((beshka - 2) / (2 * ashka))))
        print("x2: " + str(float((beshka + 2) / (2 * ashka))))
    if koren1 == 9:
        print("x1: " + str(float((beshka - 3) / (2 * ashka))))
        print("x2: " + str(float((beshka + 3) /( 2 * ashka))))
    if koren1 == 16:
        print("x1: " + str(float((beshka - 4) /( 2 * ashka))))
        print("x2: " + str(float((beshka + 4) / (2 * ashka))))
    if koren1 == 25:
        print("x1: " + str(float((beshka - 5) / (2 * ashka))))
        print("x2: " + str(float((beshka + 5) / (2 * ashka))))
    if koren1 == 36:
        print("x1: " + str(float((beshka - 6) /( 2 * ashka))))
        print("x2: " + str(float((beshka + 6) /( 2 * ashka))))
    if koren1 == 49:
        print("x1: " + str(float((beshka - 7) / (2 * ashka))))
        print("x2: " + str(float((beshka + 7) / (2 * ashka))))
    if koren1 == 64:
        print("x1: " + str(float((beshka - 8) / (2 * ashka))))
        print("x2: " + str(float((beshka + 8) / (2 * ashka))))
    if koren1 == 81:
        print("x1: " + str(float((beshka - 9) / (2 * ashka))))
        print("x2: " + str(float((beshka + 9) / (2 * ashka))))
    if koren1 == 100:
        print("x1: " + str(float((beshka - 10) / (2 * ashka))))
        print("x2: " + str(float((beshka + 10) /( 2 * ashka))))
    if koren1 == 121:
        print("x1: " + str(float((beshka - 11) /( 2 * ashka))))
        print("x2: " + str(float((beshka + 11) /( 2 * ashka))))
    if koren1 == 144:
        print("x1: " + str(float((beshka - 12) /( 2 * ashka))))
        print("x2: " + str(float((beshka + 12) /( 2 * ashka))))
    if koren1 == 169:
        print("x1: " + str(float((beshka - 13) /( 2 * ashka))))
        print("x2: " + str(float((beshka + 13) /( 2 * ashka))))
    if koren1 == 196:
        print("x1: " + str(float((beshka - 14) / (2 * ashka))))
        print("x2: " + str(float((beshka + 14) /( 2 * ashka))))
    if koren1 == 225:
        print("x1: " + str(float((beshka - 15) /(2 * ashka))))
        print("x2: " + str(float((beshka + 15) / (2 * ashka))))
    if koren1 == 256:
        print("x1: " + str(float((beshka - 16) /( 2 * ashka))))
        print("x2: " + str(float((beshka + 16) / (2 * ashka))))
    if koren1 == 289:
        print("x1: " + str(float((beshka - 17) / (2 * ashka))))
        print("x2: " + str(float((beshka + 17) / (2 * ashka))))
    if koren1 == 324:
        print("x1: " + str(float((beshka - 18) /( 2 * ashka))))
        print("x2: " + str(float((beshka + 18) /( 2 * ashka))))
    if koren1 == 361:
        print("x1: " + str(float((beshka - 19) / (2 * ashka))))
        print("x2: " + str(float((beshka + 19) / (2 * ashka))))
    if koren1 == 400:
        print("x1: " + str(float((beshka - 20) /( 2 * ashka))))
        print("x2: " + str(float((beshka + 20) / (2 * ashka))))
