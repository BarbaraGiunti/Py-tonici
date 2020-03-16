def turn_clockwise( old_card_dir ) :
    if old_card_dir == 'N' :
        return 'E'
    if old_card_dir == 'S' :
        return 'W'
    if old_card_dir == 'W' :
        return 'N'
    if old_card_dir == 'E' :
        return 'S'
    return None

print( turn_clockwise("N") == "E" )
print( turn_clockwise("W") == "N" )