Este projeto em Python visa tratar e organizar dados contidos em um arquivo CSV que contém informações sobre filmes, incluindo colunas como id do filme, Titulo e Genero. O objetivo principal é corrigir problemas nos dados, como erros de formatação, valores nulos, e duplicatas, além de organizar e renumerar os filmes.

- Uso:
  Para utilizar o projeto, basta seguir os seguintes passos:

- Clone o repositório:
  git clone https://github.com/hellentavares/movieorganizer.git
  
- Instale as dependências:
  Certifique-se de ter o Python instalado em seu ambiente. Em seguida, instale as dependências necessárias usando:
  pip install -r requirements.txt

  
- Execute o script principal:
  python main.py

  
- Resultados:
  Após a execução do script, o programa realizará as seguintes etapas:

  Renomear as colunas do arquivo CSV.
  Limpar títulos e gêneros, removendo caracteres especiais e espaços desnecessários.
  Tratar valores nulos, preenchendo-os com uma string vazia.
  Remover duplicatas baseadas em todas as colunas.
  Organizar e renumerar os filmes com base no título.
  Exibir uma amostra das primeiras e últimas linhas do DataFrame resultante.
  Salvar o DataFrame organizado em um novo arquivo CSV chamado filmes_organizados.csv.
  Estrutura do Projeto
  main.py: Script principal que utiliza a classe OrganizadorDeFilmes para realizar as operações de tratamento e organização do CSV.
  organizador.py: Contém a implementação da classe OrganizadorDeFilmes, que encapsula as operações de manipulação do DataFrame.
  Dependências
  pandas: Uma biblioteca para manipulação e análise de dados tabulares.
  unicodedata: Módulo Python que fornece acesso ao banco de dados de caracteres Unicode.
  re: Módulo Python para expressões regulares.
  locale: Módulo Python para manipulação de localidade.
  Certifique-se de que você tem essas dependências instaladas antes de executar o script principal.
