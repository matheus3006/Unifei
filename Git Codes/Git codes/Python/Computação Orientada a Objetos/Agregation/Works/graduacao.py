#Informar:
#carga horária total das disciplinas obrigatórias cursadas;
#carga horária total das disciplinas eletivas cursadas.

class Disciplina:
    #Construtor
    def __init__(self, codigo, nome, cargaHoraria):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome
    
    def getCargaHoraria(self):
        return self.__cargaHoraria
    
class Grade: 
    #Construtor
    def __init__(self, ano):
        self.__ano = ano
    
        #A grade é composta por uma lista de disciplinas
        #Isto se torna uma agregação
        self.__disciplinas = []

    def getAno(self):
        return self.__ano
    
    def getDisciplina(self):
        return self.__disciplinas
    
    def addDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)
    
class Curso:
    #Construtor
    def __init__(self, nome, grade):
        self.__nome = nome 
        #Cada curso possui exatamente uma grade
        #Então criei uma lista para se adicionar somente uma grade
        #Isto se torna uma composição
        self.__grade = []

    def getNome(self):
        return self.__nome
    
    def getGrade(self):
        return self.__grade
    
    def addGrade(self, grade):
        #Aqui, uma grade será adicionada ao curso
        #NÃO SE DEVE ADICIONAR MAIS DE UMA GRADE A ESTA LISTA
        self.__grade.append(grade)
    
class Aluno:
    #Construtor
    def __init__(self, nome, nroMatric, curso):
        self.__nome = nome
        self.__nroMatric = nroMatric
        self.__curso = curso

        #O aluno possui uma lista com os cursos cujas disciplinas ele cursa
        #E uma lista para seu histórico de cursos
        self.__disciplinasObrigatorias = []
        self.__disciplinasEletivas = []
        self.__historico = []

    def getNome(self):
        return self.__nome

    def getNroMatric(self):
        return self.__nroMatric
    
    def getCurso(self):
        return self.__curso
    
    def getDisciplinasObrigatorias(self):
        return self.__disciplinasObrigatorias
    
    def getDisciplinasEletivas(self):
        return self.__disciplinasEletivas
    
    def getHistorico(self):
        return self.__historico
    
    def addDisciplinaObrigatoria(self, disciplina):
        #Aqui, uma disciplina obrigatoria pode ser adicionada ao aluno
        self.__disciplinasObrigatorias.append(disciplina)
    
    def addDisciplinaEletiva(self, disciplina):
        #Aqui, uma disciplina eletiva pode ser adicionada ao aluno
        self.__disciplinasEletivas.append(disciplina)
    
    def addHistorico(self, historico):
        #Aqui um novo registro de historico pode ser adicionado ao aluno
        self.__historico.append(historico)
        
