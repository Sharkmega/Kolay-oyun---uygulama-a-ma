import os
csgo = "csgo"
steam = "steam"
epicgames = "epicgames"


secme = input("Hangi oyunu oynamak istiyorsunuz: ")

def oyun():

    if secme == csgo:
        print("Csgo açılıyor....")
        os.system("start csgo.url")
        oyun()

    if secme == steam:
        print("Steam açılıyor....")
        os.system("start steam")
        oyun()

    if secme == epicgames:
        print("Epic games açılıyor....")
        os.system("start epic.lnk")
        oyun()


while True:
    oyun()