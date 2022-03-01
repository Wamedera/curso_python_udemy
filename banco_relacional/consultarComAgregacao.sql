-- agrupa a soma da população de cada região e ordena de forma decrescente
select
    regiao as 'Região',
    sum(populacao) as Total
from estados
group by regiao
order by Total desc;

select
    avg(populacao) as Total
from estados;