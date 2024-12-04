package main

import (
	"RISK/pkg/models"
)

func main() {
	models.Gebieden_ophalen()

	models.Landen_verdelen()

	// game.Kleuren_kiezen()
	// fmt.Println(models.Kleuren)
	// fmt.Println(models.Legers)

	// game.Troepen_verdelen()
}
