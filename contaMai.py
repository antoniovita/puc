def contaMai(s):
    if s == "":
        return 0
    if s[0] >= "A" and s[0] <= "Z":
        return 1 + contaMai(s[1:])
    else:
        return contaMai(s[1:])

#print(contaMai("AaAaa"))

def exibaString (s):
    if s != "":
        print(s[0])
        exibaString(s[1:])

#exibaString("CARLOS")

def duplicaString(s):
    if s == "":
        return ""
    return s[0] * 2 + duplicaString(s[1:])

#print(duplicaString("antonio"))

def duplicavogais (s):
    if s == "":
        return ""
    if s[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        return s[0] * 2 + duplicavogais(s[1:])
    else:
        return s[0] + duplicavogais(s[1:])
#print(duplicavogais("carro"))

def trocaPorA (s):
    if s == "":
        return ""
    if s[0] == " ":
        return "a" + trocaPorA(s[1:])
    else:
        return s[0] + trocaPorA(s[1:])
    
print(trocaPorA("gordo filho da puta"))
