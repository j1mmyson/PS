package kata

type Fighter struct {
	Name                    string
	Health, DamagePerAttack int
}

func DeclareWinner(fighter1 Fighter, fighter2 Fighter, firstAttacker string) string {
	var winner Fighter
	var attacker Fighter
	var defender Fighter

	if firstAttacker == fighter1.Name {
		attacker, defender = fighter1, fighter2
	} else {
		attacker, defender = fighter2, fighter1
	}

	for {
		defender.Health -= attacker.DamagePerAttack
		if defender.Health <= 0 {
			winner = attacker
			break
		}
		attacker, defender = defender, attacker
	}

	return winner.Name
}
