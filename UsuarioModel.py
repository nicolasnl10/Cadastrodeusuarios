import mysql.connector
class Usuario:
    def __init__(self, cpf, nome, email):
        self.cpf = cpf
        self.nome = nome
        self.email = email

    def save(self):
        # Configurar a conexão com o banco de dados
        conn = mysql.connector.connect(
            host="localhost",
            database="projeto_Integrador",
            user="root",
            password=""
        )

        try:
            # Criação de um cursor para executar comandos SQL
            cursor = conn.cursor()

            # Executar o comando SQL para inserir o usuário
            comando_sql = "INSERT INTO usuarios (cpf, nome, email) VALUES (%s, %s, %s)"
            valores = (self.cpf, self.nome, self.email)
            cursor.execute(comando_sql, valores)

            # Confirmar a transação
            conn.commit()

            print("Usuário adicionado com sucesso!")
        except mysql.connector.Error as error:
            print("Erro ao adicionar usuário ao banco de dados:", error)
        finally:
            # Fechar a conexão com o banco de dados
            if conn.is_connected():
                cursor.close()
                conn.close()