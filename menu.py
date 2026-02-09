from utils import *
from titulos import *
from cadastro import cadastro
from models.pessoa import Pessoa

def menu_principal():
    limpar()
    titulo_menuPrincipal()
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
            case 4: menu_exportacao()
            case 0: pass
    else:
        print_cores("\n❌ Digite apenas opções entre 0 e 4", "vermelho")

def menu_filtros():
    limpar()
    titulo_menuFiltros()
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
                subtitulo_exibirHomens()
                Pessoa.homens()
                mensagem_continuar()
                menu_filtros()

            case 2: 
                limpar()
                subtitulo_exibirMulheres()
                Pessoa.mulheres()
                mensagem_continuar()
                menu_filtros()
            
            case 3: 
                limpar()
                subtitulo_pessoaMaisVelha()
                Pessoa.mais_velho()
                mensagem_continuar()
                menu_filtros()

            case 4: 
                limpar()
                subtitulo_pessoaMaisNova()
                Pessoa.mais_novo()
                mensagem_continuar()
                menu_filtros()

            case 5: 
                limpar()
                subtitulo_menoresIdade()
                Pessoa.menor_idade()
                mensagem_continuar()
                menu_filtros()

            case 6: 
                limpar()
                subtitulo_idadeAcimaMedia()
                Pessoa.pessoa_acima_media()
                mensagem_continuar()
                menu_filtros()

            case 7: 
                limpar()
                subtitulo_todosCadastros()
                Pessoa.listar_cadastros()
                mensagem_continuar()
                menu_filtros()
            
            case 8:
                limpar()
                subtitulo_aniversariantesMes()
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
    titulo_menuEstatisticas()
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
                subtitulo_totalCadastros()
                Pessoa.total_cadastros()
                mensagem_continuar()
                menu_estatisticas()
                
            case 2: 
                limpar()
                subtitulo_totalHomensMulheres()
                Pessoa.quantidade_mulheres()
                Pessoa.quantidade_homens()
                mensagem_continuar()
                menu_estatisticas()

            case 3:
                limpar()
                subtitulo_mediaIdade()
                print(f"\nA média de idade é {Pessoa.media_idade()} anos.")
                mensagem_continuar()
                menu_estatisticas()
            
            case 4:
                limpar()
                subtitulo_maioresMenoresIdade()
                Pessoa.quantidade_menores()
                Pessoa.quantidade_maiores()
                mensagem_continuar()
                menu_estatisticas()

            case 5:
                limpar()
                subtitulo_pessoasFaixaEtaria()
                Pessoa.quantidade_faixa_etaria()
                mensagem_continuar()
                menu_estatisticas()
            
            case 6: 
                limpar()
                subtitulo_maisVelhomaisNovo()
                Pessoa.maior_menor_idade()
                mensagem_continuar()
                menu_estatisticas()

            case 7: 
                limpar()
                subtitulo_aniversariantesMes()
                Pessoa. quant_aniversariantes_todosMeses()
                mensagem_continuar()
                menu_estatisticas()

            case 0: menu_principal()
    else:
         print_cores("\n❌ Digite apenas opções entre 0 e 7", "vermelho")

def menu_edicao_cadastro():
    limpar()
    titulo_edicaoCadastro()
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
                subtitulo_pesquisarporCPF()
                cpf = input("CPF: ").strip()
                if cpf.isdigit() and len(cpf) == 11:
                    achou = Pessoa.pesquisar_cadastro(int(cpf))

                    if achou:
                        mensagem_continuar()
                        limpar()
                        menu_edicao(int(cpf))
                    
                    else:
                       mensagem_continuar()
                       menu_edicao_cadastro()
                else:
                    print_cores("\n❌ Inválido! Digite os 11 dígitos do CPF", "vermelho")
                    mensagem_continuar()
                    menu_edicao_cadastro()
                    
            case 3: 
                limpar()
                subtitulo_pesquisarporCPF()
                cpf = input("CPF: ").strip()
                if cpf.isdigit() and len(cpf) == 11:
                    achou = Pessoa.pesquisar_cadastro(int(cpf))

                    if achou:
                        while True:
                            confirmar = input("\nConfirmar exclusão do cadastro [S/N]? ").strip().upper()[0]
                            if confirmar in ["S", "N"]:
                                if confirmar == "S":
                                    Pessoa.excluir_cadastro(int(cpf))
                                    mensagem_continuar()
                                    break
                                    
                                elif confirmar == "N":
                                    print_cores("\n❌ Remoção de cadastro cancelada", "vermelho")
                                    mensagem_continuar()
                                    break
                            else:
                                print_cores('\n❌ Digite apenas "S" ou "N" para sim ou não', 'vermelho')
                        
                        menu_principal()

                    else:
                       mensagem_continuar()
                       menu_edicao_cadastro()
                else:
                    print_cores("\n❌ Inválido! Digite os 11 dígitos do CPF", "vermelho")
                    mensagem_continuar()
                    menu_edicao_cadastro()

            case 0: menu_principal()
    else:
        print_cores("\n❌ Digite apenas opções entre 0 e 3", "vermelho")

def menu_edicao(cpf):
    titulo_opcoesEdicao()
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
            case 4: Pessoa.editar_sexo(cpf)
            case 5: Pessoa.editar_cpf(cpf)
            case 0: menu_edicao_cadastro()

def menu_exportacao():
    limpar()
    titulo_menuExportacao()
    print("1. Exportar para CSV")
    print("2. Exportar para XLSX")
    print("3. Exportar para JSON")
    print("0. Voltar para menu principal")

    opcao = input("\nEscolha: ").strip()

    if opcao.isdigit() and (0 <= int(opcao) <= 3):
        match int(opcao):
            case 1:
                while True:
                    confirmar = input("Confirmar exportação [S/N]: ").strip().upper()[0]
                    if confirmar in ["S", "N"]:
                        match confirmar:
                            case "S": 
                                Pessoa.exportar_csv()
                                mensagem_continuar()
                                break
                            case "N":
                                print_cores("\n❌ Exportação cancelada", "vermelho")
                                mensagem_continuar()
                                break
                    else:
                        print_cores('\n❌ Digite apenas "S" ou "N" para sim ou não', 'vermelho')
                    
                menu_principal()

            case 2:
                while True:
                    confirmar = input("Confirmar exportação [S/N]: ").strip().upper()[0]
                    if confirmar in ["S", "N"]:
                        match confirmar:
                            case "S": 
                                Pessoa.exportar_xlsx()
                                mensagem_continuar()
                                break
                            case "N":
                                print_cores("\n❌ Exportação cancelada", "vermelho")
                                mensagem_continuar()
                                break
                    else:
                        print_cores('\n❌ Digite apenas "S" ou "N" para sim ou não', 'vermelho')
                    
                menu_principal()
            case 3:
                while True:
                    confirmar = input("Confirmar exportação [S/N]: ").strip().upper()[0]
                    if confirmar in ["S", "N"]:
                        match confirmar:
                            case "S": 
                                Pessoa.exportar_json()
                                mensagem_continuar()
                                break
                            case "N":
                                print_cores("\n❌ Exportação cancelada", "vermelho")
                                mensagem_continuar()
                                break
                    else:
                        print_cores('\n❌ Digite apenas "S" ou "N" para sim ou não', 'vermelho')
                    
                menu_principal()
            case 0: menu_principal()
    else:
        print_cores("\n❌ Escolha uma opção entre 0 e 3", "vermelho")
