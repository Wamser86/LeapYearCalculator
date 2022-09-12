

while True:
    eingabe = int(input("Hallo Tony gib dein Jahr ein: "))

    if (eingabe % 4 == 0) and (eingabe % 100 != 0) or (eingabe % 400 == 0):
        print(eingabe, " ist EIN Schaltjahr")
    else:
        print(eingabe, " ist KEIN Schaltjahr")