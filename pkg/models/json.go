package models

// Definieer the struct
type Gebied struct {
	Continent string   `json:"continent"`
	Troep     string   `json:"troep"`
	Locatie   string   `json:"locatie"`
	Grenzen   []string `json:"grenzen"`
}

type Gebiedskaarten struct {
	Gebiedskaarten map[string]Gebied `json:"gebiedskaarten"`
}

var Landen = []map[string]map[string]interface{}{
	{
		"Alaska":           {"continent": "N_Amerika", "troep": "I", "locatie": "(105, 120)", "grenzen": []string{"Noordwestelijke staten", "Alberta", "Kamtsjatka"}, "speler": "blauw", "aantal_troepen": 1},
		"Peru":             {"continent": "Z_Amerika", "troep": "I", "locatie": "(309, 508)", "grenzen": []string{"Venezuela", "Brazilie", "Argentinie"}, "speler": "blauw", "aantal_troepen": 1},
		"Argentinie":       {"continent": "Z_Amerika", "troep": "I", "locatie": "(334, 596)", "grenzen": []string{"Peru", "Brazilie"}, "speler": "blauw", "aantal_troepen": 1},
		"Scandinavie":      {"continent": "Europa", "troep": "C", "locatie": "(588, 163)", "grenzen": []string{"Ijsland", "Rusland", "Groot-brittannie", "Noord-europa"}, "speler": "blauw", "aantal_troepen": 1},
		"Rusland":          {"continent": "Europa", "troep": "C", "locatie": "(684, 217)", "grenzen": []string{"Scandinavie", "Noord-europa", "Zuid-europa", "Oeral", "Afghanistan", "Midden-oosten"}, "speler": "blauw", "aantal_troepen": 1},
		"Groot-brittannie": {"continent": "Europa", "troep": "A", "locatie": "(495, 255)", "grenzen": []string{"Ijsland", "Scandinavie", "Noord-europa", "West-europa"}, "speler": "blauw", "aantal_troepen": 1},
		"Zuid-europa":      {"continent": "Europa", "troep": "A", "locatie": "(599, 326)", "grenzen": []string{"Noord-europa", "West-europa", "Rusland", "Midden-oosten", "Noord-afrika", "Egypte"}, "speler": "blauw", "aantal_troepen": 1},
		"Egypte":           {"continent": "Afrika", "troep": "I", "locatie": "(631, 438)", "grenzen": []string{"Noord-afrika", "Zuid-europa", "Midden-oosten", "Oost-afrika"}, "speler": "blauw", "aantal_troepen": 1},
		"Siberie":          {"continent": "Azie", "troep": "C", "locatie": "(849, 143)", "grenzen": []string{"Oeral", "China", "Yakutsk", "Irkoetsk", "Mongolie"}, "speler": "blauw", "aantal_troepen": 1},
		"Afghanistan":      {"continent": "Azie", "troep": "C", "locatie": "(774, 283)", "grenzen": []string{"Rusland", "Midden-oosten", "Oeral", "China", "India"}, "speler": "blauw", "aantal_troepen": 1},
		"Japan":            {"continent": "Azie", "troep": "A", "locatie": "(1039, 277)", "grenzen": []string{"Mongolie", "Kamtsjatka"}, "speler": "blauw", "aantal_troepen": 1},
		"Midden-oosten":    {"continent": "Azie", "troep": "I", "locatie": "(707, 394)", "grenzen": []string{"Zuid-europa", "Rusland", "Afghanistan", "India", "Egypte", "Oost-afrika"}, "speler": "blauw", "aantal_troepen": 1},
		"India":            {"continent": "Azie", "troep": "C", "locatie": "(835, 390)", "grenzen": []string{"Midden-oosten", "Afghanistan", "China", "Zuidoost-azie"}, "speler": "blauw", "aantal_troepen": 1},
		"West-australie":   {"continent": "Oceanie", "troep": "A", "locatie": "(975, 637)", "grenzen": []string{"Indonesie", "Oost-australie"}, "speler": "blauw", "aantal_troepen": 1},
	},
	{
		"Noordwestelijke staten":  {"continent": "N_Amerika", "troep": "A", "locatie": "(217, 121)", "grenzen": []string{"Alaska", "Alberta", "Ontario", "Groenland"}, "speler": "groen", "aantal_troepen": 1},
		"Groenland":               {"continent": "N_Amerika", "troep": "C", "locatie": "(417, 86)", "grenzen": []string{"Noordwestelijke staten", "Ontario", "Oost-canada", "Ijsland"}, "speler": "groen", "aantal_troepen": 1},
		"Ontario":                 {"continent": "N_Amerika", "troep": "C", "locatie": "(280, 196)", "grenzen": []string{"Noordwestelijke staten", "Alberta", "Groenland", "Verenigde staten (west)", "Oost-canada", "Verenigde staten (oost)"}, "speler": "groen", "aantal_troepen": 1},
		"Verenigde staten (west)": {"continent": "N_Amerika", "troep": "A", "locatie": "(215, 270)", "grenzen": []string{"Alberta", "Ontario", "Verenigde staten (oost)", "Centraal-amerika"}, "speler": "groen", "aantal_troepen": 1},
		"Verenigde staten (oost)": {"continent": "N_Amerika", "troep": "A", "locatie": "(296, 284)", "grenzen": []string{"Verenigde staten (west)", "Ontario", "Oost-canada", "Centraal-amerika"}, "speler": "groen", "aantal_troepen": 1},
		"Brazilie":                {"continent": "Z_Amerika", "troep": "A", "locatie": "(382, 483)", "grenzen": []string{"Venezuela", "Peru", "Argentinie", "Noord-afrika"}, "speler": "groen", "aantal_troepen": 1},
		"Ijsland":                 {"continent": "Europa", "troep": "I", "locatie": "(511, 169)", "grenzen": []string{"Groenland", "Groot-brittannie", "Scandinavie"}, "speler": "groen", "aantal_troepen": 1},
		"Noord-afrika":            {"continent": "Afrika", "troep": "C", "locatie": "(568, 465)", "grenzen": []string{"Brazilie", "West-europa", "Zuid-europa", "Egypte", "Centraal-afrika", "Oost-afrika"}, "speler": "groen", "aantal_troepen": 1},
		"Oost-afrika":             {"continent": "Afrika", "troep": "I", "locatie": "(680, 500)", "grenzen": []string{"Noord-afrika", "Egypte", "Centraal-afrika", "Midden-oosten", "Zuid-afrika", "Madagaskar"}, "speler": "groen", "aantal_troepen": 1},
		"Madagaskar":              {"continent": "Afrika", "troep": "C", "locatie": "(729, 641)", "grenzen": []string{"Zuid-afrika", "Oost-afrika"}, "speler": "groen", "aantal_troepen": 1},
		"Kamtsjatka":              {"continent": "Azie", "troep": "I", "locatie": "(1024, 116)", "grenzen": []string{"Yakutsk", "Irkoetsk", "Mongolie", "Japan", "Alaska"}, "speler": "groen", "aantal_troepen": 1},
		"Irkoetsk":                {"continent": "Azie", "troep": "C", "locatie": "(919, 195)", "grenzen": []string{"Siberie", "Yakutsk", "Kamtsjatka", "Mongolie"}, "speler": "groen", "aantal_troepen": 1},
		"Indonesie":               {"continent": "Oceanie", "troep": "A", "locatie": "(931, 540)", "grenzen": []string{"Zuidoost-azie", "Nieuw-guinea", "West-australie"}, "speler": "groen", "aantal_troepen": 1},
		"Oost-australie":          {"continent": "Oceanie", "troep": "A", "locatie": "(1052, 612)", "grenzen": []string{"Nieuw-guinea", "West-australie"}, "speler": "groen", "aantal_troepen": 1},
	},
	{
		"Alberta":          {"continent": "N_Amerika", "troep": "C", "locatie": "(201, 187)", "grenzen": []string{"Alaska", "Noordwestelijke staten", "Ontario", "Verenigde staten (west)"}, "speler": "paars", "aantal_troepen": 1},
		"Oost-canada":      {"continent": "N_Amerika", "troep": "C", "locatie": "(355, 204)", "grenzen": []string{"Groenland", "Ontario", "Verenigde staten (oost)"}, "speler": "paars", "aantal_troepen": 1},
		"Centraal-amerika": {"continent": "N_Amerika", "troep": "A", "locatie": "(222, 350)", "grenzen": []string{"Verenigde staten (west)", "Verenigde staten (oost)", "Venezuela"}, "speler": "paars", "aantal_troepen": 1},
		"Venezuela":        {"continent": "Z_Amerika", "troep": "I", "locatie": "(303, 422)", "grenzen": []string{"Centraal-amerika", "Peru", "Brazilie"}, "speler": "paars", "aantal_troepen": 1},
		"Noord-europa":     {"continent": "Europa", "troep": "A", "locatie": "(587, 262)", "grenzen": []string{"Groot-brittannie", "Scandinavie", "Rusland", "West-europa", "Zuid-europa"}, "speler": "paars", "aantal_troepen": 1},
		"West-europa":      {"continent": "Europa", "troep": "A", "locatie": "(518, 343)", "grenzen": []string{"Groot-brittannie", "Noord-europa", "Zuid-europa", "Noord-afrika"}, "speler": "paars", "aantal_troepen": 1},
		"Centraal-afrika":  {"continent": "Afrika", "troep": "I", "locatie": "(626, 550)", "grenzen": []string{"Noord-afrika", "Oost-afrika", "Zuid-afrika", "Madagaskar"}, "speler": "paars", "aantal_troepen": 1},
		"Zuid-afrika":      {"continent": "Afrika", "troep": "A", "locatie": "(639, 639)", "grenzen": []string{"Centraal-afrika", "Oost-afrika", "Madagaskar"}, "speler": "paars", "aantal_troepen": 1},
		"Oeral":            {"continent": "Azie", "troep": "C", "locatie": "(794, 190)", "grenzen": []string{"Rusland", "Siberie", "China", "Afghanistan"}, "speler": "paars", "aantal_troepen": 1},
		"Yakutsk":          {"continent": "Azie", "troep": "C", "locatie": "(931, 111)", "grenzen": []string{"Siberie", "Kamtsjatka", "Irkoetsk"}, "speler": "paars", "aantal_troepen": 1},
		"China":            {"continent": "Azie", "troep": "I", "locatie": "(890, 332)", "grenzen": []string{"Oeral", "Siberie", "Mongolie", "India", "Zuidoost-azie", "Afghanistan"}, "speler": "paars", "aantal_troepen": 1},
		"Mongolie":         {"continent": "Azie", "troep": "I", "locatie": "(932, 274)", "grenzen": []string{"Siberie", "Irkoetsk", "Japan", "China"}, "speler": "paars", "aantal_troepen": 1},
		"Zuidoost-azie":    {"continent": "Azie", "troep": "I", "locatie": "(919, 425)", "grenzen": []string{"India", "China", "Zuidoost-azie", "Indonesie"}, "speler": "paars", "aantal_troepen": 1},
		"Nieuw-guinea":     {"continent": "Oceanie", "troep": "I", "locatie": "(1021, 511)", "grenzen": []string{"Indonesie", "Oost-australie"}, "speler": "paars", "aantal_troepen": 1},
	},
}

