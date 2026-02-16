

***Primeira fase de desenvolvimento:***

  Automoção de lista de ingredientes a partir de receitas a serem feitas com possibilidade de download de lista para preparação em .doc, .pdf e .txt.

***Segunda fase do desenvolvimento:***

  Calculos de base nutricional por pratos a partir de integração com base de dados TACO (Tabela Brasileira de Composição de Alimentos) criando um sistema de consolidação alimentar baseado em dados nutricionais oficiais brasileiros a partir do projeto (TACO) coordenado pelo Núcleo de Estudos e Pesquisas em Alimentação (NEPA) da UNICAMP e com financiamento do Ministério da Saúde – MS e do Ministério do Desenvolvimento Social e Combate à Fome – MDS.
  O conjunto de dados Afrodite, usado para a busca de receitas, fornece dados de receitas semiestruturados. Uma lógica de análise sintática personalizada foi implementada para extrair quantidades numéricas e padronizar os nomes dos ingredientes antes de mesclar com a tabela nutricional oficial brasileira (TACO).

***Terceira fase:***
  Aqui fizemos a limpeza e padronização dos dados da BD Afrodite, de forma que possamos intergra-la com maior facilidade com o TACO e amenizando desafios de padronização semântica entre bases distintas.


<!--
Fluxo final ideal:
  Seleciona pratos da semana
  Visualiza ingredientes por prato
  Calcula macros por prato
  Consolida ingredientes da semana
  Baixa lista (.txt)

### Etapas do projeto
  - Exploração da base TACO
  - Limpeza e padronização
  - Criação de estrutura relacional simplificada
  - Agregação nutricional
  - Automação da consolidação de compras
