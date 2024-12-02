package main

import (
	"RISK/pkg/game"
	"RISK/pkg/models"
	"fmt"
)

func main() {
	game.Kleuren_kiezen()
	fmt.Println(models.Kleuren)
	fmt.Println(models.Legers)
}
