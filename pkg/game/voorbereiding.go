package game

import (
	"RISK/pkg/models"
	"bufio"
	"fmt"
	"os"
	"strings"
)

func Kleuren_kiezen() {
	// Verschillende soorten legers
	Kleuren := models.Kleuren
	keuzes := make([]string, len(Kleuren))
	copy(keuzes, Kleuren)

	var Legers = models.Legers

	var leger string
	var found bool

	// Scanner voor speler input
	scanner := bufio.NewScanner(os.Stdin)

	for i := 0; i < models.Spelers; i++ {
		for {
			fmt.Printf("Welk leger zou jij (Speler %v) willen zijn?\nDe beschikbare kleuren zijn: %v \n>>> ", i+1, keuzes)

			// Lees de ouput van de speler
			scanner.Scan()
			leger = strings.ToLower(scanner.Text())

			// Kijk of de juiste kleur is ingevuld
			found = false
			for _, color := range keuzes {
				if strings.ToLower(color) == leger {
					found = true
					break
				}
			}

			// Als het leger is gekozen, stop de loop, anders doorvragen
			if found {
				break
			} else {
				fmt.Println(leger, "is niet een van de beschikbare kleuren")
			}
		}

		// Verwijder het gekozen leger van de slice
		for i, color := range keuzes {
			if strings.ToLower(color) == leger {
				// Verwijder de kleur
				Legers = append(Legers, leger)
				keuzes = append(keuzes[:i], keuzes[i+1:]...)
				break
			}
		}
	}
}
