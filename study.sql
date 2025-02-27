-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 27/02/2025 às 13:24
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `study`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `states`
--

CREATE TABLE `states` (
  `id` int(11) NOT NULL,
  `name_estado` varchar(60) NOT NULL,
  `acronym_estado` char(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `states`
--

INSERT INTO `states` (`id`, `name_estado`, `acronym_estado`) VALUES
(1, 'amazonas', 'AM'),
(2, 'Acre', 'AC'),
(3, 'Rio de Janeiro', 'RJ');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `states`
--
ALTER TABLE `states`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `states`
--
ALTER TABLE `states`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
