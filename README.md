# Projeto final da disciplina Teoria dos Grafos

Alunos: Dennis Felipe Urtubia, Jorge Franzon e Otávio Goes.

## Aplicação do projeto

Este projeto consiste em uma aplicação que, dado dois atores, o programa calcula a distância mais curta em relação a atuação em conjunto entre estes atores.

## Desenvolvimento

O programa foi desenvolvido na linguagem de programação Python e algumas bibliotcas da mesma, sendo elas:

- [https://networkx.github.io](Networkx): como pacote para a criação e manipulação da estrutura de dados.

Cada vértice representa um ator da base de dados. Cada aresta representa uma atuação em conjunto entre dois atores.
/documentation/stable/reference/algorithms/shortest_paths.html
Foi utilizado o método shortest_path da biblioteca citada acima para o cálculo da distância mais curta entre um par de vértices. Este método tem como parâmetros:

- G: grafo a ser aplicada a função
- Source: Vétice de origem
- Target: Vértice de destino

## Base de Dados

Foi utilizada a base de dados TMDB, disponibilizada em https://www.kaggle.com/tmdb/tmdb-movie-metadata a qual disponibiliza os filmes e seus respectivos elencos utilizados para esta aplicação.
