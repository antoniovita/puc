def meioString (pal1, pal2):
    pal2Inicio = pal2[:int(len(pal2)/2)]
    pal2Final = pal2[int(len(pal2)/2):]
    strinFinal = pal2Inicio + pal1 + pal2Final
    return strinFinal

print(meioString("abcd", "abcd"))