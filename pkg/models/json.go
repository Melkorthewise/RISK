package models

import (
	"io"
	"log"
	"os"
)

// Definieer the struct
type Gebied struct {
	Continent     string   `json:"continent"`
	Troep         string   `json:"troep"`
	Locatie       string   `json:"locatie"`
	Grenzen       []string `json:"grenzen"`
	Speler        string   `json:"speler"`
	AantalTroepen int      `json:"aantal_troepen"`
}

// type Gebiedskaarten struct {
//	Gebiedskaarten map[string]Gebied `json:"gebiedskaarten"`
// }

// var Landen Gebiedskaarten

var Landen map[string]Gebied

func Gebieden_ophalen() {

	// wd, err := os.Getwd()
	// if err != nil {
	// 	fmt.Printf("Error getting working directory: %v\n", err)
	// 	return
	// }
	// fmt.Printf("Current working directory: %s\n", wd)

	// Open JSON file
	file, err := os.Open("../../pkg/models/gebiedskaarten.json")
	if err != nil {
		log.Fatalf("Error opening file: %v", err)
	}
	defer file.Close()

	// Lees de inhoud van de JSON
	data, err := io.ReadAll(file)
	if err != nil {
		log.Fatalf("Error opening file: %v", err)
	}

	// Declare the map to hold the data
	// var Landen map[string]Gebied

	// Unmarshal the JSON into the map
	// err = json.Unmarshal(data, &Landen)
	// if err != nil {
	// 	log.Fatal(err)
	// }

	// Bind the JSON body to the struct and validate
	if err := data.ShouldBindJSON(&Landen); err != nil {
		return
	}

	// // Accessing the data
	// // for name, region := range gebiedskaarten.Gebiedskaarten {
	// // 	fmt.Printf("Region: %s\n", name)
	// // 	fmt.Printf("  Continent: %s\n", region.Continent)
	// // 	fmt.Printf("  Troep: %s\n", region.Troep)
	// // 	fmt.Printf("  Locatie: %s\n", region.Locatie)
	// // 	fmt.Printf("  Grenzen: %v\n", region.Grenzen)
	// // }
}

