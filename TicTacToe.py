# Tic-Tac-Toe spel i Python som körs i terminalen. Två spelare turas om att göra drag på en 3x3 spelplan.
print("Välkommen till Tic-Tac-Toe!")  # Skriver ut en välkomsttext
print("Spelare 1 är X och Spelare 2 är O.")  # Informerar om vilka symboler spelarna använder
print("För att göra ett drag, skriv in numret på rutan du vill markera.")  # Instruktioner för hur man gör ett drag

# Skapar en lista som representerar spelplanen med numrerade rutor
spelplan =["1", "2", "3",
           "4", "5", "6",
           "7", "8", "9"]  


def skriv_ut_spelplan(): # Definierar en funktion som skriver ut spelplanen
    '''Skriver ut spelplanen i terminalen.'''

    print(f"{spelplan[0]} | {spelplan[1]} | {spelplan[2]}")  # Skriver ut de 3 första rutorna på spelplanens första rad.
    print("--|---|--")  # Skriver ut en rad som separerar raderna på spelplanen.
    print(f"{spelplan[3]} | {spelplan[4]} | {spelplan[5]}")  # Skriver ut de 3 rutorna på spelplanens andra rad.
    print("--|---|--")  # Skriver ut en rad som separerar raderna på spelplanen.
    print(f"{spelplan[6]} | {spelplan[7]} | {spelplan[8]}")  # Skriver ut de 3 rutorna på spelplanens tredje rad.
    print()  # Skriver ut en tom rad efter spelplanen.

def gör_drag(spelare):  # Definierar en funktion som låter spelaren göra ett drag
    '''Låter spelaren välja en ruta på spelplanen.'''

    while True:  # Startar en oändlig loop som fortsätter tills spelaren gör ett giltigt drag
        val = input(f"Spelare {spelare}, välj en ruta (1-9): ")  # Ber spelaren att välja en ruta
        if not val.isdigit():  # Kontrollerar om spelarens val inte är ett tal
            print("Du måste skriva ett tal mellan 1 och 9.")  # Skriver ut ett felmeddelande om valet inte är ett tal
            continue  # Hoppar tillbaka till början av loopen för att låta spelaren försöka igen

        # Omvandlar spelarens val till ett index i listan spelplan
        ruta = int(val) - 1  # Omvandlar spelarens val till ett index i listan spelplan. Sträng omvandlas till ett heltal och subtraheras med 1 för att matcha listans indexering (0-8).
        if not 0 <= ruta < 9: # Kontrollerar om spelarens val är utanför intervallet 0-8 (motsvarar rutor 1-9)
            print("Välj en ruta mellan 1 och 9.") # Skriver ut ett felmeddelande om valet är utanför intervallet
            continue # Hoppar tillbaka till början av loopen för att låta spelaren försöka igen

        if spelplan[ruta] in ["X", "O"]:  # Kontrollerar om rutan redan är markerad med X eller O
            print("Den rutan är redan upptagen. Välj en annan ruta.")  # Skriver ut ett felmeddelande om rutan redan är markerad
            continue  # Hoppar tillbaka till början av loopen för att låta spelaren försöka igen

        spelplan[ruta] = spelare
        break  # Avslutar loopen när ett giltigt drag har gjorts


def kontrollera_vinnare(spelare):  # Definierar en funktion som kontrollerar om en spelare har vunnit
    '''Kontrollerar om någon spelare har vunnit spelet.'''

    vinstkombinationer = [  # Skapar en lista med alla möjliga vinnande kombinationer
        [0, 1, 2],  # Första raden
        [3, 4, 5],  # Andra raden
        [6, 7, 8],  # Tredje raden
        [0, 3, 6],  # Första kolumnen
        [1, 4, 7],  # Andra kolumnen
        [2, 5, 8],  # Tredje kolumnen
        [0, 4, 8],  # Diagonal från vänster till höger
        [2, 4, 6]   # Diagonal från höger till vänster
    ]

    for kombination in vinstkombinationer:  # Loopar igenom varje vinnande kombination
        if (spelplan[kombination[0]] == spelare and # Kontrollerar om den första rutan i kombinationen är markerad av spelaren
            spelplan[kombination[1]] == spelare and # Kontrollerar om den andra rutan i kombinationen är markerad av spelaren
            spelplan[kombination[2]] == spelare):  # Kontrollerar om den tredje rutan i kombinationen är markerad av spelaren
            return True  # Returnerar True om en vinnande kombination hittas
    return False  # Returnerar False om ingen vinnande kombination hittas


def spelplan_full():  # Definierar en funktion som kontrollerar om spelplanen är full
    '''Kontrollerar om alla rutor på spelplanen är markerade.'''

    for ruta in spelplan: # Loopar igenom varje ruta på spelplanen
        if ruta not in ["X", "O"]: # Kontrollerar om rutan inte är markerad med X eller O
            return False # Returnerar False om det finns minst en ruta som inte är markerad
    return True # Returnerar True om alla rutor är markerade


def spela():  # Definierar huvudfunktionen som kör spelet
    '''Starta spelet'''

    spelare = "X"  # Sätter den första spelaren till X

    while True:  # Startar en oändlig loop som fortsätter tills spelet är slut
        skriv_ut_spelplan()  # Skriver ut den aktuella spelplanen
    
        gör_drag(spelare)  # Låter den aktuella spelaren göra ett drag

        if kontrollera_vinnare(spelare):  # Kontrollerar om den aktuella spelaren har vunnit
            skriv_ut_spelplan()  # Skriver ut den aktuella spelplanen
            print(f"Grattis! Spelare {spelare} har vunnit!")  # Skriver ut ett meddelande om att spelaren har vunnit
            break  # Avslutar loopen och spelet

        if spelplan_full():  # Kontrollerar om spelplanen är full
            skriv_ut_spelplan()  # Skriver ut den aktuella spelplanen
            print("Spelet är oavgjort!")  # Skriver ut ett meddelande om att spelet är oavgjort
            break  # Avslutar loopen och spelet

        if spelare == "X":  # Byter spelare från X till O
            spelare = "O"  # Sätter den aktuella spelaren till O
        else:
            spelare = "X"  # Sätter den aktuella spelaren till X        

if __name__ == "__main__": # Kör spelet om filen körs direkt
    spela() 

    while True:  # Startar en oändlig loop som fortsätter tills spelaren väljer att avsluta
        svar = input("Vill du spela igen?")  # Ber spelaren om de vill spela igen
        if svar == "ja":  # Kontrollerar om spelarens svar är "ja"
            spelplan = ["1", "2", "3",  # Återställer spelplanen till ursprungsläget
                        "4", "5", "6",
                        "7", "8", "9"]
            spela()  # Startar spelet igen
        elif svar == "nej":  # Kontrollerar om spelarens svar är "nej"
            break  # Avslutar loopen och spelet
print("Tack för att du spelade Tic-Tac-Toe!")  # Skriver ut ett tackmeddelande när spelet är slut