class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola meu nome e {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 69

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_pai = super().cumprimentar()
        return f'{cumprimentar_da_classe_pai}. Aperto de mao!'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    raphael = Mutante(nome='Raphael')
    ronaldo = Homem(raphael, nome='Ronaldo')
    print(Pessoa.cumprimentar(ronaldo))
    print(id(ronaldo))
    print(ronaldo.cumprimentar())
    print(ronaldo.nome)
    print(ronaldo.idade)
    print(ronaldo.filhos)
    for filho in ronaldo.filhos:
        print(filho.nome)
    ronaldo.sobrenome = 'Nogueira'
    ronaldo.idade = 57
    del raphael.filhos
    print(ronaldo.sobrenome)
    raphael.olhos = 1
    del raphael.olhos
    print(ronaldo.__dict__)
    print(raphael.__dict__)
    print(Pessoa.olhos)
    print(raphael.olhos)
    print(ronaldo.olhos)
    print(id(Pessoa.olhos), id(raphael.olhos), id(ronaldo.olhos))
    print(Pessoa.metodo_estatico(), raphael.metodo_estatico(), ronaldo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), raphael.nome_e_atributos_de_classe(),
          ronaldo.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(raphael, Pessoa))
    print(isinstance(raphael, Homem))
    print(raphael.cumprimentar())
    print(ronaldo.cumprimentar())
