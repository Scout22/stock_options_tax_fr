

def compute_tax(aquisition_price, percentage_off, exercise_price, sell_price, volume):
    if percentage_off>0.05:
        rabais_excedentaire = aquisition_price*(percentage_off-0.05)
    else:
        rabais_excedentaire = 0

    gain_de_levee = 0.497*max(exercise_price-aquisition_price*(1+percentage_off), 0)
    gain_de_vente = 0.30*max(sell_price-exercise_price, 0)

    return volume*(rabais_excedentaire+gain_de_levee+gain_de_vente)


def compute_gain(aquisition_price, percentage_off, exercise_price, sell_price, volume):
    return 1650*(sell_price-aquisition_price)-compute_tax(aquisition_price, percentage_off, exercise_price, sell_price, volume)

print(compute_gain(1.25,0.20,1.25,4.80,1650))
