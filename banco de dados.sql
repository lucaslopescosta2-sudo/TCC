CREATE DATABASE db_almox;
USE db_almox;

CREATE TABLE estoque(
	id INT PRIMARY KEY AUTO_INCREMENT, 
    nome VARCHAR(100) NOT NULL, 
    quantidade_disponivel INT NOT NULL, 
    quantidade_minima INT NOT NULL, 
    preco DECIMAL (10,2)  NOT NULL, 
    descricao VARCHAR(100), 
    categoria VARCHAR(100) NOT NULL, 
    imagem VARCHAR(255)
    );

CREATE TABLE usuarios(
	id INT PRIMARY KEY AUTO_INCREMENT, 
    usuario VARCHAR(100) NOT NULL, 
    senha VARCHAR(100) NOT NULL,
    permissao VARCHAR(100)
    );

INSERT INTO usuarios (usuario, senha) 
VALUES ('eduardo@gmail.com','$2a$12$fmIM8ozrPC4qHgqX92DzceDCMURchR.bk9uUzWjETY0mtkIhGIfVS');

INSERT INTO usuarios (usuario, senha)
VALUES ('vitor@gmail.com','$2a$12$ovEcR.GU3Hsb3v69Mjt3puscM5x2anJI/GwbcYiFoWQDv.w6Pbdy6');

INSERT INTO usuarios (usuario, senha) 
VALUES ('lucas@gmail.com','$2a$12$hEuZMsE/GaTxAJxCbyv6EuN1p3cp310kWyO/PDhfr.ZPBIvVZR0G2');

INSERT INTO estoque (nome, quantidade_disponivel, quantidade_minima, preco, descricao, categoria, imagem) 
VALUES ('Martelo', 32, 2, 53.90, 'para pregar', 'ferramenta', 'https://cdn.leroymerlin.com.br/products/martelo_unha_cabo_de_plastico_28,8cm_dexter_90114150_0001_300x300.jpg');

INSERT INTO estoque (nome, quantidade_disponivel, quantidade_minima, preco, descricao, categoria, imagem) 
VALUES ('Chave de Fenda', 22, 2, 22.90, 'para apertar','ferramenta', 'https://cdn.leroymerlin.com.br/products/chave_de_fenda_7_32x4_dexter_89573295_8dbf_300x300.jpeg');

INSERT INTO estoque (nome, quantidade_disponivel, quantidade_minima, preco, descricao, categoria, imagem) 
VALUES ('Chave Phillips', 20, 2, 18.90, 'para aperta','ferramenta', 'https://cdn.leroymerlin.com.br/products/chave_phillips_ph1x80mm_dexter__89680150_0001_300x300.jpg');

INSERT INTO estoque (nome, quantidade_disponivel, quantidade_minima, preco, descricao, categoria, imagem) 
VALUES ('Parafusadeira', 11, 2, 300.75, 'para aperta','ferramenta', 'https://cdn.leroymerlin.com.br/products/parafusadeira_furadeira_3_8_18v_ipfv1820_vonder_1566901668_2b3d_300x300.jpg');

INSERT INTO estoque (nome, quantidade_disponivel, quantidade_minima, preco, descricao, categoria, imagem) 
VALUES ('Furadeira', 8, 2, 831.90, 'para furar','ferramenta', 'https://cdn.leroymerlin.com.br/products/martelete_sds_plus_820w_gbh_2_24_d_com_maleta_220v_bosch_89974934_16ac_300x300.jpg');

INSERT INTO estoque (nome, quantidade_disponivel, quantidade_minima, preco, descricao, categoria, imagem) 
VALUES ('Capacete', 40, 2, 97.90, 'proteger a cabeça','EPIs', 'https://cdn.leroymerlin.com.br/products/capacete_de_seguranca_h_701_branco_3m_91960001_ea5f_300x300.jpg');

INSERT INTO estoque (nome, quantidade_disponivel, quantidade_minima, preco, descricao, categoria, imagem) 
VALUES ('Óculos de Proteção', 42, 2, 7.19, 'para proteger os olhos','EPIs', 'https://cdn.leroymerlin.com.br/products/oculos_de_seguranca_incolor_spectra_2000_carbografite_89257924_e881_300x300.jpg');

INSERT INTO estoque (nome, quantidade_disponivel, quantidade_minima, preco, descricao, categoria, imagem) 
VALUES ('Luva', 26, 2, 4.99, 'para proteger as mãos','EPIs', 'https://cdn.leroymerlin.com.br/products/luva_servicos_gerais_grande_flextactil_danny_92345813_e573_300x300.jpg');

INSERT INTO estoque (nome, quantidade_disponivel, quantidade_minima, preco, descricao, categoria, imagem) 
VALUES ('Calçado de Segurança', 38, 2, 139.90, 'para proteger os pés','EPIs', 'https://cdn.leroymerlin.com.br/products/bota_de_seguranca_em_cadarco_no40_biqueira_plastica_dexter_90976515_3e61_300x300.jpg');

INSERT INTO estoque (nome, quantidade_disponivel, quantidade_minima, preco, descricao, categoria, imagem) 
VALUES ('Colete de Segurança', 72, 2, 39.90, 'para sinalização visual','EPIs', 'https://cdn.leroymerlin.com.br/products/colete_faixa_sinalizador_refletivo_seguranca_trabalho_epi_blu_1568662138_d9b6_300x300.jpg');


select * from usuarios;
select * from estoque;