from math import floor

def diona_shield(hp, talent_level, hold, constellation):
    if talent_level == 1:
        shield_base_diona = hp * 0.072 + 693
    elif talent_level == 2:
        shield_base_diona = hp * 0.077 + 762
    elif talent_level == 3:
        shield_base_diona = hp * 0.083 + 837
    elif talent_level == 4:
        shield_base_diona = hp * 0.09 + 918
    elif talent_level == 5:
        shield_base_diona = hp * 0.095 + 1005
    elif talent_level == 6:
        shield_base_diona = hp * 0.101 + 1097
    elif talent_level == 7:
        shield_base_diona = hp * 0.108 + 1195
    elif talent_level == 8:
        shield_base_diona = hp * 0.115 + 1299
    elif talent_level == 9:
        shield_base_diona = hp * 0.122 + 1409
    elif talent_level == 10:
        shield_base_diona = hp * 0.13 + 1524
    elif talent_level == 11:
        shield_base_diona = hp * 0.137 + 1646
    elif talent_level == 12:
        shield_base_diona = hp * 0.144 + 1773
    elif talent_level == 13:
        shield_base_diona = hp * 0.153 + 1905
    else:
        return
        
    if hold and constellation:
        shield_effect_diona = shield_base_diona * 1.75 * 1.15
    elif hold and not constellation:
        shield_effect_diona = shield_base_diona * 1.75
    elif not hold and constellation:
        shield_effect_diona = shield_base_diona * 1.15
    elif not hold and not constellation:
        shield_effect_diona = shield_base_diona
    else:
        return
    
    return floor(shield_effect_diona)