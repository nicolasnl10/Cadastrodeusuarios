import tkinter as tk
import mysql.connector
from tkinter import messagebox
from UsuarioController import cadastrarUsuario
class TelaCadastroUsuario:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cadastro de Usuário")
    

        janela.geometry("500x400")  
        janela.resizable(True, True)

        # Título
        nome_projeto="Projeto Integrador"
        titulo_label = tk.Label(janela, text=nome_projeto, font=("Arial", 16))
        titulo_label.pack(pady=10)

    # Subtítulo
        subtitulo_label = tk.Label(janela, text="Cadastre o usuário: ", font=("Arial", 12))
        subtitulo_label.pack(pady=5)


        # Rótulo e campo de entrada para o nome
        self.lbl_nome = tk.Label(janela, text="Nome:")
        self.lbl_nome.pack()
        self.entry_nome = tk.Entry(janela)
        self.entry_nome.pack()

        # Rótulo e campo de entrada para o CPF
        self.lbl_cpf = tk.Label(janela, text="CPF:")
        self.lbl_cpf.pack()
        self.entry_cpf = tk.Entry(janela)
        self.entry_cpf.pack()

        # Rótulo e campo de entrada para o e-mail
        self.lbl_email = tk.Label(janela, text="E-mail:")
        self.lbl_email.pack()
        self.entry_email = tk.Entry(janela)
        self.entry_email.pack()

        # Botão de cadastrar
        self.btn_cadastrar = tk.Button(janela, text="Cadastrar", command=self.cadastrar_usuario)
        self.btn_cadastrar.pack()
        
        self.btn_relatorio = tk.Button(janela, text="Gerar Relatório", command=self.gerar_relatorio)
        self.btn_relatorio.pack()

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        email = self.entry_email.get()
        sucesso = cadastrarUsuario(nome,cpf,email)
        if sucesso:
            self.entry_nome.delete(0, tk.END)
            self.entry_cpf.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            messagebox.showinfo("Alerta", "Usuario cadastrado com sucesso")
        else:
            messagebox.showinfo("Alerta", "Dados inválidos!")

    def gerar_relatorio(self):
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
            comando_sql = "select * from usuarios"
            cursor.execute(comando_sql)
            resultado = cursor.fetchall()
            with open ("Relatório.txt","w") as arquivo:
                for linha in resultado:
                    arquivo.write(str(linha)+"\n")
            messagebox.showinfo("Alerta", "Relatório gerado com sucesso!")
        except mysql.connector.Error as error:
            print("Erro ao conectar ao banco de dados!", error)
        finally:
            # Fechar a conexão com o banco de dados
            if conn.is_connected():
                cursor.close()
                conn.close()

        # Aqui você pode adicionar a lógica para salvar os dados do usuário no banco de dados

        #print("Usuário cadastrado:")
        #print("Nome:", nome)
        #print("CPF:", cpf)
        #print("E-mail:", email)

