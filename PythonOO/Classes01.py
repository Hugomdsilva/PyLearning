class Pessoa:
    def __init__(self, nome, idade):
        self.set_nome(nome)
        self.set_ender(idade)
    def set_nome(self,nome):
        self.nome=nome
    def set_ender(self, idade):
        self.idade=idade
    def get_nome(self):
        return self.nome
    def get_idade(self):
        return self.idade
    def imprimir(self):
        print(self.nome, 'tem', self.idade, 'ano(s)')


class Profissional(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao
    def imprimir(self):
        super().imprimir()
        print('\t e trabalha como', self.profissao)

p = Profissional('Hugo', 18, 'repositor')
p.imprimir()