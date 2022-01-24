arter_svenska = ['Större strandsnäcka', 'Vivipar strandsnäcka', 'Tornsnäcka', 'Pelikanfotsnäcka', 'Nätsnäcka', 'Valthornsnäcka', 'Neptunsnäcka', 'Sjöhare', 'Blåmussla', 'Hästmussla', 'Europeiskt ostron', 'Japansk jätteostron', 'Stor kammussla', 'Hoppmussla', 'Sjustrålig kammussla', 'Islandsmussla', 'Hjärtmussla', 'Taggig Hjärtmussla', 'Amerikansk kammussla', 'Sandmussla', 'Skeppsmask', 'Tandsnäcka']
arter_latin = ['Littorina littorea', 'Littorina saxatilis', 'Turritella communis', 'Aporrhais pespelecani', 'Nassarius nitidus', 'Buccinum undatum', 'Neptunea antiqua', 'Alypsia punctata', 'Mytilus edulis', 'Modiolus modiolus', 'Ostrea edulis', 'Crassostrea gigas', 'Pecten maximus', 'Aequipteren opercularis', 'Pseudamussium peslutrae', 'Arctica islandica', 'Cerastoderma sp', 'Acanthocardia echinata', 'Ensis americanus', 'Mya arenaria', 'Teredo navalis', 'Antalis entalis']

def test_latin():
    poäng = 0
    for i in arter_latin:
        index = arter_latin.index(i)
        svar = str(input(f"Vad heter {arter_svenska[index]} på latin?: ").lower())
        while svar != str(arter_latin[index].lower()):    
            svar = str(input("Fel svar, pröva igen: ").lower())
        else:
            poäng += 1
            print(f"Korrekt! {poäng} poäng")

def test_svenska():
    poäng = 0
    for i in arter_svenska:
        index = arter_svenska.index(i)
        svar = str(input(f"Vad heter {arter_latin[index]} på svenska?: ").lower())
        while svar != str(arter_svenska[index].lower()):    
            svar = str(input("Fel svar, pröva igen: ").lower())
        else:
            poäng += 1
            print(f"Korrekt! {poäng} poäng")
val = ""
while val != "latin" or "svenska" :
    val = str(input("Vill du svara på Svenska eller Latin?: ")).lower()
    if val == "latin":
        test_latin()
    elif val == "svenska":
        test_svenska()
    else:
        print("Felaktig inmatning.")





