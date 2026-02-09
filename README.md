[README.md](https://github.com/user-attachments/files/25191627/README.md)
# Cadastro de Pessoas (CLI) 🧾👥

Projeto em **Python (linha de comando)** para cadastrar pessoas, aplicar **filtros**, ver **estatísticas** e **exportar** os dados (CSV/XLSX/JSON).  
O sistema funciona através de menus interativos no terminal, com mensagens coloridas e títulos em ASCII.

---

## ✨ Funcionalidades

### Cadastro / Edição (CRUD)
- **Adicionar pessoas** (nome, sobrenome, data de nascimento, sexo, CPF)
- **Pesquisar por CPF**
- **Editar**: nome, sobrenome, data de nascimento, sexo e CPF
- **Excluir** cadastro por CPF

### Menu de filtros
- Exibir todos os **homens**
- Exibir todas as **mulheres**
- Exibir **pessoa mais velha**
- Exibir **pessoa mais nova**
- Exibir **menores de 18**
- Exibir pessoas **acima da média de idade**
- Exibir **todos os cadastros**
- Exibir aniversariantes **por mês** (informando o mês)

### Estatísticas
- Total de cadastros
- Quantidade de homens e mulheres
- Média de idade
- Quantidade de menores e maiores de idade
- Quantidade por faixa etária (0–17, 18–29, 30–49, 50+)
- Maior e menor idade
- Aniversariantes por mês (todos os meses)

### Exportação
- Exportar para **CSV** (separador `;`)
- Exportar para **XLSX**
- Exportar para **JSON**

> ⚠️ Observação: os cadastros ficam **em memória** enquanto o programa roda.  
> Para “salvar” os dados, use as opções de **exportação**.

---

## ✅ Requisitos

- **Python 3.10+** (o projeto usa `match/case`)
- Dependência extra:
  - `openpyxl` (necessário para exportar `.xlsx`)

---

## 📦 Instalação

### 1) Clonar o repositório
```bash
git clone <URL_DO_SEU_REPO>
cd <PASTA_DO_PROJETO>
```

### 2) (Opcional) Criar venv
**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Instalar dependências
```bash
pip install openpyxl
```

---

## ▶️ Como executar

Na raiz do projeto:

```bash
python app.py
```

ou:

```bash
python3 app.py
```

---

## 🌱 Seed (dados de exemplo) vs. cadastro manual

No arquivo `app.py` existe esta variável:

```python
habilitar_cadastro = False
```

- **False**: o sistema inicia com **dados de exemplo (seed)** para você testar rápido.
- **True**: o sistema inicia direto no **cadastro manual**.

---

## 🧭 Menus do sistema

### Menu principal
```
1. Menu de filtros
2. Editar cadastro
3. Exibir estatísticas
4. Opções de exportação
0. Sair
```

### Menu de filtros
```
1. Exibir todos os Homens
2. Exibir todas as mulheres
3. Exibir pessoa mais velha
4. Exibir pessoa mais nova
5. Exibir pessoas com menos de 18 anos
6. Exibir pessoas com idade acima da média de idade
7. Exibir todos os cadastros
8. Exibir pessoas que fazem aniversário no mesmo mês
0. Voltar ao menu principal
```

### Editar cadastro
```
1. Adicionar mais pessoas
2. Editar uma pessoa
3. Excluir uma pessoa
0. Voltar ao menu principal
```

### Opções de edição
```
1. Nome
2. Sobrenome
3. Data de nascimento
4. Sexo
5. CPF
0. Cancelar operação
```

### Estatísticas
```
1. Total de cadastros
2. Quantidade de homens e mulheres
3. Média de idade
4. Quantidade de menores e maiores de idade
5. Quantidade por faixa etária
6. Maior e menor idade
7. Aniversariantes por mês
0. Voltar ao menu principal
```

### Exportação
```
1. Exportar para CSV
2. Exportar para XLSX
3. Exportar para JSON
0. Voltar para menu principal
```

---

## 📁 Onde os arquivos exportados ficam?

Por padrão, o projeto salva em:

- `~/Documents` (Pasta **Documents/Documentos** do usuário)

Arquivos gerados:
- `pessoas.csv`
- `pessoas.xlsx`
- `pessoas.json`

---

## 🧱 Estrutura do projeto

Exemplo de estrutura esperada (simplificada):

```
.
├─ app.py
├─ menu.py
├─ cadastro.py
├─ titulos.py
├─ utils.py
└─ models/
   └─ pessoa.py
```

---

## 📝 Notas úteis

- A função de limpar tela usa `cls` (Windows). Em Linux/macOS, se quiser, troque para `clear`.
- O mês do filtro de aniversariantes espera algo como:
  - `janeiro`, `fevereiro`, `março`, ... `dezembro`


