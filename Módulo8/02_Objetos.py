# Criando um novo tipo de objeto chamado Carro
class Carro(object):
    pass

# Instância do Carro
ferrari = Carro()

# Criando uma classe
class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

# Criando um objeto chamado Estudante1 a partir da classe Estudantes
Estudante1 = Estudantes("Bob", 12, 9.5)

# Criando uma classe
class Funcionarios:
    
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def listFunc(self):
        print("Funcionário(a) " + self.nome + " tem salário de R$" + str(self.salario) + " e o cargo é " + self.cargo)

# Criando um objeto chamado Func1 a partir da classe Funcionarios
Func1 = Funcionarios("Mary", 20000, "Cientista de Dados")
# Usando o método da classe
Func1.listFunc()

# Setter
setattr(Func1, "salario", 4500)

# Getter
getattr(Func1, "salario")