from utils import limpar, print_cores, input_cores, titulo, mensagem_continuar
from cadastro import cadastro
from models.pessoa import Pessoa

def menu_principal():
    limpar()
    print("1. Menu de filtros")
    print("2. Editar cadastro")
    print("3. Exibir estatísticas")
    print("4. Opções de exportação")
    print("0. Sair")

    opcao = input("\nEscolha: ").strip()

    if opcao.isdigit() and (int(opcao) >= 0 and int(opcao) <=4):
        match int(opcao):
            case 1: menu_filtros()
            case 2: menu_edicao_cadastro()
            case 3: menu_estatisticas()
            case 4: pass
            case 0: pass
    else:
        print_cores("\n❌ Digite apenas opções entre 0 e 4", "vermelho")

def menu_filtros():
    limpar()
    print("1. Exibir todos os Homens")
    print("2. Exibir todas as mulheres")
    print("3. Exibir pessoa mais velha")
    print("4. Exibir pessoa mais nova")
    print("5. Exibir pessoas com menos de 18 anos")
    print("6. Exibir pessoas com idade acima da média de idade")
    print("7. Exibir todos os cadastros")
    print("8. Exibir pessoas que fazem aniversário no mesmo mês")
    print("0. Voltar ao  menu principal")

    opcao = input("\nEscolha: ").strip()

    if opcao.isdigit() and (int(opcao) >= 0 and int(opcao) <=8):
        match int(opcao):
            case 1:
                limpar()
                titulo("EXIBIR TODOS OS HOMENS")
                Pessoa.homens()
                mensagem_continuar()
                menu_filtros()

            case 2: 
                limpar()
                titulo("EXIBIR TODAS AS MULHERES")
                Pessoa.mulheres()
                mensagem_continuar()
                menu_filtros()
            
            case 3: 
                limpar()
                titulo("EXIBIR PESSOA MAIS VELHA")
                Pessoa.mais_velho()
                mensagem_continuar()
                menu_filtros()

            case 4: 
                limpar()
                titulo("EXIBIR PESSOA MAIS NOVA")
                Pessoa.mais_novo()
                mensagem_continuar()
                menu_filtros()

            case 5: 
                limpar()
                titulo("EXIBIR MENORES DE IDADE")
                Pessoa.menor_idade()
                mensagem_continuar()
                menu_filtros()

            case 6: 
                limpar()
                titulo("EXIBIR PESSOAS COM IDADE ACIMA DA MÉDIA DE IDADE")
                Pessoa.pessoa_acima_media()
                mensagem_continuar()
                menu_filtros()

            case 7: 
                limpar()
                titulo("EXIBIR TODOS OS CADASTROS")
                Pessoa.listar_cadastros()
                mensagem_continuar()
                menu_filtros()
            
            case 8:
                limpar()
                titulo("EXIBIR ANIVERSARIANTES NO MESMO MÊS")
                mes = input("Qual mês deseja pesquisar? ").strip()
                print()
                Pessoa.aniversariantes_por_mes(mes)
                mensagem_continuar()
                menu_filtros()

            case 0: menu_principal()
    else:
        print_cores("\n❌ Digite apenas opções entre 0 e 8", "vermelho")

def menu_estatisticas():
    limpar()
    print("1. Total de cadastros")
    print("2. Quantidade de homens e mulheres")
    print("3. Média de idade")
    print("4. Quantidade de menores e maiores de idade")
    print("5. Quantidade por faixa etária")
    print("6. Maior e menor idade")
    print("7. Aniversariantes por mês")
    print("0. Voltar ao menu principal")

    opcao = input("\nEscolha: ").strip()

    if opcao.isdigit() and (0 <= int(opcao) <= 7):
        match int(opcao):
            case 1:
                limpar()
                titulo("TOTAL DE CADASTROS")
                Pessoa.total_cadastros()
                mensagem_continuar()
                menu_estatisticas()
                
            case 2: 
                limpar()
                titulo("QUANTIDADE DE HOMENS E MULHERES")
                Pessoa.quantidade_mulheres()
                Pessoa.quantidade_homens()
                mensagem_continuar()
                menu_estatisticas()

            case 3:
                limpar()
                titulo("MÉDIA DE IDADE\n")
                print(f"\nA média de idade é {Pessoa.media_idade()} anos.")
                mensagem_continuar()
                menu_estatisticas()
            
            case 4:
                limpar()
                titulo("QUANTIDADE DE MAIORES E MENORES DE IDADE")
                Pessoa.quantidade_menores()
                Pessoa.quantidade_maiores()
                mensagem_continuar()
                menu_estatisticas()

            case 5:
                limpar()
                titulo("QUANTIDADE DE PESSOAS POR FAIXA ETÁRIA")
                Pessoa.quantidade_faixa_etaria()
                mensagem_continuar()
                menu_estatisticas()
            
            case 6: 
                limpar()
                titulo("PESSOA COM A MENOR IDADE E COM A MAIOR IDADE")
                Pessoa.maior_menor_idade()
                mensagem_continuar()
                menu_estatisticas()

            case 7: 
                limpar()
                titulo("ANIVERSARIANTES POR MES")
                Pessoa. quant_aniversariantes_todosMeses()
                mensagem_continuar()
                menu_estatisticas()

            case 0: menu_principal()
    else:
         print_cores("\n❌ Digite apenas opções entre 0 e 7", "vermelho")

def menu_edicao_cadastro():
    limpar()
    print("1. Adicionar mais pessoas")
    print("2. Editar uma pessoa")
    print("3. Excluir uma pessoa")
    print("0. Voltar ao menu principal")

    opcao = input("\nEscolha: ").strip()

    if opcao.isdigit() and (0 <= int(opcao) <= 3):
        match int(opcao):
            case 1: 
                cadastro()
                mensagem_continuar()
                menu_principal()
            case 2: 
                limpar()
                titulo("PESQUISAR POR CPF")
                cpf = input("CPF: ").strip()
                if cpf.isdigit() and len(cpf) == 11:
                    Pessoa.pesquisar_cadastro(int(cpf))
                    mensagem_continuar()
                    limpar()
                    menu_edicao(int(cpf))
                    mensagem_continuar()
                    menu_principal()
                else:
                    print_cores("❌ Inválido! Digite os 11 dígitos do CPF", "vermelho")
            case 3: pass
            case 0: pass
    else:
        print_cores("❌ Digite apenas opções entre 0 e 3", "vermelho")

def menu_edicao(cpf):
    print("O que deseja editar?\n")
    print("1. Nome")
    print("2. Sobrenome")
    print("3. Data de nascimento")
    print("4. Sexo")
    print("5. CPF")
    print("0. Cancelar operação")

    opcao = input("\nEscolha: ").strip()

    if opcao.isdigit() and (0 <= int(opcao) <= 5):
        match int(opcao):
            case 1: Pessoa.editar_nome(cpf)
            case 2: Pessoa.editar_sobrenome(cpf)
            case 3: Pessoa.editar_dataNascimento(cpf)
            case 4: pass
            case 5: pass
            case 0: pass