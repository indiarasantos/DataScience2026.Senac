USE meu_ecommerce;

DROP 

-- CRIANDO A ENTIDADE CLIENTES:

CREATE TABLE Clientes (
id_cliente VARCHAR(10),
nome VARCHAR(100),
email VARCHAR(30)
);

-- DELETE FROM Clientes WHERE id_cliente = "id_cliente";

-- CRIANDO A ENTIDADE PEDIDOS:

CREATE TABLE Pedidos (
id_pedido VARCHAR(10),
id_cliente VARCHAR(10),
data_pedido DATETIME,
valor_total DECIMAL(10,2),
id_produto VARCHAR(10),
quantidade SMALLINT
);


-- OPÇÕES DE CONSTRUÇÃO DE CHAVES:
-- 1. DESDE O CREATE TABLE:
CREATE TABLE Pedidos (
id_pedido INT NOT NULL PRIMARY KEY, -- NOT NULL - NÃO VAZIO
data_pedido DATE,
valor_total DECIMAL(10,2),
id_cliente INT,
id_produto INT,
quantidade INT,
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);
-- OU
CREATE TABLE Pedidos (
id_pedido INT AUTO_INCREMENT PRIMARY KEY, -- PREENCHIMENTO AUTOMÁTICO
data_pedido DATE,
valor_total DECIMAL(10,2),
id_cliente INT,
id_produto INT,
quantidade INT,
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

-- 2. USANDO ALTER TABLE COM A TABELA JÁ CRIADA:
ALTER TABLE produtos
ADD CONSTRAINT pk_produtos
PRIMARY KEY (id_produto);

ALTER TABLE clientes
ADD CONSTRAINT pk_clientes
PRIMARY KEY (id_cliente);

ALTER TABLE pedidos
ADD CONSTRAINT pk_pedidos
PRIMARY KEY (id_pedido);

ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_clientes
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente);

ALTER TABLE pedidos
ADD CONSTRAINT fk_pedidos_produtos
FOREIGN KEY (id_produto) REFERENCES produtos(id_produto);
