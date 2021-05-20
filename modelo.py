class programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano 
        self._like = 0

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome.title()

class filme(programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} - {self._like}'

class serie(programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} - {self._like}'

class playlist:
    def __init__(self, nomes, programas):
        self.nomes = nomes
        self._programas = programas
        
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem (self):
        return  self._programas

    def __len__ (self):
        return len(self._programas)

vingadores = filme('vingadores - guerra infinita', 2018, 160)
tmep = filme('Todo Mundo em Pânico', 1999, 100)
demolidor = serie('Demolidor', 2016, 2)
atlanta = serie('atlanta', 2018, 2)

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
fim_de_semana = playlist('fim de semana', filmes_e_series)
print(f'Tamanho da playlist: {len(fim_de_semana)}')
for programa in fim_de_semana:
        print(programa)
