# Trabalho 1 – Programação Orientada a Objetos

## Sistema Eleitoral em Python

Este trabalho consiste na criação de um sistema eleitoral utilizando programação orientada a objetos em Python.
O programa realiza o cadastro de partidos, eleitores e candidatos a prefeito e vereador. Também simula uma eleição, contabilizando votos válidos, brancos e nulos.

## Organização dos arquivos

- `eleicao/sistema.py`: contém as classes e os métodos do sistema.
- `eleicao/__init__.py`: identifica o pacote Python.
- `app.py`: programa principal, responsável pela leitura dos arquivos e execução da eleição.
- `input/`: contém os arquivos Partidos.txt, Eleitores.txt e Urnas.txt.
- `output/`: contém os cinco relatórios gerados pelo programa.

## Como executar

1. Ter o Python instalado no computador.
2. Abrir a pasta do trabalho no VS Code.
3. Verificar se os três arquivos de entrada estão na pasta `input`.
4. Abrir o terminal na pasta principal do projeto.
5. Executar o comando:

`python app.py`

Após a execução, os relatórios serão gerados automaticamente na pasta `output`.

## Funcionamento do programa

O programa começa lendo os partidos e depois realiza o cadastro dos eleitores e candidatos. Em seguida, lê os votos e os distribui entre as urnas de acordo com a zona e a seção eleitoral.

As classes utilizam herança, métodos de classe, dicionários e tratamento de exceções para organizar os dados e validar os cadastros.

## Relatórios gerados

O sistema gera cinco arquivos:

1. `relatorio_eleitores.txt`: quantidade de eleitores e candidatos, separados por zona e seção.
2. `relatorio_partidos.txt`: partidos cadastrados e quantidade de candidatos.
3. `relatorio_urnas.txt`: votos válidos, brancos e nulos de cada urna.
4. `relatorio_resultado.txt`: resultado geral da eleição e candidatos mais votados.
5. `relatorio_erros.txt`: erros encontrados durante os cadastros.
