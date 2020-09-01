class Pessoa:
    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    raphael = Pessoa(nome='Raphael')
    ronaldo = Pessoa(raphael, nome='Ronaldo')
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
    print(ronaldo.__dict__)
    print(raphael.__dict__)
