class Professor:
    #Construtor
    def __init__(self, nome, sexo, estado, CorrigirTarefaDireito, Consequencia):
        self.__nome = nome
        self.__sexo = sexo
        self.__estado = estado
        self.__CorrigirTarefaDireito = CorrigirTarefaDireito
        self.__Consequencia = Consequencia

    def getNome(self):
        return self.__nome
    
    def getSexo(self):
        return self.__sexo
    
    def getEstado(self):
        return self.__estado
    
    def isTarefaCorrigidaDireito(self):
        return self.__CorrigirTarefaDireito
    
    def getConsequencia(self):
        return self.__Consequencia
    
    #Métodos de instância
    def CorrigirTarefa(self):
        if(self.isTarefaCorrigidaDireito()):
            print('A tarefa já foi corrigida corretamente!')
        else:
            self.__CorrigirTarefaDireito = True
            print('A tarefa acabou de ser corrigida corretamente!')
    
    def aplicarConsequencia(self):
        if(self.getConsequencia()):
            if(self.isTarefaCorrigidaDireito()):
                print("""Em razão da tarefa ter sido corrigida corretamente, {} foi premiado(a) como melhor do mês!
                """.format(self.getNome()))
            else:
                print("""Em razão da tarefa ter sido mal corrigida, {} foi punido(a) como lixo do mês!
                """.format(self.getNome()))
        else:
            if(self.isTarefaCorrigidaDireito()):
                print("""A tarefa foi corrigida corretamente, mas {} não foi premiado(a) pois o professor
Adler fez melhor... que azar!
                """.format(self.getNome()))
            else:
                print("""A tarefa foi mal corrigida, mas {} não foi punido(a) pois o professor Ramos cometeu um
erro maior e foi considerado o lixo do mês! Que sorte!
                """.format(self.getNome()))
    
    def showEstado(self):
        if self.__sexo == 'feminino':
            print("""A professora {} corrigiu as tarefas e está {}.""".format(self.getNome(), self.getEstado()))
        else:
            print("""O professor {} corrigiu as tarefas e está {}.""".format(self.getNome(), self.getEstado()))
            
    
Elisa = Professor('Elisa', 'feminino', 'confiante', False, True)
Elisa.showEstado()
print('E estes são os resultados:')
Elisa.aplicarConsequencia()
print('Porém, {} se redimiu e tentou corrigir as tarefas novamente:'.format(Elisa.getNome()))
Elisa.CorrigirTarefa()
print('\n')

Crystianne = Professor('Crystianne', 'feminino', 'ansiosa', True, True)
Crystianne.showEstado()
print('E estes são os resultados:')
Crystianne.aplicarConsequencia()

Ramos = Professor('Ramos', 'masculino', 'apavorado', True, False)
Ramos.showEstado()
print('E estes são os resultados:')
Ramos.aplicarConsequencia()

Baldochi = Professor('Baldochi', 'masculino', 'com medo', False, False)
Baldochi.showEstado()
print('E estes são os resultados:')
Baldochi.aplicarConsequencia()
print('Porém, {} se arrependeu e tentou corrigir as tarefas novamente:'.format(Baldochi.getNome()))
Baldochi.CorrigirTarefa()