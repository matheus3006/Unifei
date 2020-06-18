#Criando nossas exceptions
class titulacaoNaoEDoutor(Exception):
    pass

class idadeMenorQuePermitida(Exception):
    pass

class cursoInvalido(Exception):
    pass

class cpfDuplicado(Exception):
    pass


from abc import ABC, abstractmethod

class Pessoa(ABC):
    #Construtor 
    def __init__(self, nome, idade, endereco, cpf):
        self.__nome = nome
        self.__idade = idade 
        self.__endereco = endereco
        self.__cpf = cpf

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def getEndereco(self):
        return self.__endereco

    def getCpf(self):
        return self.__cpf
    
    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    #Construtor
    def __init__(self, nome, idade, endereco, cpf, titulacao):
        #Chama contrutor da super classe
        super().__init__(nome, idade, endereco, cpf)
        self.__titulacao = titulacao
    
    def getTitulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        print("""Professor: {}
        Idade: {}
        Titulação: {}
        Endereço: {}
        cpf: {}
        """.format(self.getNome(),self.getIdade(), self.getTitulacao(), self.getEndereco(), self.getCpf()))

class Aluno(Pessoa):
    #Construtor
    def __init__(self, nome, idade, endereco, cpf, curso):
        #Chama construtor da super classe
        super().__init__(nome, idade, endereco, cpf)
        self.__curso = curso
    
    def getCurso(self):
        return self.__curso
    
    def printDescricao(self):
        print("""Aluno: {}
        Idade: {}
        Curso: {}
        Endereço: {}
        cpf: {}
        """.format(self.getNome(),self.getIdade(), self.getCurso(), self.getEndereco(), self.getCpf()))

#Criando professores teste
#Lista de professores
Professores = [
("Adalberto", 30, "Itajubá, Av. BPS, n° 32", "123.456.789-12", "Doutor"),
("Francisco", 25, "Itajubá, Av. BPS, n° 54", "987.654.321-34", "Doutor"),
("Jonas", 33, "Itajubá, Rua Tatuí, n° 79", "123.456.789-12", "Doutor"),
("Diomedes", 35, "Itajubá, Av. BPS, n° 167", "234.567.891-56", "Mestre"),
("Thomas", 34, "Delfim Moreira, Rua Juscelino Kubitscheck, n° 15", "345.678.912-78", "Licenciado"),
("Diovania", 24, "Itajubá, Av. BPS, n° 226", "234.567.891-56", "Mestre"),
("Claudemir", 30, "Goiânia, Av. Isadora Pinto, n° 69", "105.903.274-94", "Doutor"),
("Valesca", 39, "Itu, Av. Chora Viola, n° 233", "102.475.376-26", "Doutor"),
("Bruna", 32, "Fernandópolis, Rua Cruz Credo, n° 666", "836.452.474-45", "Doutor")
]


#Criando alunos teste
#Lista de alunos
Alunos = [
("Jonathan", 18, "Delfim Moreira, Rua Jacinto Pinto, n° 17", "312.645.978-90", "CCO"),
("Jeorgina", 19, "Paraisópolis, Rua Thomas Turbando, n° 39", "321.432.543-65", "SIN"),
("Ginecleusa", 18, "Rio de Janeiro, Rua Cruz Credo, n° 356", "789.678.567-25", "SIN"),
("Pigmeu", 24, "Delfim Moreira, Rua Sem Saída, n° 69", "789.678.567-25", "CCO"),
("Vasconcelos", 15, "Itajubá, Rua Tadeu e Tadano, S/N", "108.605.274-94", "SIN"),
("Clóvis", 19, "Divinópolis, Rua da Macumba, 666", "109.645.294-44", "SIN"),
("Felícia", 27, "Campos de Jordão, Rua Quase Lá, n° 70", "790.674.537-65", "CCO"),
("Pitolomeu", 26, "Delfim Moreira, Rua Nem te Conto, n° 60", "789.638.565-25", "CCO"),
("Bartolomeu", 24, "Delfim Moreira, Rua Tilambucano, n° 24", "784.348.567-25", "SIN"),
("Pigméia", 17, "Delfim Moreira, Rua Sem Saída, n° 63", "759.675.587-46", "CCO"),
("Olívio", 24, "Delfim Moreira, Sai pra Lá, n° 25", "789.678.567-25", "CCO"),
("Fernandete", 24, "Delfim Moreira, Rua Sem Saída, n° 38", "770.678.567-45", "EEL")
]

#Lista de cadastro
Cadastro = {}

#Exceptions para professores
print('Cadastrando professores...')
for nome, idade, endereco, cpf, titulacao in Professores:
    try:
        if cpf in Cadastro:
            raise cpfDuplicado()
        if idade < 30:
            raise idadeMenorQuePermitida()
        if titulacao != 'Doutor':
            raise titulacaoNaoEDoutor()
    except cpfDuplicado:
        print('O CPF {} em posse do(a) professor(a) {} já está sendo usado por outra pessoa! - Cadastro não permitido'.format(cpf, nome))
    except idadeMenorQuePermitida:
        print('O(A) professor(a) {} possui idade inferior à permitida -> {} < 30 anos - Cadastro não permitido'. format(nome, idade))
    except titulacaoNaoEDoutor:
        print('O(A) professor(a) {} não é doutor(a), é {} -> Cadastro não permitido'.format(nome, titulacao))
    #Se atender a todos os critérios, o professor é cadastrado com sucesso
    else:
        pessoa = Professor(nome, idade, endereco, cpf, titulacao)
        Cadastro[cpf] = pessoa
        print("\nProfessor(a) {} cadastrado com sucesso!".format(nome))
        pessoa.printDescricao()
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------')
#Exceptions para alunos
print('Cadastrando alunos...')
for nome, idade, endereco, cpf, curso in Alunos:
    try:
        if cpf in Cadastro:
            raise cpfDuplicado()
        if idade < 18:
            raise idadeMenorQuePermitida()
        if curso != 'CCO' and curso != 'SIN':
            raise cursoInvalido()
    except cpfDuplicado:
        print('O CPF {} em posse do(a) aluno(a) {} já está sendo usado por outra pessoa! - Cadastro não permitido'.format(cpf, nome))
    except idadeMenorQuePermitida:
        print('O(A) aluno(a) {} possui idade inferior à permitida -> {} < 18 anos - Cadastro não permitido'. format(nome, idade))
    except cursoInvalido:
        print('O(A) aluno(a) {} não cursa CCO e nem SIN, cursa {} -> Cadastro não permitido'.format(nome, curso))
    #Se atender a todos os critérios, o aluno é cadastrado com sucesso
    else:
        pessoa = Aluno(nome, idade, endereco, cpf, curso)
        Cadastro[cpf] = pessoa
        print("\nAluno(a) {} cadastrado com sucesso!".format(nome))
        pessoa.printDescricao()