// var Landen map[string]Gebied = map[string]Gebied{
// 	"Alaska":                  {Continent: "N_Amerika", Troep: "I", Locatie: "(105, 120)", Grenzen: []string{"Noordwestelijke staten", "Alberta", "Kamtsjatka"}, Speler: "blauw", AantalTroepen: 1},
// 	"Peru":                    {Continent: "Z_Amerika", Troep: "I", Locatie: "(309, 508)", Grenzen: []string{"Venezuela", "Brazilie", "Argentinie"}, Speler: "blauw", AantalTroepen: 1},
// 	"Argentinie":              {Continent: "Z_Amerika", Troep: "I", Locatie: "(334, 596)", Grenzen: []string{"Peru", "Brazilie"}, Speler: "blauw", AantalTroepen: 1},
// 	"Scandinavie":             {Continent: "Europa", Troep: "C", Locatie: "(588, 163)", Grenzen: []string{"Ijsland", "Rusland", "Groot-brittannie", "Noord-europa"}, Speler: "blauw", AantalTroepen: 1},
// 	"Rusland":                 {Continent: "Europa", Troep: "C", Locatie: "(684, 217)", Grenzen: []string{"Scandinavie", "Noord-europa", "Zuid-europa", "Oeral", "Afghanistan", "Midden-oosten"}, Speler: "blauw", AantalTroepen: 1},
// 	"Groot-brittannie":        {Continent: "Europa", Troep: "A", Locatie: "(495, 255)", Grenzen: []string{"Ijsland", "Scandinavie", "Noord-europa", "West-europa"}, Speler: "blauw", AantalTroepen: 1},
// 	"Zuid-europa":             {Continent: "Europa", Troep: "A", Locatie: "(599, 326)", Grenzen: []string{"Noord-europa", "West-europa", "Rusland", "Midden-oosten", "Noord-afrika", "Egypte"}, Speler: "blauw", AantalTroepen: 1},
// 	"Egypte":                  {Continent: "Afrika", Troep: "I", Locatie: "(631, 438)", Grenzen: []string{"Noord-afrika", "Zuid-europa", "Midden-oosten", "Oost-afrika"}, Speler: "blauw", AantalTroepen: 1},
// 	"Siberie":                 {Continent: "Azie", Troep: "C", Locatie: "(849, 143)", Grenzen: []string{"Oeral", "China", "Yakutsk", "Irkoetsk", "Mongolie"}, Speler: "blauw", AantalTroepen: 1},
// 	"Afghanistan":             {Continent: "Azie", Troep: "C", Locatie: "(774, 283)", Grenzen: []string{"Rusland", "Midden-oosten", "Oeral", "China", "India"}, Speler: "blauw", AantalTroepen: 1},
// 	"Japan":                   {Continent: "Azie", Troep: "A", Locatie: "(1039, 277)", Grenzen: []string{"Mongolie", "Kamtsjatka"}, Speler: "blauw", AantalTroepen: 1},
// 	"Midden-oosten":           {Continent: "Azie", Troep: "I", Locatie: "(707, 394)", Grenzen: []string{"Zuid-europa", "Rusland", "Afghanistan", "India", "Egypte", "Oost-afrika"}, Speler: "blauw", AantalTroepen: 1},
// 	"India":                   {Continent: "Azie", Troep: "C", Locatie: "(835, 390)", Grenzen: []string{"Midden-oosten", "Afghanistan", "China", "Zuidoost-azie"}, Speler: "blauw", AantalTroepen: 1},
// 	"West-australie":          {Continent: "Oceanie", Troep: "A", Locatie: "(975, 637)", Grenzen: []string{"Indonesie", "Oost-australie"}, Speler: "blauw", AantalTroepen: 1},
// 	"Noordwestelijke staten":  {Continent: "N_Amerika", Troep: "A", Locatie: "(217, 121)", Grenzen: []string{"Alaska", "Alberta", "Ontario", "Groenland"}, Speler: "groen", AantalTroepen: 1},
// 	"Groenland":               {Continent: "N_Amerika", Troep: "C", Locatie: "(417, 86)", Grenzen: []string{"Noordwestelijke staten", "Ontario", "Oost-canada", "Ijsland"}, Speler: "groen", AantalTroepen: 1},
// 	"Ontario":                 {Continent: "N_Amerika", Troep: "C", Locatie: "(280, 196)", Grenzen: []string{"Noordwestelijke staten", "Alberta", "Groenland", "Verenigde staten (west)", "Oost-canada", "Verenigde staten (oost)"}, Speler: "groen", AantalTroepen: 1},
// 	"Verenigde staten (west)": {Continent: "N_Amerika", Troep: "A", Locatie: "(215, 270)", Grenzen: []string{"Alberta", "Ontario", "Verenigde staten (oost)", "Centraal-amerika"}, Speler: "groen", AantalTroepen: 1},
// 	"Verenigde staten (oost)": {Continent: "N_Amerika", Troep: "A", Locatie: "(296, 284)", Grenzen: []string{"Verenigde staten (west)", "Ontario", "Oost-canada", "Centraal-amerika"}, Speler: "groen", AantalTroepen: 1},
// 	"Brazilie":                {Continent: "Z_Amerika", Troep: "A", Locatie: "(382, 483)", Grenzen: []string{"Venezuela", "Peru", "Argentinie", "Noord-afrika"}, Speler: "groen", AantalTroepen: 1},
// 	"Ijsland":                 {Continent: "Europa", Troep: "I", Locatie: "(511, 169)", Grenzen: []string{"Groenland", "Groot-brittannie", "Scandinavie"}, Speler: "groen", AantalTroepen: 1},
// 	"Noord-afrika":            {Continent: "Afrika", Troep: "C", Locatie: "(568, 465)", Grenzen: []string{"Brazilie", "West-europa", "Zuid-europa", "Egypte", "Centraal-afrika", "Oost-afrika"}, Speler: "groen", AantalTroepen: 1},
// 	"Oost-afrika":             {Continent: "Afrika", Troep: "I", Locatie: "(680, 500)", Grenzen: []string{"Noord-afrika", "Egypte", "Centraal-afrika", "Midden-oosten", "Zuid-afrika", "Madagaskar"}, Speler: "groen", AantalTroepen: 1},
// 	"Madagaskar":              {Continent: "Afrika", Troep: "C", Locatie: "(729, 641)", Grenzen: []string{"Zuid-afrika", "Oost-afrika"}, Speler: "groen", AantalTroepen: 1},
// 	"Kamtsjatka":              {Continent: "Azie", Troep: "I", Locatie: "(1024, 116)", Grenzen: []string{"Yakutsk", "Irkoetsk", "Mongolie", "Japan", "Alaska"}, Speler: "groen", AantalTroepen: 1},
// 	"Irkoetsk":                {Continent: "Azie", Troep: "C", Locatie: "(919, 195)", Grenzen: []string{"Siberie", "Yakutsk", "Kamtsjatka", "Mongolie"}, Speler: "groen", AantalTroepen: 1},
// 	"Indonesie":               {Continent: "Oceanie", Troep: "A", Locatie: "(931, 540)", Grenzen: []string{"Zuidoost-azie", "Nieuw-guinea", "West-australie"}, Speler: "groen", AantalTroepen: 1},
// 	"Oost-australie":          {Continent: "Oceanie", Troep: "A", Locatie: "(1052, 612)", Grenzen: []string{"Nieuw-guinea", "West-australie"}, Speler: "groen", AantalTroepen: 1},
// 	"Alberta":                 {Continent: "N_Amerika", Troep: "C", Locatie: "(201, 187)", Grenzen: []string{"Alaska", "Noordwestelijke staten", "Ontario", "Verenigde staten (west)"}, Speler: "paars", AantalTroepen: 1},
// 	"Oost-canada":             {Continent: "N_Amerika", Troep: "C", Locatie: "(355, 204)", Grenzen: []string{"Groenland", "Ontario", "Verenigde staten (oost)"}, Speler: "paars", AantalTroepen: 1},
// 	"Centraal-amerika":        {Continent: "N_Amerika", Troep: "A", Locatie: "(222, 350)", Grenzen: []string{"Verenigde staten (west)", "Verenigde staten (oost)", "Venezuela"}, Speler: "paars", AantalTroepen: 1},
// 	"Venezuela":               {Continent: "Z_Amerika", Troep: "I", Locatie: "(303, 422)", Grenzen: []string{"Centraal-amerika", "Peru", "Brazilie"}, Speler: "paars", AantalTroepen: 1},
// 	"Noord-europa":            {Continent: "Europa", Troep: "A", Locatie: "(587, 262)", Grenzen: []string{"Groot-brittannie", "Scandinavie", "Rusland", "West-europa", "Zuid-europa"}, Speler: "paars", AantalTroepen: 1},
// 	"West-europa":             {Continent: "Europa", Troep: "A", Locatie: "(518, 343)", Grenzen: []string{"Groot-brittannie", "Noord-europa", "Zuid-europa", "Noord-afrika"}, Speler: "paars", AantalTroepen: 1},
// 	"Centraal-afrika":         {Continent: "Afrika", Troep: "I", Locatie: "(626, 550)", Grenzen: []string{"Noord-afrika", "Oost-afrika", "Zuid-afrika", "Madagaskar"}, Speler: "paars", AantalTroepen: 1},
// 	"Zuid-afrika":             {Continent: "Afrika", Troep: "A", Locatie: "(639, 639)", Grenzen: []string{"Centraal-afrika", "Oost-afrika", "Madagaskar"}, Speler: "paars", AantalTroepen: 1},
// 	"Oeral":                   {Continent: "Azie", Troep: "C", Locatie: "(794, 190)", Grenzen: []string{"Rusland", "Siberie", "China", "Afghanistan"}, Speler: "paars", AantalTroepen: 1},
// 	"Yakutsk":                 {Continent: "Azie", Troep: "C", Locatie: "(931, 111)", Grenzen: []string{"Siberie", "Kamtsjatka", "Irkoetsk"}, Speler: "paars", AantalTroepen: 1},
// 	"China":                   {Continent: "Azie", Troep: "I", Locatie: "(890, 332)", Grenzen: []string{"Oeral", "Siberie", "Mongolie", "India", "Zuidoost-azie", "Afghanistan"}, Speler: "paars", AantalTroepen: 1},
// 	"Mongolie":                {Continent: "Azie", Troep: "I", Locatie: "(932, 274)", Grenzen: []string{"Siberie", "Irkoetsk", "Japan", "China"}, Speler: "paars", AantalTroepen: 1},
// 	"Zuidoost-azie":           {Continent: "Azie", Troep: "I", Locatie: "(919, 425)", Grenzen: []string{"India", "China", "Zuidoost-azie", "Indonesie"}, Speler: "paars", AantalTroepen: 1},
// 	"Nieuw-guinea":            {Continent: "Oceanie", Troep: "I", Locatie: "(1021, 511)", Grenzen: []string{"Indonesie", "Oost-australie"}, Speler: "paars", AantalTroepen: 1},
// {
