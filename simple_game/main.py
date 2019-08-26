stos1 = [1, 2, 3, 4]
stos2 = [0, 0, 0, 0]
stos3 = [0, 0, 0, 0]

#funkcja sluzaca do wyswietlania stosow
def wyswietlanie():
    for i in range(4):
        print("    " + str(stos1[i]) + "           " + str(stos2[i]) + "           " + str(stos3[i]) + "    ")
    print("---------   ---------   ---------")

#funkcja sprawdzajaca czy liczba wieszka nie jest na liczbie mniejszej
def stos_check(liczba_pomocnicza,stos):
    for i in range(4):
        if stos[i] != 0:
            pomocnicza = stos[i]
            if liczba_przenoszona > pomocnicza:
                print("\033[0;31mPRZEGRALES!!!! LICZBA PRZENOSZONA NIE MOŻE BYĆ WIĘKSZA OD LICZBY POD SPODEM!\n Spróbuj ponownie;)")
                return 0
                break

#funkcja sprawdzajaca czy spelniony jest warunek wygranej
def win_check():
    if stos3 == [1, 2, 3, 4]:
        print("WYGRALES!!!")
        print("\u001b[32m Wygrałeś ! \u001b[0m")
        return 0


liczba_przenoszona = 0
koniec = 1


print("Gra polega na przeniesieniu wszystkich klocków z pierwszego stosu na stos trzeci. UWAGA! "
      "Nie możesz położyć większego klocka na klocku mniejszym! Good luck!")
while koniec !=0:
    liczba_przenoszona = 0
    wyswietlanie()
    print("podaj z ktorego stosu chcesz wziac liczbe")
    z_ktorego_stosu = int(input())
    print("podaj na ktory stos chcesz polozyc liczbe")
    na_ktory_stos = int(input())


    if z_ktorego_stosu == 1:
        for i in range(4):
            if stos1[i] != 0:
                liczba_przenoszona = stos1[i]
                stos1[i] = 0
                break

    if z_ktorego_stosu == 2:
        for i in range(4):
            if stos2[i] != 0:
                liczba_przenoszona = stos2[i]
                stos2[i] = 0
                break

    if z_ktorego_stosu == 3:
        for i in range(4):
            if stos3[i] != 0:
                liczba_przenoszona = stos3[i]
                stos3[i] = 0
                break


    if na_ktory_stos == 1:
        koniec = stos_check(liczba_przenoszona,stos1)
        stos1.reverse()
        for i in range(4):
            if stos1[i] == 0:
                stos1[i] = liczba_przenoszona
                stos1.reverse()
                break

    if na_ktory_stos == 2:
        koniec = stos_check(liczba_przenoszona,stos2)
        stos2.reverse()
        for i in range(4):
            if stos2[i] == 0:
                stos2[i] = liczba_przenoszona
                stos2.reverse()
                break


    if na_ktory_stos == 3:
        koniec = stos_check(liczba_przenoszona,stos3)
        stos3.reverse()
        for i in range(4):
            if stos3[i] == 0:
                stos3[i] = liczba_przenoszona
                stos3.reverse()
                break
    if koniec == 0:
        pass
    else:
        koniec = win_check()


input("Press some key ...")