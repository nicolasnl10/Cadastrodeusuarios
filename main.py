import tkinter as tk
from UsuarioView import TelaCadastroUsuario
if __name__=="__main__":
    # Criar a janela principal
    janela = tk.Tk()

    # Criar a tela de cadastro de usuário
    tela_cadastro = TelaCadastroUsuario(janela)

    # Iniciar o loop principal da aplicação
    janela.mainloop()
