import random

Charizard_lvl = 90
Charizard_Atk = 205

Pow = 110

Feraligatr_lvl = 95
Feraligatr_Def = 188

Targets = 1
Weather = 1
Badge = 1
Stab = 1.5
type = 0.5
burn = 1
rand = random.uniform(0.85,1)
Critical = 1

Modifier = Targets * Weather * Badge * Critical * random.uniform(0.85,1.00) * Stab * type 

Damage = ((((((2 * Charizard_lvl)/5)+2)*Pow*Charizard_Atk/Feraligatr_Def)/50)+2) * Modifier 






print("Charizards's attack damage: ",Damage)
