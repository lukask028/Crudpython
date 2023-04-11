import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root123!',
    database = 'bdcrud',
)

cursor = conexao.cursor()


#CRUD
nome_produto = "cenoura"
valor = 15
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}" '
cursor.execute(comando)
conexao.commit() #valida alteração no banco de dados



cursor.close()
conexao.close()

#CREATE
# nome_produto = "arroz"
# valor = 30
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor}) '
# cursor.execute(comando)
# conexao.commit() #valida alteração no banco de dados
# # resultado = cursor.fetchall() #ler o banco de dados

#READ

# nome_produto = "arroz"
# valor = 30
# comando = f'SELECT * FROM vendas '
# cursor.execute(comando)
# # conexao.commit() #valida alteração no banco de dados
# resultado = cursor.fetchall() #ler o banco de dados
# print(resultado)


#UPDATE

# nome_produto = "cenoura"
# valor = 15
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}" '
# cursor.execute(comando)
# conexao.commit() #valida alteração no banco de dados

#DELETE

# nome_produto = "cenoura"
# valor = 15
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}" '
# cursor.execute(comando)
# conexao.commit() #valida alteração no banco de dados