class Historico:
    #Construtor
    def __init__(self, aluno):
        self.__aluno = aluno

        #O histórico possui uma lista com as disciplinas cursadas pelo aluno
        self.__disciplinasObrigatorias = []
        self.__disciplinasEletivas = []
        self.__horasObrigatorias = 0
        self.__horasEletivas = 0

        #Sempre que uma nova disciplina for adicionado ao histórico
        #O aluno receberá esse novo histórico atualizado
        aluno.addHistorico(self)

    def getAluno(self):
        return self.__aluno
    
    def getDisciplinasObrigatorias(self):
        if len(self.__disciplinasObrigatorias) == 0:
            print('\n{} não ainda cursou disciplinas obrigatórias'.format(self.getAluno().getNome()))
        else:
            print('\nEstas são as disciplinas obrigatórias cursadas por {}'.format(self.getAluno().getNome()))
            for disciplina in self.__disciplinasObrigatorias:
                print('{} - Carga horária: {}'.format(disciplina.getNome(), disciplina.getCargaHoraria()))
    
    def getHorasObgt(self):
        if len(self.__disciplinasObrigatorias) == 0:
            print('{} não possui carga horária cadastrada para disciplinas obrigatórias'.format(self.getAluno().getNome()))
        else:
            print('Carga horária total: {}'.format(self.__horasObrigatorias))
            
    def getDisciplinasEletivas(self):
        if len(self.__disciplinasEletivas) == 0:
            print('\n{} ainda não cursou disciplinas eletivas'.format(self.getAluno().getNome()))
        else:
            print('\nEstas são as disciplinas eletivas cursadas por {}:'.format(self.getAluno().getNome()))
            for disciplina in self.__disciplinasEletivas:
                print('{} - Carga horária: {}'.format(disciplina.getNome(), disciplina.getCargaHoraria()))
    
    def getHorasEltv(self):
        if len(self.__disciplinasEletivas) == 0:
            print('{} não possui carga horária cadastrada para disciplinas eletivas'.format(self.getAluno().getNome()))
        else:
            print('Carga horária total: {}'.format(self.__horasEletivas))
    
    def addDisciplinaObrigatoria(self, disciplina):
        self.__horasObrigatorias += disciplina.getCargaHoraria()
        self.__disciplinasObrigatorias.append(disciplina)
    
    def addDisciplinaEletiva(self, disciplina):
        self.__horasEletivas += disciplina.getCargaHoraria()
        self.__disciplinasEletivas.append(disciplina)
    

#----------------------------------- PRIMEIRA GRADE DE TESTE ------------------------------------------------------#
#Criando possíveis disciplinas para a primeira grade de teste
Disc1 = Disciplina('COM112.1', 'ALGORITMO E ESTRUTURA DE DADOS II', 80)
Disc2 = Disciplina('COM311', 'ANÁLISE DE INVESTIMENTO EM INFORMÁTICA', 48)
Disc3 = Disciplina('COM220.1', 'COMPUTAÇÃO ORIENTADA A OBJETOS I', 64)
Disc4 = Disciplina('SIN311', 'CONTABILIDADE EM INFORMÁTICA', 64)
Disc5 = Disciplina('COM210.1', 'ENGENHARIA DE SOFTWARE I', 80)
Disc6 = Disciplina('MAT017', 'FUNDAMENTOS DE LÓGICA E MATEMÁTICA DISCRETA', 64)

#Criando a primeira grade de teste
grade1 = Grade(2020.1)

#Adicionando as diciplinas a primeira grade de teste
grade1.addDisciplina(Disc1)
grade1.addDisciplina(Disc2)
grade1.addDisciplina(Disc3)
grade1.addDisciplina(Disc4)
grade1.addDisciplina(Disc5)
grade1.addDisciplina(Disc6)

#Criando o primeiro curso de teste adaptado à primeira grade de teste
curso1 = Curso('Sistemas de informação', grade1)
#------------------------------------------------- FIM -----------------------------------------------------------#

#----------------------------------- SEGUNDA GRADE DE TESTE ------------------------------------------------------#
#Criando possíveis disciplinas para a segunda grade de teste
Disc7 = Disciplina('EEL301', 'ELETROTÉCNICA GERAL I', 64)
Disc8 = Disciplina('ELT303', 'ELETRÔNICA ANALÓGICA I', 64)
Disc9 = Disciplina('ELT313', 'LABORATÓRIO DE ELETRÔNICA ANALÓGICA I', 16)
Disc10 = Disciplina('EME311', 'MECÂNICA DOS SÓLIDOS', 64)
Disc11 = Disciplina('MAT003', 'CÁLCULO III', 64)
Disc12 = Disciplina('MAT021', 'EQUACOES DIFERENCIAIS I', 64)

#Criando a segunda grade de teste
grade2 = Grade(2020.1)

#Adicionando as diciplinas a segunda grade de teste
grade2.addDisciplina(Disc7)
grade2.addDisciplina(Disc8)
grade2.addDisciplina(Disc9)
grade2.addDisciplina(Disc10)
grade2.addDisciplina(Disc11)
grade2.addDisciplina(Disc12)

