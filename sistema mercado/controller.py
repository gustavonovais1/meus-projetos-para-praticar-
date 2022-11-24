from model import *
import pymysql.cursors

connection = pymysql.connect(

    host = 'localhost',
    user = 'root',
    password = '222545', 
    port = 3306,
    autocommit = True,
    db = 'projeto-mercado',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
    )

class ControllerFuncionario():

    @classmethod
    def cadastrar_funcionario(cls, funcionario: Funcionario):

        with connection.cursor() as cursor:
                cursor.execute(f'select cpf from Funcionario where cpf = {funcionario.cpf};')
                verificaCPF = cursor.fetchall()
                if len(verificaCPF) > 0:
                    return 1
                elif len(verificaCPF) == 0:
                    try:
                        with connection.cursor() as cursor:
                            cursor.execute(f'insert into Funcionario (nome, telefone, cpf, clt) values ("{funcionario.nome}", {funcionario.telefone}, {funcionario.cpf}, {funcionario.clt})')
                        return 2
                    except:
                        return 3

    @classmethod
    def excluir_funcionario(cls, cpf):

        with connection.cursor() as cursor:
                cursor.execute(f'select cpf from Funcionario where cpf = {cpf};')
                verificaCPF = cursor.fetchall()
                if len(verificaCPF) > 0:
                    try:
                        with connection.cursor() as cursor:
                                cursor.execute(f'delete from Funcionario where cpf = {cpf};')
                        return 4
                    except:
                        return 5
                elif len(verificaCPF) == 0:
                    return 6

class ControllerCliente:

    @classmethod
    def cadastrar_cliente(cls, cliente: Cliente):

        with connection.cursor() as cursor:
                cursor.execute(f'select cpf from Cliente where cpf = {cliente.cpf};')
                verificaCPF = cursor.fetchall()
                if len(verificaCPF) > 0:
                    return 7
                elif len(verificaCPF) == 0:
                    try:    
                        with connection.cursor() as cursor:
                            cursor.execute(f'insert into Cliente (nome, telefone, cpf, id_cliente) values ("{cliente.nome}", {cliente.telefone}, {cliente.cpf}, {cliente.id_cliente})')
                            return 8
                    except:
                        return 9

    @classmethod
    def excluir_cliente(cls, cpf):

        with connection.cursor() as cursor:
                cursor.execute(f'select cpf from Cliente where cpf = {cpf};')
                verificaCPF = cursor.fetchall()
                if len(verificaCPF) > 0:
                    try:
                        with connection.cursor() as cursor:
                                cursor.execute(f'delete from Cliente where cpf = {cpf};')
                        return 10
                    except:
                        return 11
                elif len(verificaCPF) == 0:
                    return 12

class ControllerProduto:

    @classmethod
    def cadastrar_produto(cls, produto: Produto):

        with connection.cursor() as cursor:
                cursor.execute(f'select nomeProduto from Produto where nomeProduto = "{produto.nomeProduto}";')
                verificaNOME = cursor.fetchall()
                if len(verificaNOME) > 0:
                    return 13
                elif len(verificaNOME) == 0:
                    try:    
                        with connection.cursor() as cursor:
                            cursor.execute(f'insert into Produto (nomeProduto, preco) values ("{produto.nomeProduto}",{produto.preco});')
                            return 14
                    except:
                        return 15

    @classmethod
    def excluir_produto(cls, nomeProduto):
    
        with connection.cursor() as cursor:
                cursor.execute(f'select nomeProduto from Produto where nomeProduto = "{nomeProduto}";')
                verificaNOME = cursor.fetchall()
                if len(verificaNOME) > 0:
                    try:
                        with connection.cursor() as cursor:
                                cursor.execute(f'delete from Produto where nomeProduto = "{nomeProduto}";')
                        return 16
                    except:
                        return 17
                elif len(verificaNOME) == 0:
                    return 18

class ControllerListar:

    @classmethod
    def listar_funcionarios(cls):
        with connection.cursor() as cursor:
            cursor.execute('select nome, cpf from Funcionario')
            lista = cursor.fetchall()
        for i in lista:
            print(i['nome'], i['cpf'])

    @classmethod
    def listar_clientes(cls):
        with connection.cursor() as cursor:
            cursor.execute('select nome, cpf from Cliente')
            lista = cursor.fetchall()
        for i in lista:
            print(i['nome'], i['cpf'])

    @classmethod
    def listar_produtos(cls):
        with connection.cursor() as cursor:
            cursor.execute('select nomeProduto, preco from Produto')
            lista = cursor.fetchall()
        for i in lista:
            print(i['nomeProduto'], i['preco'])


ControllerListar.listar_produtos()