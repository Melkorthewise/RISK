package game

import (
	"RISK/pkg/models"
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strings"
)

func Kleuren_kiezen() {
	// Verschillende soorten legers
	Kleuren := models.Kleuren
	keuzes := make([]string, len(Kleuren))
	copy(keuzes, Kleuren)

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
				models.Legers = append(models.Legers, leger)
				keuzes = append(keuzes[:i], keuzes[i+1:]...)
				break
			}
		}
	}

	randomNumber := rand.Intn(len(keuzes))
	models.Legers = append(models.Legers, keuzes[randomNumber])

	//fmt.Println(randomNumber)
	//fmt.Println(keuzes[randomNumber])

}

func Landen_verdelen() {
	// Todo
}

func Troepen_verdelen() {
	troepen := 40 // Moet het juiste aantal zijn voor het aantal spelers en moet nog min het aantal landen
	models.Troepen = append(models.Troepen, troepen, troepen, troepen)

	scanner := bufio.NewScanner(os.Stdin)

	landen := models.Landen.Gebiedskaarten

	var found bool

	for i := 0; i < troepen; i++ {
		for j := 0; j < len(models.Legers); j++ {
			for {
				fmt.Printf("Speler %v, %v\n", models.Legers[j], models.Troepen[j])
				fmt.Println("Op welk land zou je een troep willen neerzetten?")

				// Lees de ouput van de speler
				scanner.Scan()
				naar := strings.ToLower(scanner.Text())

				fmt.Println("Gebiedskaarten:", models.Landen.Gebiedskaarten)

				for land := range landen {
					if strings.ToLower(land) == naar {
						found = true
						break
					}
				}

				if found {
					break
				} else {
					fmt.Println(naar, "is niet een van de beschikbare landen")
				}

				break
			}
			break
		}
		break
	}
}
