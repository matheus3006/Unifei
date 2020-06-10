class Musica:
    #Construtor
    def __init__(self, titulo, artista, album, nroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album 
        self.__nroFaixa = nroFaixa

        artista.addMusica(self)

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    def getAlbum(self):
        return self.__album

    def getNroFaixa(self):
        return self.__nroFaixa
    
class Album:
    #Construtor
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__ano = ano
        self.__artista = artista

        #Isto se torna uma agregação
        self.__Faixas = []

        artista.addAlbum(self)

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista
    
    def getAno(self):
        return self.__ano
    
    def getFaixas(self):
        return self.__Faixas

    def addFaixa(self, titulo, artista = None):
        #Quando tem none significa que é opcional passar o artista por parametro ou não
        #Se não tiver esse parametro ai pega o artista da faixa mesmo 
        if artista is None:
            artista = self.__artista
        nroFaixa = len(self.__Faixas)
        musica = Musica(titulo, artista, self, nroFaixa)
        self.__Faixas.append(musica)

class Artista:
    #Construtor
    def __init__(self, nome):
        self.__nome = nome

        #O artista possui uma lista de albuns e de musicas
        self.__albuns = []
        self.__musicas = []

    def getNome(self):
        return self.__nome
    
    def getAlbum(self):
        return self.__albuns
    
    def getMusicas(self):
        return self.__musicas
    
    def addAlbum(self, album):
        self.__albuns.append(album)
    
    def addMusica(self, musica):
        self.__musicas.append(musica)
    
class Playlist:
    #Construtor
    def __init__(self, nome):
        self.__nome = nome

        #Isto se torna uma agregação
        self.__musicas = []

    def getNome(self):
        return self.__nome
    
    def getMusicas(self):
        return self.__musicas

    def addMusica(self, musica):
        self.__musicas.append(musica)
    
art1 = Artista('Projota')
art2 = Artista('Anitta')
album1 = Album('Não há lugar no mundo melhor do que nosso lar', art1, 2011)
album1.addFaixa('As vezes')
album1.addFaixa("3 F's")
album1.addFaixa('Faz parte', art2)

musica1 = Musica('As vezes', art1, album1, 1)
musica2 = Musica("3 F's", art1, album1, 1)
musica3 = Musica('Faz parte', art1, album1, 1)

play1 = Playlist('Raps')

for musica in album1.getFaixas():
    play1.addMusica(musica)

print('Estas são as músicas presentes na playlist "{}"'.format(play1.getNome()))
for musica in play1.getMusicas():
    print(musica.getTitulo())

print('\nEste é o nome do album do artista {}'.format(art1.getNome()))
print(album1.getTitulo())

print('\nNa música "{}", do album "{}", a artista {} fez fez uma participação especial ao lado de {}.'
.format(musica3.getTitulo(), album1.getTitulo(), art2.getNome(), art1.getNome()))