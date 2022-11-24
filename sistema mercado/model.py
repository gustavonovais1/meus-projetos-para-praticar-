class Pessoa:
    def __init__(self, nome, telefone, cpf):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf

class Produto:
    def __init__(self, nomeProduto, preco):
        self.nomeProduto = nomeProduto
        self.preco = preco

class Funcionario(Pessoa):
    def __init__(self, nome, telefone, cpf, clt):
        super().__init__(nome, telefone, cpf)
        self.clt = clt 

class Cliente(Pessoa):
    def __init__(self, nome, telefone, cpf, id_cliente):
        super().__init__(nome, telefone, cpf)
        self.id_cliente = id_cliente