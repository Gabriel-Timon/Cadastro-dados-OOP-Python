from models.pessoa import Pessoa
from menu import menu_principal
from cadastro import cadastro, seed

habilitar_cadastro = False

def main():
    if habilitar_cadastro:
        cadastro()
    else:
        seed()
        
    menu_principal()
    # print(pessoa for pessoa in )
   

if __name__ == "__main__":
    main()
