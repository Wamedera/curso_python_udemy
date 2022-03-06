alter table empresas modify cnpj varchar(14);

insert into empresas
    (nome, cnpj)
values
    ('Bradesco', 18631583000114),
    ('Vale', 69629911000189),
    ('Cielo', 92266798000136);

desc empresas;
desc prefeitos;
select * from empresas;
select * from cidades;

insert into empresas_unidades
    (empresa_id, cidade_id, sede)
values
    (1, 17, 1),
    (1, 18, 0),
    (2, 17, 0),
    (2, 18, 1);