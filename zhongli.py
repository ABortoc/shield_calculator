from math import floor

def zhongli_shield(hp, talent_level):
    if talent_level == 1:
        shield_base_zhongli = hp * 0.128 + 1232
    elif talent_level == 2:
        shield_base_zhongli = hp * 0.138 + 1356
    elif talent_level == 3:
        shield_base_zhongli = hp * 0.148 + 1489
    elif talent_level == 4:
        shield_base_zhongli = hp * 0.16 + 1633
    elif talent_level == 5:
        shield_base_zhongli = hp * 0.17 + 1787
    elif talent_level == 6:
        shield_base_zhongli = hp * 0.179 + 1951
    elif talent_level == 7:
        shield_base_zhongli = hp * 0.192 + 2126
    elif talent_level == 8:
        shield_base_zhongli = hp * 0.205 + 2311
    elif talent_level == 9:
        shield_base_zhongli = hp * 0.218 + 2506
    elif talent_level == 10:
        shield_base_zhongli = hp * 0.23 + 2712
    elif talent_level == 11:
        shield_base_zhongli = hp * 0.243 + 2927
    elif talent_level == 12:
        shield_base_zhongli = hp * 0.256 + 3153
    elif talent_level == 13:
        shield_base_zhongli = hp * 0.272 + 3389
    else:
        return
    
    shield_effect_zhongli = shield_base_zhongli * 1.5
    return floor(shield_effect_zhongli)