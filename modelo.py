class Filmes:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__like = 0

    def dar_like(self):
        self.__like += 1


class Series:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__like = 0

    def dar_like(self):
        self.__like += 1


vingadores = Filmes("Vingadores - Guerra infitina", 2018, 160)

atlanta = Series("Atlanta", 2018, 2)

vingadores.dar_like()

atlanta.dar_like()
atlanta.dar_like()

print(f'Nome: {vingadores.__nome}, Ano: {vingadores.ano}, Temporadas: {vingadores.duracao}, Likes: {vingadores.__like}')
print(f'Nome: {atlanta.__nome}, Ano: {atlanta.ano}, Temporadas: {atlanta.temporadas}, Likes: {atlanta.__like}')
