package main

import (
	"RISK/pkg/game"
	"RISK/pkg/models"
	"fmt"
)

func main() {
	models.Gebieden_ophalen()

	game.Kleuren_kiezen()
	fmt.Println(models.Kleuren)
	fmt.Println(models.Legers)

	game.Troepen_verdelen()
}
