use std::collections::HashMap;

fn main() {
    let swedish_names = [
        "Större strandsnäcka",
        "Vivipar strandsnäck",
        "Tornsnäck",
        "Pelikanfotsnäcka",
        "Nätsnäcka",
        "Valthornsnäcka",
        "Neptunsnäcka",
        "Sjöhare",
        "Blåmussla",
        "Hästmussla",
        "Europeiskt ostron",
        "Japansk jätteostron",
        "Stor kammussla",
        "Hoppmussla",
        "Sjustrålig kammussla",
        "Islandsmussla",
        "Hjärtmussla",
        "Taggig Hjärtmussla",
        "Amerikansk kammussla",
        "Sandmussla",
        "Skeppsmask",
        "Tandsnäcka",
    ];
    let latin_names = [
        "Littorina littorea",
        "Littorina saxatilis",
        "Turritella communis",
        "Aporrhais pespelecani",
        "Nassarius nitidus",
        "Buccinum undatum",
        "Neptunea antiqua",
        "Alypsia punctata",
        "Mytilus edulis",
        "Modiolus modiolus",
        "Ostrea edulis",
        "Crassostrea gigas",
        "Pecten maximus",
        "Aequipteren opercularis",
        "Pseudamussium peslutrae",
        "Arctica islandica",
        "Cerastoderma sp",
        "Acanthocardia echinata",
        "Ensis americanus",
        "Mya arenaria",
        "Teredo navalis",
        "Antalis entalis",
    ];
    let mut dictionary: HashMap<&str, &str> = HashMap::new();

    for (swedish, latin) in swedish_names.iter().zip(latin_names.iter()) {
        dictionary.insert(swedish, latin);
    }
    for (swedish, latin) in &dictionary {
        println!("{} - {}", swedish, latin);
    }
}
// fn start_test() {}
