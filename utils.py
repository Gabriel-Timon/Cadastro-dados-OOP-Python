from os import system 

def limpar():
    system("cls")

def titulo(titulo):
    print('-'*(len(titulo)+2))
    print(titulo)
    print('-'*(len(titulo)+2))
    print()


def print_cores(texto: str = "", cor: str = ""):
    c = cor.lower()
    match c:
        case "preto": print(f"\033[30m{texto}\033[0m")
        case "vermelho": print(f"\033[31m{texto}\033[0m")
        case "verde": print(f"\033[32m{texto}\033[0m")
        case "amarelo": print(f"\033[33m{texto}\033[0m")
        case "azul": print(f"\033[34m{texto}\033[0m")
        case "magenta": print(f"\033[35m{texto}\033[0m")
        case "ciano": print(f"\033[36m{texto}\033[0m")
        case "": print(texto)


def input_cores(texto: str = "", cor: str = ""):
    c = cor.lower()
    match c:
        case "preto": input(f"\033[30m{texto}\033[0m")
        case "vermelho": input(f"\033[31m{texto}\033[0m")
        case "verde": input(f"\033[32m{texto}\033[0m")
        case "amarelo": input(f"\033[33m{texto}\033[0m")
        case "azul": input(f"\033[34m{texto}\033[0m")
        case "magenta": input(f"\033[35m{texto}\033[0m")
        case "ciano": input(f"\033[36m{texto}\033[0m")
        case "": input(texto)


def mensagem_continuar():
    input_cores('\nPressione "Enter" para continuar', "verde")