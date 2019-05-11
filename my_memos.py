import pickle
import time
import os

def main():
    
    tiedosto = "memo.dat"
    muistikirja = []
    try:
        with open(tiedosto,"rb") as rfp:
            muistikirja = pickle.load(rfp)

            
    #virheilmoitus:
    except (IOError, OSError):
        print("memo.dat was created for the first time.\n")

    while True:
        print("(1) Read memo\n(2) Add note\n(3) Edit node\n(4) Delete note\n(5) Save and close\n")

        try: #varmista, että kayttaja syottaa numeron
            valinta = int(input("What do you want to do?: "))

            if valinta == 1: #printtaa sisällon rivi rivilta
                for i in muistikirja:
                    print(i)

            elif valinta == 2: #lisaa uuden merkinnan
                lisays = input("Write new note: ")
                muistikirja.append(lisays + ":::" + time.strftime("%X %x"))

            elif valinta == 3 or valinta == 4:
                merkinnat = len(muistikirja) #listan alkioiden maara
                print("Memo has",merkinnat,"notes.")

                if valinta == 3: #korvaa merkinnan toisella
                    try:
                        muokattava = int(input("What number of notes do you want to edit?: "))
                        muokattava = muokattava - 1 #muuttaa valitun numeron alkion numeroksi
                        print(muistikirja[muokattava])
                        tilalle = input("Write note: ")
                        muistikirja[muokattava] = tilalle + ":::" + time.strftime("%X %x")   #korvaa merkinnan
                    except IndexError:
                        print("Edit error. ")

                if valinta == 4: #poistaa merkinnän
                    try:
                        poisto = int(input("What number of notes do you want to delete?: "))
                        poisto = poisto - 1 #muuttaa valitun numeron alkion numeroksi
                        print("Note",muistikirja[poisto],"was deleted.")
                        muistikirja.pop(poisto)
                    except IndexError:
                        print("Delete error.")

            elif valinta == 5: #tallentaa muutokset pickle-tiedostoon ja lopettaa
                print("Program is closed.")
                with open(tiedosto,"wb") as wfp:
                    pickle.dump(muistikirja,wfp)
                break

            else: #jos valinta muuta kuin 1,2,3,4,5
                print("Given number is not valid. Choose number between 1-5.")

        except ValueError: #annettu input ei ole numero
            print("Given character is not a number.")

if __name__ == "__main__":
    main()
