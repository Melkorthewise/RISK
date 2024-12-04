package models

import (
	"fmt"
	"time"

	"golang.org/x/exp/rand"
)

func Landen_verdelen() {
	// Extract country names

	// Shuffle the countries
	rand.Seed(uint64(time.Now().UnixNano())) // Initialize the random seed
	rand.Shuffle(len(countries), func(i, j int) {
		countries[i], countries[j] = countries[j], countries[i]
	})

	// Divide countries into 3 players
	players := map[string][]string{
		"Player1": {},
		"Player2": {},
		"Player3": {},
	}
	for i, country := range countries {
		switch i % 3 {
		case 0:
			players["Player1"] = append(players["Player1"], country)
		case 1:
			players["Player2"] = append(players["Player2"], country)
		case 2:
			players["Player3"] = append(players["Player3"], country)
		}
	}

	// Print the results
	for player, assignedCountries := range players {
		fmt.Printf("%s: %v\n", player, assignedCountries)
	}
}
