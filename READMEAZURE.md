
# Desafio - Criando um Dashboard corporativo com integração com MySQL e Azure

Esse arquivo tem o intuito de documentar os passos realizados para a conclusão do desafio.




## João Paulo Nogueira da Silva

- [@joaopaulonsilva](https://github.com/joaopaulonsilva/projetos/tree/main)

## Links

 - [Relatório Power BI](https://github.com/joaopaulonsilva/projetos/blob/main/Criando%20um%20Dashboard%20corporativo%20com%20integra%C3%A7%C3%A3o%20com%20MySQL%20e%20Azure.pbix)
   
## Consulta SQL

Código criado para junção dos colaboradores e respectivos nomes dos gerentes.

```SQL
select concat(b.fname, ' ', b.minit, ' ',b.lname) as Gerente, concat(a.fname, ' ', a.minit, ' ',a.lname) as Colaborador 
from Employee as a left join Employee as b 
on a.super_ssn = b.ssn;
```


## Telas do Desafio

![Relacionamentos entre tabelas](https://github.com/joaopaulonsilva/projetos/blob/main/relacionamentos.JPG)



