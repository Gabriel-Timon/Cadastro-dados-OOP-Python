from datetime import datetime
from utils import print_cores
import csv
import json
from pathlib import Path

class Pessoa:
    lista_pessoas = []
    def __init__(self, nome:str, sobrenome:str, data_nascimento:str, sexo:str, cpf:int):
        self._nome = nome.title()
        self._sobrenome = sobrenome.title()
        self._nascimento = data_nascimento
        self._sexo = sexo
        self._cpf = cpf
        Pessoa.lista_pessoas.append(self) 
    
    def __str__(self):
        return (
            f"{"Nome"}: {self._nome}\n"
            f"{"Sobrenome"}: {self._sobrenome}\n"
            f"{"Idade"}: {self.idade}\n"
            f"{"Sexo"}: {self.formatar_sexo}\n"
            f"{"CPF"}: {self.formatar_cpf}\n"
                )
    
    @property
    def formatar_sexo(self):
        if self._sexo == "M" or self._sexo == "F":
            match self._sexo:
                case "M": return "Masculino"
                case "F": return "Feminino"
        else:
            raise ValueError('Apenas "M" para Masculino ou "F" para Feminino')
    
    @property
    def idade(self):
        nascimento = datetime.strptime(self._nascimento, "%d/%m/%Y")
        hoje = datetime.today()
        idade = hoje.year - nascimento.year

        if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
            idade -= 1

        return round(idade, 1)
    
    @property
    def formatar_cpf(self):
        cpf_format = str(self._cpf)
        return f"{cpf_format[0:3]}.{cpf_format[3:6]}.{cpf_format[6:9]}-{cpf_format[9:]}"

    @classmethod
    def listar_cadastros(cls):
        for pessoa in cls.lista_pessoas:
            print(pessoa)
        
    
    @classmethod
    def homens(cls):
        lista_homens = [pessoa for pessoa in cls.lista_pessoas if pessoa._sexo == "M"]
        for h in lista_homens:
            print(h)

    @classmethod
    def mulheres(cls):
        lista_mulheres = [pessoa for pessoa in cls.lista_pessoas if pessoa._sexo == "F"]
        for m in lista_mulheres:
            print(m)

    @classmethod
    def mais_velho(cls):
        mais_velho = max(cls.lista_pessoas, key= lambda pessoa: pessoa.idade)
        print(mais_velho)
    
    @classmethod
    def mais_novo(cls):
        mais_novo = min(cls.lista_pessoas, key= lambda pessoa: pessoa.idade)
        print(mais_novo)
    
    @classmethod
    def menor_idade(cls):
        menores = [pessoas for pessoas in cls.lista_pessoas if pessoas.idade < 18]
        for menor in menores:
            print(menor)
    
    @classmethod
    def media_idade(cls):
        lista_idades = [pessoa.idade for pessoa in cls.lista_pessoas]
        return round(sum(lista_idades) / len(lista_idades), 1)

    @classmethod
    def pessoa_acima_media(cls):
        media = cls.media_idade()
        acima = [pessoa for pessoa in cls.lista_pessoas if media < pessoa.idade]
        for pessoa in acima:
            print(pessoa)

    @classmethod
    def total_cadastros(cls):
        print(f"Total de cadastros: {len(cls.lista_pessoas)} cadastros.")

    @classmethod
    def quantidade_homens(cls):
        lista_homens = [pessoa for pessoa in cls.lista_pessoas if pessoa._sexo == "M"]
        print(f"Quantidade de homens: {len(lista_homens)} homens.")
    
    @classmethod
    def quantidade_mulheres(cls):
        lista_mulheres = [pessoa for pessoa in cls.lista_pessoas if pessoa._sexo == "F"]
        print(f"Quantidade de mulheres: {len(lista_mulheres)} mulheres.")

    @classmethod
    def quantidade_menores(cls):
        lista_menores = [pessoa for pessoa in cls.lista_pessoas if pessoa.idade < 18]
        print(f"Quantidade de menores de idade: {len(lista_menores)} pessoas.")

    @classmethod
    def quantidade_maiores(cls):
        lista_maiores = [pessoa for pessoa in cls.lista_pessoas if pessoa.idade >= 18]
        print(f"Quantidade de maiores de idade: {len(lista_maiores)} pessoas.")

    @classmethod
    def quantidade_faixa_etaria(cls):
        lista_0_17 = [pessoa for pessoa in cls.lista_pessoas if 0 <= pessoa.idade <= 17]
        lista_18_29 = [pessoa for pessoa in cls.lista_pessoas if 18 <= pessoa.idade <= 29]
        lista_30_49 = [pessoa for pessoa in cls.lista_pessoas if 30 <= pessoa.idade <= 49]
        lista_50_mais = [pessoa for pessoa in cls.lista_pessoas if pessoa.idade >= 50]

        print(f"0-17: {len(lista_0_17)} pessoas.")
        print(f"18-29: {len(lista_18_29)} pessoas.")
        print(f"30-49: {len(lista_30_49)} pessoas.")
        print(f"50+: {len(lista_50_mais)} pessoas.")

    @classmethod
    def maior_menor_idade(cls):
        mais_novo = min(cls.lista_pessoas, key= lambda pessoa: pessoa.idade)
        mais_velho = max(cls.lista_pessoas, key= lambda pessoa: pessoa.idade)

        print(f"Menor idade: {mais_novo._nome} - {mais_novo.idade} anos.")
        print(f"Maior idade: {mais_velho._nome} - {mais_velho.idade} anos.")
    
    @classmethod
    def aniversariantes_por_mes(cls, mes_niver:str):
        meses = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]

        mes = mes_niver.lower()
        match mes:
            case "janeiro": mes = 1
            case "fevereiro": mes = 2
            case "março": mes = 3
            case "abril": mes = 4
            case "maio": mes = 5
            case "junho": mes = 6
            case "julho": mes = 7
            case "agosto": mes = 8
            case "setembro": mes = 9
            case "outubro": mes = 10
            case "novembro": mes = 11
            case "dezembro": mes = 12

        aniversariantes = [pessoa for pessoa in cls.lista_pessoas if datetime.strptime(pessoa._nascimento, "%d/%m/%Y").month == mes]
        
        if mes_niver in meses:
            if not aniversariantes:
                print_cores(f"❌ Não há aniversariantes no mês de {mes_niver.lower()}.", "vermelho")
            else:
                for n in aniversariantes:
                    print(n)
        else:
            print_cores("❌ mês inválido", "vermelho")

    @classmethod
    def quant_aniversariantes_todosMeses(cls):

        meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]

        def plural_pessoa(qtd):
            return "pessoa" if qtd == 1 else "pessoas"

        contagem = {mes: 0 for mes in range(1, 13)}

        for p in cls.lista_pessoas:
            mes = datetime.strptime(p._nascimento, "%d/%m/%Y").month
            contagem[mes] += 1

        for mes_num in range(1, 13):
            qtd = contagem[mes_num]
            print(f"{meses[mes_num-1].ljust(10)}: {qtd} {plural_pessoa(qtd)}")

    @classmethod
    def pesquisar_cadastro(cls, cpf:int):
        cpf_istrue = [p for p in cls.lista_pessoas if p._cpf == cpf]
        if cpf_istrue:
            print_cores("Cadastro atual:", "azul")
            for p in cpf_istrue:
                print(p)
                return True
        else:
            print_cores(f"\n❌ CPF não encontrado", "vermelho")
            return False

    @classmethod    
    def editar_nome(cls, cpf:int):
        for pessoa in cls.lista_pessoas:
            if pessoa._cpf == cpf:
                novo_nome = input("\nNovo nome: ").strip()
                pessoa._nome = novo_nome
        
        print_cores(f"\n✅ Nome alterado com sucesso", "verde")
    
    @classmethod
    def editar_sobrenome(cls, cpf:int):
        for pessoa in cls.lista_pessoas:
            if pessoa._cpf == cpf:
                novo_sobrenome = input("\nNovo sobrenome: ").strip()
                pessoa._sobrenome = novo_sobrenome
        
        print_cores(f"\n✅ Sobrenome alterado com sucesso", "verde")
    
    @classmethod
    def editar_dataNascimento(cls, cpf:int):
        for pessoa in cls.lista_pessoas:
            if pessoa._cpf == cpf:
                 while True:
                    nova_data = input("\nNova data de nascimento [dd/mm/aaaa]: ").strip()
                    try:
                        datetime.strptime(nova_data, "%d/%m/%Y")
                        pessoa._nascimento = nova_data
                        break
                    except ValueError:
                        print_cores('❌ Data inválida! Use o formato "dd/mm/aaaa".', "vermelho")
        
        print_cores(f"\n✅ Data de nascimento alterada com sucesso", "verde")
    
    @classmethod
    def editar_sexo(cls,cpf:int):
        for pessoa in cls.lista_pessoas:
            if pessoa._cpf == cpf:
                while True:
                    novo_sexo = input("\nSexo atualizado [M/F]: ").strip().upper()[0]
                    if novo_sexo not in ["M", "F"]:
                        print_cores('Resposta inválida! Digite "M" para Masculino ou "F" para Feminino', 'vermelho')
                    else:
                        pessoa._sexo = novo_sexo
                        break

        print_cores(f"\n✅ Sexo alterado com sucesso", "verde")

    @classmethod
    def editar_cpf(cls, cpf:int):
        for pessoa in cls.lista_pessoas:
            if pessoa._cpf == cpf:
                while True:
                    novo_cpf = input("\nNovo CPF: ").strip()
                    if novo_cpf.isdigit() and len(novo_cpf) == 11:
                        pessoa._cpf = int(novo_cpf)
                        break
                    else:
                        print_cores(f"O CPF {novo_cpf} é inválido.", "vermelho")
        print_cores("\n✅ CPF alterado com sucesso", "verde")

    @classmethod
    def excluir_cadastro(cls, cpf:int):
        for pessoa in cls.lista_pessoas:
            if pessoa._cpf == cpf:
                cls.lista_pessoas.remove(pessoa)
        
        print_cores("\n✅ Cadastro removido com sucesso", "verde")
            
    @classmethod
    def to_dict_list(cls):
        return [
            {
                "nome": p._nome,
                "sobrenome": p._sobrenome,
                "data_nascimento": p._nascimento,
                "sexo": p.formatar_sexo,
                "cpf": str(p._cpf).zfill(11),
                "idade": p.idade,
            }
            for p in cls.lista_pessoas
        ]
    
    @classmethod
    def pasta_documentos(cls):
        return Path.home() / "Documents"


    @classmethod
    def exportar_csv(cls, nome_arquivo="pessoas.csv"):
        dados = cls.to_dict_list()
        if not dados:
            print_cores("❌ Não há cadastros para exportar.", "vermelho")
            return

        caminho = cls.pasta_documentos() / nome_arquivo

        with caminho.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=dados[0].keys(), delimiter=";")
            writer.writeheader()
            writer.writerows(dados)

        print_cores(f"✅ Exportado para CSV em: {caminho}", "verde")


    @classmethod
    def exportar_json(cls, nome_arquivo="pessoas.json"):
        dados = cls.to_dict_list()
        if not dados:
            print_cores("❌ Não há cadastros para exportar.", "vermelho")
            return

        caminho = cls.pasta_documentos() / nome_arquivo

        with caminho.open("w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

        print_cores(f"✅ Exportado para JSON em: {caminho}", "verde")


    @classmethod
    def exportar_xlsx(cls, nome_arquivo="pessoas.xlsx"):
        from openpyxl import Workbook

        dados = cls.to_dict_list()
        if not dados:
            print_cores("❌ Não há cadastros para exportar.", "vermelho")
            return

        wb = Workbook()
        ws = wb.active
        ws.title = "Pessoas"

        headers = list(dados[0].keys())
        ws.append(headers)

        for row in dados:
            ws.append([row[h] for h in headers])

        caminho = cls.pasta_documentos() / nome_arquivo
        wb.save(caminho)

        print_cores(f"✅ Exportado para XLSX em: {caminho}", "verde")