#Criando o segundo curso de teste adaptado à segunda grade de teste
curso2 = Curso('Engenharia Elétrica', grade2)
#------------------------------------------------- FIM -----------------------------------------------------------#

#-------------------------------------------- PRIMEIRO ALUNO -----------------------------------------------------#
#Criando o primeiro aluno, que cursa o primeiro curso de teste
aluno1 = Aluno('João Lucas Ribeiro', 2019005856, curso1)

#Adicionando as disciplinas do curso 1 à lista de disciplinas do aluno
for disciplina in grade1.getDisciplina():
    aluno1.addDisciplinaObrigatoria(disciplina)

#Adicionando disciplinas do curso 2 ao primeiro aluno
aluno1.addDisciplinaEletiva(Disc8)
aluno1.addDisciplinaEletiva(Disc10)

#Criando o histórico do primeiro aluno e adicionando as informações
histAluno1 = Historico(aluno1)
for disciplina in aluno1.getDisciplinasObrigatorias():
    histAluno1.addDisciplinaObrigatoria(disciplina)

for disciplina in aluno1.getDisciplinasEletivas():
    histAluno1.addDisciplinaEletiva(disciplina)
#------------------------------------------------- FIM -----------------------------------------------------------#

#-------------------------------------------- SEGUNDO ALUNO ------------------------------------------------------#
#Criando o segundo aluno, que cursa o segundo curso de teste
aluno2 = Aluno('Robson de Arruda Silva Souza', 2019013624, curso2)

#Adicionando as disciplinas do curso 2 à lista de disciplinas do aluno
for disciplina in grade2.getDisciplina():
    aluno2.addDisciplinaObrigatoria(disciplina)

#Adicionando disciplinas do curso 1 ao segundo aluno
aluno2.addDisciplinaEletiva(Disc5)
aluno2.addDisciplinaEletiva(Disc2)

#Criando o histórico do segundo aluno e adicionando as informações
histAluno2 = Historico(aluno2)
for disciplina in aluno2.getDisciplinasObrigatorias():
    histAluno2.addDisciplinaObrigatoria(disciplina)

for disciplina in aluno2.getDisciplinasEletivas():
    histAluno2.addDisciplinaEletiva(disciplina)
#------------------------------------------------- FIM -----------------------------------------------------------#

#-------------------------------------------- TERCEIRO ALUNO -----------------------------------------------------#
#Criando o terceiro aluno, que cursa o primeiro curso de teste
aluno3 = Aluno('Rodrigo Duarte Silva Luz', 2020003520, curso1)

#Este aluno acabou de entrar, então, ainda não cursou nenhuma disciplina

#Criando o histórico do terceiro aluno e adicionando as informações
histAluno3 = Historico(aluno3)
#------------------------------------------------- FIM -----------------------------------------------------------#

#-------------------------------------------- QUARTO ALUNO -------------------------------------------------------#
#Criando o quarto aluno, que cursa o segundo curso de teste
aluno4 = Aluno('Matheus de Souza Silva', 2019005909, curso2)

#Adicionando as disciplinas do curso 2 à lista de disciplinas do aluno
for disciplina in grade2.getDisciplina():
    aluno4.addDisciplinaObrigatoria(disciplina)

#Este aluno não quis cursar disciplinas da grade de outro curso

#Criando o histórico do quarto aluno e adicionando as informações
histAluno4 = Historico(aluno4)
for disciplina in aluno4.getDisciplinasObrigatorias():
    histAluno4.addDisciplinaObrigatoria(disciplina)
#------------------------------------------------- FIM ----------------------------------------------------------#

#-------------------------------------------- QUINTO ALUNO ------------------------------------------------------#
#Criando o quinto aluno, que cursa o segundo curso de teste
aluno5 = Aluno('Carlos Henrique Souza Silva', 2019015979, curso2)

