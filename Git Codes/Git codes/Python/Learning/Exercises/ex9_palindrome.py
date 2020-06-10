def palin(str):
    for i in range(0, int(len(str)/2)):
        if(str[i] != str[len(str) - i - 1]):
            return False
    return True

str = input('Digite uma string: ')

if(palin(str)):
    print(str + ' é um palindrome')
else:
    print(str + ' não é um palindrome')

