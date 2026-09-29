# 📊 Analisador de Relatórios Financeiros CLI

Um analisador de despesas pessoal em Python que lê dados de transações a partir de um arquivo CSV, realiza a higienização dos dados e exibe um relatório detalhado com os gastos agrupados por categoria e o total geral.

Projetado com foco em **boas práticas de programação**, **tratamento de exceções personalizadas** e **modularização**.

---

## 🛠️ Funcionalidades

- **Processamento de CSV**: Leitura e parsing de arquivos CSV usando o módulo nativo `csv`.
- **Sanitização de Dados**: Limpeza inteligente de valores numéricos para remover aspas, espaços e caracteres indesejados antes da conversão para `float`.
- **Tratamento de Exceções**: 
  - Captura e aviso para arquivos inexistentes (`FileNotFoundError`).
  - Identificação de linhas corrompidas ou mal formatadas sem interromper a execução do programa.
  - Exceções personalizadas (`ValorInferiorException`, `ErroArquivoCSVException`) para validação de regras de negócio.
- **Agrupamento Dinâmico**: Somatório e exibição dos gastos agrupados por categoria através de dicionários.
- **Estrutura Modular**: Organizado em funções e protegido pelo bloco `if __name__ == "__main__":`.

---

## 💻 Tecnologias Utilizadas

- **Python 3.x**
- Módulos nativos: `csv`

---

## 📁 Estrutura do Arquivo `dados.csv`

O arquivo `dados.csv` deve estar na raiz do projeto e possuir o seguinte formato:

```csv
Data,Descricao,Categoria,Valor
2026-03-01,Supermercado,Alimentacao,"150.50"
2026-03-02,Uber,Transporte,"25.00"
2026-03-03,Restaurante,Alimentacao,"89.90"
2026-03-05,Farmacia,Saude,"45.20"