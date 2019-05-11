def oletusMuistio():
    try:
        tiedosto = open("muistio.dat")
        muistio = tiedosto.name
        tiedosto.close()
        return muistio
       
    except (IOError,OSError):
        print("Virhe tiedostossa, luodaan uusi muistio.dat")
        oletusmuistio = open("muistio.dat","a")
        muistio = oletusmuistio.name
        oletusmuistio.close()
        return muistio

def main ():
    import time
    muistio = oletusMuistio() #avaa/luo tiedoston muistio.dat
    while True:
        print("(1) Lue muistikirjaa\
        \n(2) Lisää merkintä\
        \n(3) Muokkaa merkintää\
        \n(4) Poista merkintä\
        \n(5) Lopeta\n")
        #varmistaa, että käyttäjä syöttää numeron
        try:
            valinta = int(input("Mitä haluat tehdä?:"))
            
            if valinta == 1:
                lue = open(muistio)
                print(lueTiedosto.read())
                lue.close()
                
            elif valinta == 2:
                lisaa = open(muistio,"a")
                lisays = input("Kirjoita uusi merkintä:")
                lisaa.write(lisays+":::"+time.strftime("%X %x")+"\n")
                lisaa.close()
                
            elif valinta == 3:
                muokkaa = open(muistio).read().splitlines() #tekee listan merkinnöistä riveittäin
                merkinnat = len(muokkaa) #listan alkioiden määrä
                print("Listalla on",merkinnat,"merkintää.")
                
                try:
                    poisto = int(input("Mitä niistä muutetaan?: "))
                    print(muokkaa[poisto])
                    tilalle = input("Anna uusi teksti:")
                    muokkaa[poisto] = tilalle+time.strftime("%X %x")+"\n" #korvaa merkinnän
                    
                except IndexError:
                    print("Virheellinen valinta.")                  
          
            elif valinta == 4:
                poista = open(muistio).read().splitlines() #tekee listan merkinnöistä riveittäin
                merkinnat = len(muokkaa) #listan alkioiden määrä
                print("Listalla on",merkinnat,"merkintää.")
                
                try:
                    poisto = int(input("Mitä niistä poistetaan?: "))
                    print(muokkaa[poisto])
                    tilalle = input("Anna uusi teksti:")
                    muokkaa[poisto] = tilalle+time.strftime("%X %x")+"\n" #korvaa merkinnän
                    
                except IndexError:
                    print("Virheellinen valinta.")   
                
            elif valinta == 5:
                print("Lopetetaan.")
                break
            
            else:
                print("Tuntematon valinta.")
                
        #palauttaa virheilmoituksen, jos käyttäjä syöttää muuta kuin numeron
        except ValueError: 
            print("Virheellinen valinta.")


if __name__ == "__main__":
    main()
