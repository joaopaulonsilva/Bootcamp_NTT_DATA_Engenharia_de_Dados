
# Desafio - Modelando um Dashboard de E-commerce com Power BI Utilizando Fórmulas DAX

Esse arquivo tem o intuito de documentar os passos realizados para a conclusão do desafio Modelando um Dashboard de E-commerce com Power BI Utilizando Fórmulas DAX.

## Star Schema da Sample Financials
![Star Schema da Sample Financials](https://github.com/joaopaulonsilva/Bootcamp_NTT_DATA_Engenharia_de_Dados/blob/main/Desafios/Modelando%20um%20Dashboard%20de%20E-commerce%20com%20Power%20BI%20Utilizando%20F%C3%B3rmulas%20DAX/assets/star_schema_financial.png)

## Criação das tabelas
Todas as tabelas foram criadas seguindo os passos do arquivo [Descrição do Desafio - Modelagem e Transformação de dad.docx](https://academiapme-my.sharepoint.com/:w:/g/personal/renato_dio_me/EW76WjPAA8RGgC3i44ofFq4BBiWzM-CN5S312YwOQCIwBA?rtime=t_QJoWzv3Eg)

> [!TIP]
> Diferente do apresentado no vídeo do desafio, todas as tabelas que contem a coluna *ID_Produto* foram criadas utilizando a função *Mesclar Consultas* entre as tabelas *Financials_origem* e *D_Produtos*, pois se houvessem vários tipos de produtos, a utilização da função *Adicionar Coluna Condicional* não seria viável.


**1) Tabela Fato - F_Vendas** (SK_ID , ID_Produto, Produto, Units Sold, Sales Price, Discount  Band, Segment, Country, Salers, Profit, Date (campos))

**2) Tabela Dimensão - D_Produtos** (ID_produto, Produto, Média de Unidades Vendidas, Médias do valor de vendas, Mediana do valor de vendas, Valor máximo de Venda, Valor mínimo de Venda)

> [!TIP]
> As colunas Média de Unidades Vendidas e Média valor de vendas foram definidas com o tipo decimal fixo.

**3) Tabela Dimensão - D_Descontos** (ID_produto, Discount, Discount Band)

**4) Tabela Dimensão - D_Produtos_Detalhes** (ID_produtos, Discount Band, Sale Price,  Units Sold, Manufactoring Price)

**5) Tabela Dimensão - D_Detalhes** (*)

**5) Tabela Dimensão - D_Data** - Criada por DAX com calendar()
>[!NOTE]
> Conforme desafio, a criação da tabela D_Data se deu por DAX conforme funções abaixo:

- Tabela D_Data - D_Data = {c:blue}CALENDARAUTO({/c}{c:green}12{/c}{c:blue}){/c}
- Year = YEAR('D_Data'[Date])
- Month Number = MONTH('D_Data'[Date])
- Week Number = WEEKNUM('D_Data'[Date])
- Weeks Day = FORMAT('D_Data'[Date], "DDDD")
- Day of the week = WEEKDAY('D_Data'[Date])