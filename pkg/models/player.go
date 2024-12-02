package models

type Player struct {
    X, Y int
}

// Move player by a certain amount
func (p *Player) Move() {
    p.X += 1
    p.Y += 1
}