// func Gebieden_ophalen() {
//
// 	// wd, err := os.Getwd()
// 	// if err != nil {
// 	// 	fmt.Printf("Error getting working directory: %v\n", err)
// 	// 	return
// 	// }
// 	// fmt.Printf("Current working directory: %s\n", wd)
//
// 	// Open JSON file
// 	file, err := os.Open("../../pkg/models/gebiedskaarten.json")
// 	if err != nil {
// 		log.Fatalf("Error opening file: %v", err)
// 	}
// 	defer file.Close()
//
// 	// Lees de inhoud van de JSON
// 	data, err := io.ReadAll(file)
// 	if err != nil {
// 		log.Fatalf("Error opening file: %v", err)
// 	}
//
// 	// Parse de JSON
// 	// var Landen Gebiedskaarten
// 	err = json.Unmarshal(data, &Landen)
// 	if err != nil {
// 		log.Fatalf("Error opening file: %v", err)
// 	}
//
// 	// Accessing the data
// 	// for name, region := range gebiedskaarten.Gebiedskaarten {
// 	// 	fmt.Printf("Region: %s\n", name)
// 	// 	fmt.Printf("  Continent: %s\n", region.Continent)
// 	// 	fmt.Printf("  Troep: %s\n", region.Troep)
// 	// 	fmt.Printf("  Locatie: %s\n", region.Locatie)
// 	// 	fmt.Printf("  Grenzen: %v\n", region.Grenzen)
// 	// }
// }
