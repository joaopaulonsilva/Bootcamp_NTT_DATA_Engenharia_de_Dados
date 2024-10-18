
# Desafio - Modelando um Dashboard de E-commerce com Power BI Utilizando Fórmulas DAX

Esse arquivo tem o intuito de documentar os passos realizados para a conclusão do desafio Modelando um Dashboard de E-commerce com Power BI Utilizando Fórmulas DAX.

## Criação das tabelas
Todas as tabelas foram criadas seguindo os passos do arquivo [Descrição do Desafio - Modelagem e Transformação de dad.docx](https://academiapme-my.sharepoint.com/:w:/g/personal/renato_dio_me/EW76WjPAA8RGgC3i44ofFq4BBiWzM-CN5S312YwOQCIwBA?rtime=t_QJoWzv3Eg)



**1) Tabela Fato - F_Vendas** (SK_ID , ID_Produto, Produto, Units Sold, Sales Price, Discount  Band, Segment, Country, Salers, Profit, Date (campos))

**2) Tabela Dimensão - D_Produtos** (ID_produto, Produto, Média de Unidades Vendidas, Médias do valor de vendas, Mediana do valor de vendas, Valor máximo de Venda, Valor mínimo de Venda)

> [!NOTE]
> As colunas Média de Unidades Vendidas e Média valor de vendas foram definidas com o tipo decimal fixo.

**3) Tabela Dimensão - D_Descontos** (ID_produto, Discount, Discount Band)

Diferente do apresentado no vídeo do desafio, a tabela *D_Descontos* foi criada utilizando a função *Mesclar Consultas* entre as tabelas *Financials_origem* e *D_Produtos_Detalhes* para obter a coluna *ID_Produto*, pois se houvessem vários tipos de produtos, a utilização da função *Adicionar Coluna Condicional* não seria viável.

```
D_Descontos (ID_produto, Discount, Discount Band)
```

### 4) Tabela Dimensão - D_Produtos_Detalhes:

A tabela *D_Produtos_Detalhes* foi criada da mesma forma da tabela *D_Descontos* utilizando a função *Mesclar Consultas* entre as tabelas *Financials_origem* e *D_Produtos_Detalhes* para obter a coluna *ID_Produto*.

```
D_Produtos_Detalhes(ID_produtos, Discount Band, Sale Price,  Units Sold, Manufactoring Price)
```