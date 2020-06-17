#Criando nossas exceptions
class titulacaoNaoEDoutor(Exception):
    pass

class idadeInvalidaProfessor(Exception):
    pass

class cursoInvalido(Exception):
    pass

class idadeInvalidaAluno(Exception):
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

#Lista que irá armazenar os professores
ListaProfessores = []

#Lista que irá armazenar os alunos
ListaAlunos = []

#Criando professores teste
p1 = Professor('Adalberto', 30, 'Itajubá, Av. BPS, n° 32', '123.456.789-12', 'Doutor')
p2 = Professor('Francisco', 25, 'Itajubá, Av. BPS, n° 54', '987.654.321-34', 'Doutor')
p3 = Professor('Jonas', 33, 'Itajubá, Rua Tatuí, n° 79', '123.456.789-12', 'Doutor')
p4 = Professor('Diomedes', 35, 'Itajubá, Av. BPS, n° 167', '234.567.891-56', 'Mestre')
p5 = Professor('Thomas', 34, 'Delfim Moreira, Rua Juscelino Kubitscheck, n° 15', '345.678.912-78', 'Licenciado')

#Adicionando os professores teste à lista de professores
ListaProfessores.append(p1)
ListaProfessores.append(p2)
ListaProfessores.append(p3)
ListaProfessores.append(p4)
ListaProfessores.append(p5)

#Criando alunos teste
a1 = Aluno('Jonathan', 18, 'Delfim Moreira, Rua Jacinto Pinto, n° 17', '312.645.978-90', 'CCO')
a2 = Aluno('Jeorgina', 19, 'Paraisópolis, Rua Thomas Turbando, n° 39', '321.432.543-65', 'SIN')
a3 = Aluno('Ginecleusa', 18, 'Rio de Janeiro, Rua Cruz Credo, n° 356', '789.678.567-25', 'ECO')
a4 = Aluno('Pigmeu', 24, 'Delfim Moreira, Rua Sem Saída, n° 69', '789.678.567-25', 'CCO')
a5 = Aluno('Vasconcelos', 15, 'Itajubá, Rua Tadeu e Tadano, S/N', '108.605.274-94', 'SIN')

#Adicionando os alunos teste à lista de alunos
ListaAlunos.append(a1)
ListaAlunos.append(a2)
ListaAlunos.append(a3)
ListaAlunos.append(a4)
ListaAlunos.append(a5)

#Criando um cadastro com professores e alunos
CadastroProfessores = []
CadastroAlunos = []

#Tratando as exceções para com os professores
print('Cadastrando professores...')
for prof in ListaProfessores:
    try:
        if prof.getTitulacao() != 'Doutor':
            raise titulacaoNaoEDoutor()
        if prof.getIdade() < 30:
            raise idadeInvalidaProfessor()
        if prof.getCpf() in CadastroProfessores:
            raise cpfDuplicado()
    except titulacaoNaoEDoutor:
        print("O professor {} não é doutor, é {}".format(prof.getNome(), prof.getTitulacao()))
    except idadeInvalidaProfessor:
        print("O professor {} não tem idade permitida! -> {} < 30 anos".format(prof.getNome(), prof.getIdade()))
    except:
        print('O CPF do professor %s já pertence a outra pessoa!' % prof.getNome())
    #Se não houver invalidações, o professor é adicionado à lista Juntos
    else:
        CadastroProfessores.append(prof)

print()

#Tratando as exceções para com os alunos
print('Cadastrando alunos...')
for aluno in ListaAlunos:
    try:
        if aluno.getCurso() != 'CCO' and aluno.getCurso() != 'SIN':
            raise cursoInvalido()
        if aluno.getIdade() < 18:
            raise idadeInvalidaAluno()
        if aluno.getCpf() in CadastroAlunos:
            raise cpfDuplicado()
    except cursoInvalido:
        print("O aluno %s não possui um curso permitido" % aluno.getNome())
    except idadeInvalidaAluno:
        print("O aluno {} não tem idade permitida! -> {} < 18 anos".format(aluno.getNome(), aluno.getIdade()))
    except cpfDuplicado:
        print('O CPF do aluno %s já pertence a outra pessoa!' % aluno.getNome())
    #Se não houver invalidações, o aluno é adicionado à lista Juntos
    else:
        CadastroAlunos.append(aluno)

print()

#Printando a lista de pessoas cadastradas
print("Estes são os professores cadastrados:")
for prof in CadastroProfessores:
    prof.printDescricao()

print("\nEstes são os alunos cadastrados:")
for aluno in CadastroAlunos:
    aluno.printDescricao()