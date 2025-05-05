def validaSenha(senha):
    nums = []
    Capital = []
    Lower = []

    for char in senha:
        if char.isdigit():
            nums.append(char)
        elif char.isupper():
            Capital.append(char)
        elif char.islower():
            Lower.append(char)

    if len(nums) == 0 or len(Capital) == 0 or len(Lower) == 0 or len(senha) < 8:
        return False
    return True
    
print(validaSenha("Senha1234"))