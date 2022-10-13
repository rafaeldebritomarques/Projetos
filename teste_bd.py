#Importando SQL e Connector
from sqlite3 import Cursor
import mysql.connector
#Comando para conexão com o BD Mysql, nesse caso MariaDB
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bd_python"
)

cursor = banco.cursor()
#Comandos para inserir dados em tabela no BD#

#comando_SQL = "INSERT INTO pessoas (nome,idade,email) VALUES (%s,%s,%s)"
#dados = ("Joao","50","joao@gmail.com")
#cursor.execute(comando_SQL,dados)
#banco.commit()

#Comandos para selecionar dados direto do BD #
#comando_SQL = "SELECT * FROM pessoas"
#cursor.execute(comando_SQL)
#valores_lidos = cursor.fetchall()
#print(valores_lidos)

#Comandos para selecionar dados direto do BD com uma condição #
#comando_SQL = "SELECT * FROM pessoas WHERE idade = 50"
#cursor.execute(comando_SQL)
#valores_lidos = cursor.fetchall()
#print(valores_lidos)

#Comandos para DELETAR dados direto do BD com uma condição #
comando_SQL = "DELETE FROM pessoas WHERE idade = 50"
cursor.execute(comando_SQL)

banco.commit()
