from datetime import datetime
from models.pessoa import Pessoa
from utils import limpar, print_cores

def seed():
    Pessoa("gabriel", "timon", "03/09/1999", "M", 16559687775)
    Pessoa("sérgio", "timon", "23/12/1965", "M", 92738461520)
    Pessoa("júlia", "lanzoni", "12/07/2004", "F", 48195027633)
    Pessoa("cassiane", "lanzoni", "03/02/1969", "F", 58900217020)
    Pessoa("arthur", "timon", "01/01/2015", "M", 73019462855)
    Pessoa("miguel", "lanzoni", "01/01/2019", "M", 60294718301)
    Pessoa("mariana", "souza", "15/05/1995", "F", 19485720366)
    Pessoa("roberto", "almeida", "22/11/1988", "M", 53820697144)
    Pessoa("fernanda", "pereira", "09/03/2002", "F", 71549286013)
    Pessoa("lucas", "oliveira", "30/08/2010", "M", 40928573691)
    Pessoa("beatriz", "costa", "17/04/1997", "F", 86031749205)
    Pessoa("joao", "silva", "05/06/1980", "M", 27590148362)
    Pessoa("carla", "mendes", "27/10/1975", "F", 91467235088)
    Pessoa("thiago", "ferreira", "11/01/2008", "M", 36850917420)
    Pessoa("patricia", "rocha", "19/09/1992", "F", 59281473066)
    Pessoa("vinicius", "ribeiro", "02/02/2001", "M", 80732619455)
    Pessoa("camila", "lima", "14/12/1999", "F", 15693074281)
    Pessoa("eduardo", "martins", "25/07/1985", "M", 67420591837)
    Pessoa("isabela", "barbosa", "08/08/2016", "F", 31985720644)
    Pessoa("gustavo", "carvalho", "03/03/1990", "M", 90214673851)
    Pessoa("aline", "dias", "21/06/2006", "F", 48017593622)
    Pessoa("rafael", "santos", "10/10/1970", "M", 61594820733)
    Pessoa("daniela", "castro", "28/02/1983", "F", 29374615089)
    Pessoa("pedro", "nascimento", "07/07/2012", "M", 74192860511)
    Pessoa("leticia", "teixeira", "16/11/2009", "F", 50937186244)
    Pessoa("bruno", "gomes", "01/04/1994", "M", 86730491572)


def cadastro():
    limpar()
    while True:
        print('\nDigite "0" no campo do nome para encerrar o cadastro')
        nome = input("Nome: ").strip()

        if nome == "0":
            break

        if nome == "":
            print_cores("❌ Nome não pode ser vazio!", "vermelho")
            continue

        sobrenome = input("Sobrenome: ").strip()
        if sobrenome == "":
            print_cores("❌ Sobrenome não pode ser vazio!", "vermelho")
            continue

        while True:
            nascimento = input("Data de nascimento [dd/mm/aaaa]: ").strip()
            try:
                datetime.strptime(nascimento, "%d/%m/%Y")
                break
            except ValueError:
                print_cores('❌ Data inválida! Use o formato "dd/mm/aaaa".', "vermelho")

        while True:
            sexo = input("Sexo [M/F]: ").strip().upper()[0]
            if sexo in ["M", "F"]:
                break
            else:
                print_cores('❌ Sexo inválido! Digite apenas "M" ou "F".', "vermelho")
        
        while True:
            cpf = input("CPF: ").strip()
            if cpf.isdigit() == False and (len(cpf) != 11):
                print_cores("❌ Formato inválido! Digite os 11 dígitos do CPF.", "vermelho")
            else:
                cpf = int(cpf)
                break

        Pessoa(nome, sobrenome, nascimento, sexo, cpf)

        print_cores("✅ Pessoa cadastrada com sucesso!", "verde")
