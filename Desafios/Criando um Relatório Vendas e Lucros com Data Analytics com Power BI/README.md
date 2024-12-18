# Desafio - Criando um Relatório Vendas e Lucros com Data Analytics com Power BI

Esse repositório como objetivo de apresentar os arquivos e link criados para a conclusão do desafio Criando um Relatório Vendas e Lucros com Data Analytics com Power BI. Nesse desafio houve a integração dos diversos assuntos abordados durante o bootcamp para aprimorar a experiência do usuário com a utilização de recursos e visuais mais avançados de análise de dados.

## Link do relatório no Power BI Service (web)
[Relatório de Vendas e Lucros](https://app.powerbi.com/groups/me/reports/9925f7bf-f5be-4592-81d2-0ca55ed25d23?ctid=ff71608c-4f7a-46dc-9bb0-8fe371f5b679&pbi_source=linkShare)

## Criação do relatório
O relatório foi criado seguindo os passos dos arquivos do link abaixo:

[Projeto de Data Analytics com Power BI](https://academiapme-my.sharepoint.com/:f:/g/personal/renato_dio_me/EovzCujn0JJEhT5Nm8K5_DkB9Hc8ONl2jSiHIVf35LXK4Q?e=wqvxUo)

## Melhorias

Realizando as alterações no **sales_report_desafio_projeto** foi elaborado um relatório com novo design e funcionalidades abaixo:

- Melhoria na visibilidade dos dados dos relatórios e experiência do usuário.
- Alteração e padronização das cores e formas do relatório.
- Revisão da segmentação dos dados.
- Insersão de novas opções de navegação entre as páginas.

## Páginas do Relatório

### Homepage

Nesta página foi realizada somente a insersão de uma forma com cantos arredondados com transparência na frente do texto para integrar essa página as demais, onde utilizei várias formas com cantos arredondados para segmentação dos dados. O botão **Explorar análise** foi mantido sem alterações e tem a função de direcionar o usuário a página principal do relatório.

![Homepage](https://github.com/joaopaulonsilva/Bootcamp_NTT_DATA_Engenharia_de_Dados/blob/main/Desafios/Criando%20um%20Relat%C3%B3rio%20Vendas%20e%20Lucros%20com%20Data%20Analytics%20com%20Power%20BI/assets/homepage.png)

### Página Principal

A página é dedicada a apresentar os resultados de vendas. Os 5 cartões na parte superior apresentam o somatório dos principais indicadores. 
> [!NOTE]
> - Um dos cartões foi alterado para apresentar a soma dos lucros (sum of profit) pois, o relatório original possuia dois cartões com a mesma informação soma de desconto (sum of discounts).<br><br>
> - Foi realizada a correção do botão **Treemap** pois, o mesmo não ocultava o gráfico de mapas (Map Chart).
A página também possuí a visão de vendas por segmento, produto e país, sendo que os gráficos com as visões segmento e país são dinâmicos selecionados por meio dos botões acima dos gráficos.

![Homepage](https://github.com/joaopaulonsilva/Bootcamp_NTT_DATA_Engenharia_de_Dados/blob/main/Desafios/Criando%20um%20Relat%C3%B3rio%20Vendas%20e%20Lucros%20com%20Data%20Analytics%20com%20Power%20BI/assets/principal.png)

### Página Detalhes

A página é dedicada a apresentar maiores detalhes dos resultados de vendas. Temos a visão temporal por mês e semestre, selecionada por meio dos dois botões acima dos gráficos.
> [!NOTE]
> A visão mensal possuí uma linha tracejada inserida utilizando a função **Linha média**, para facilitar a visualização dos meses que estão acima da média.
A página também possuí a tabela com as vendas por trimestre e o Histograma das unidades vendidas.

![Homepage](https://github.com/joaopaulonsilva/Bootcamp_NTT_DATA_Engenharia_de_Dados/blob/main/Desafios/Criando%20um%20Relat%C3%B3rio%20Vendas%20e%20Lucros%20com%20Data%20Analytics%20com%20Power%20BI/assets/detalhes.png)

### Página Principais Produtos e Outliers

A página é dedicada a apresentar as vendas discrepantes por meio de um gráfico de dispersão e os três principais produtos vendidos por país e no geral e possuí um menu de reprodução no qual é possível visualizar os dados mês a mês de forma contínua. 

Os gráficos foram criados utilizando medidas e também a função P e R. Os códigos das medidas criadas são apresentados abaixo:

```MEDIDAS
TOP3 PRODUCT = CALCULATE(
    [total sales],
    TOPN(
        3, 
        ALL(financials[Product]),
        [total sales]), 
    VALUES(financials[Product])
    )
    
outlier = CALCULATE( 
    [total de vendidos],
    FILTER(
        VALUES(financials[Product]),
        COUNTROWS( FILTER(financials, [total de vendidos] >= 150)) > 0
    )
)
```

![Homepage](https://github.com/joaopaulonsilva/Bootcamp_NTT_DATA_Engenharia_de_Dados/blob/main/Desafios/Criando%20um%20Relat%C3%B3rio%20Vendas%20e%20Lucros%20com%20Data%20Analytics%20com%20Power%20BI/assets/topn.png)



> [!TIP]
> A imagem de fundo de todas as páginas foi inserida como wallpaper e não como uma imagem inserida no relatório e enviada para trás, como sugere a instrutora.
> 
> ![Wallpaper](https://github.com/joaopaulonsilva/Bootcamp_NTT_DATA_Engenharia_de_Dados/blob/main/Desafios/Criando%20um%20Relat%C3%B3rio%20Vendas%20e%20Lucros%20com%20Data%20Analytics%20com%20Power%20BI/assets/wallpaper.png)