#Adicionando as disciplinas do curso 2 à lista de disciplinas do aluno
for disciplina in grade2.getDisciplina():
    aluno5.addDisciplinaObrigatoria(disciplina)

#Adicionando disciplinas do curso 1 ao quinto aluno
aluno5.addDisciplinaEletiva(Disc4)
aluno5.addDisciplinaEletiva(Disc3)
aluno5.addDisciplinaEletiva(Disc1)

#Criando o histórico do quinto aluno e adicionando as informações
histAluno5 = Historico(aluno5)
for disciplina in aluno5.getDisciplinasObrigatorias():
    histAluno5.addDisciplinaObrigatoria(disciplina)

for disciplina in aluno5.getDisciplinasEletivas():
    histAluno5.addDisciplinaEletiva(disciplina)
#------------------------------------------------- FIM ----------------------------------------------------------#


#--------------------------------- PROCESSANDO AS INFORMAÇÕES E PRINTANDO ----------------------------------------#
#Processando  o histórico e exibindo as disciplinas obrigatórias e eletivas do primeiro aluno
#Juntamente com a carga horária total
print("""Acessando histórico dos alunos... Encontrado!\n 
Aluno: {}
Matrícula: {} 
Curso: {}""".format(aluno1.getNome(), aluno1.getNroMatric(), aluno1.getCurso().getNome()))
histAluno1.getDisciplinasObrigatorias()
histAluno1.getHorasObgt()
histAluno1.getDisciplinasEletivas()
histAluno1.getHorasEltv()

print('-----------------------------------------------------------------------------------------------------------')

#Processando o histórico e exibindo as disciplinas obrigatórias e eletivas do segundo aluno
#Juntamente com a carga horária total
print("""Aluno: {}
Matrícula: {} 
Curso: {}""".format(aluno2.getNome(), aluno2.getNroMatric(), aluno2.getCurso().getNome()))
histAluno2.getDisciplinasObrigatorias()
histAluno2.getHorasObgt()
histAluno2.getDisciplinasEletivas()
histAluno2.getHorasEltv()

print('-----------------------------------------------------------------------------------------------------------')

#Processando o histórico e exibindo as disciplinas obrigatórias e eletivas do terceiro aluno
#Juntamente com a carga horária total
print("""Aluno: {}
Matrícula: {} 
Curso: {}""".format(aluno3.getNome(), aluno3.getNroMatric(), aluno3.getCurso().getNome()))
histAluno3.getDisciplinasObrigatorias()
histAluno3.getHorasObgt()
histAluno3.getDisciplinasEletivas()
histAluno3.getHorasEltv()

print('-----------------------------------------------------------------------------------------------------------')

#Processando o histórico e exibindo as disciplinas obrigatórias e eletivas do quarto aluno
#Juntamente com a carga horária total
print("""Aluno: {}
Matrícula: {} 
Curso: {}""".format(aluno4.getNome(), aluno4.getNroMatric(), aluno4.getCurso().getNome()))
histAluno4.getDisciplinasObrigatorias()
histAluno4.getHorasObgt()
histAluno4.getDisciplinasEletivas()
histAluno4.getHorasEltv()

print('-----------------------------------------------------------------------------------------------------------')

#Processando o histórico e exibindo as disciplinas obrigatórias e eletivas do quinto aluno
#Juntamente com a carga horária total
print("""Aluno: {}
Matrícula: {} 
Curso: {}""".format(aluno5.getNome(), aluno5.getNroMatric(), aluno5.getCurso().getNome()))
histAluno5.getDisciplinasObrigatorias()
histAluno5.getHorasObgt()
histAluno5.getDisciplinasEletivas()
histAluno5.getHorasEltv()

print('-----------------------------------------------------------------------------------------------------------')
#------------------------------------------------- FIM ------------------------------------------------------- ---#