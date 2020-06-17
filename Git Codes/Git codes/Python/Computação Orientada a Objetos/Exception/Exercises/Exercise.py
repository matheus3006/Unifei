#Definir nossas exceptions

class UsernameDuplicado(Exception):
    pass

class IdadeInvalida(Exception):
    pass

class IdadeMenorQuePermitida(Exception):
    pass

class EmailInvalido(Exception):
    pass

#Classe para conter os dados dos usuários

class User:

    def __init__(self, username, email):
        self.__username = username
        self.__email = email

    def getUsername(self):
        return self.__username
    
    def getEmail(self):
        return self.__email
    
listaExemplo = [
    ("Paulo", "paulo@gmail.com", 21),
    ("maria", "maria@gmail.com", 19),
    ("Antonio", "antonio@gmail.com", 25),
    ("Pedro", "pedro@gmail.com", 15),
    ("Marisa", "marisa", 23),
    ("Ana", "ana@gmail.com", -3),
    ("Maria", "maria@gmail.com", 27)
]

cadastro = {}

for username, email, idade in listaExemplo:
    try:
        if username in cadastro:
            raise UsernameDuplicado()
        if idade < 0:
            raise IdadeInvalida()
        if idade < 18:
            raise IdadeMenorQuePermitida()

        emailPartes = email.split('@')
        if len(emailPartes) != 2 or not emailPartes[1]:
            raise EmailInvalido()

    except UsernameDuplicado:
        print("Username '%s' ja esta em uso" % username)
    except IdadeInvalida:
        print("Idade invalida: %d" % idade)
    except IdadeMenorQuePermitida:
        print("Usuario %s tem idade inferior a permitida" % username)
    except EmailInvalido:
        print("'%s' nao eh um endereco de email valido" % email)

    else:
        cadastro[username] = User(username, email)