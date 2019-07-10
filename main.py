import pandas as pd
import networkx as nx
import json
import matplotlib
import matplotlib.pyplot as plt

G = nx.Graph()

movies = 5000
actors = 224
plot = False

print('Lendo dataset')

dataset = pd.read_csv('./tmdb.csv')[:movies]
dataset.drop(['crew'], inplace=True, axis=1)

print('Construindo grafo')

for index, row in dataset.iterrows():
    movie_id = row['movie_id']
    title = row['title']
    cast = json.loads(row['cast'])

    for actor in cast[:actors]:
        if not G.has_node(actor['name']):
            G.add_node(actor['name'])

        for another_actor in cast[:actors]:
            if actor['name'] != another_actor['name']:
                G.add_edge(actor['name'], another_actor['name'],
                           color='black', weight=1)

print('Grafo construido. Numero de atores: ', len(G))

while True:

    actor1 = input('Digite o primeiro ator: ')
    actor2 = input('Digite o segundo ator: ')

    try:
        shortest_path = nx.shortest_path(G, actor1, actor2)
        print('Foi encontrado um caminho entre os dois atores!')
        print('A distância mínima é ', len(shortest_path)-1)
        print('O caminho percorrido foi: ')
        for sp in shortest_path:
            print('\t' + sp)
        print('')

        if plot:

            print('Plotando grafo')
            plt.figure(3, figsize=(100, 100))
            pos = nx.circular_layout(G)

            pairs = [(shortest_path[i], shortest_path[i+1])
                     for i in range(len(shortest_path)-1)]

            edges = G.edges(data=True)
            for u, v, d in edges:
                if (u, v) in pairs or (v, u) in pairs:
                    d['color'] = 'red'
                    d['weight'] = 20

            colors = [G[u][v]['color'] for u, v, d in edges]
            weights = [G[u][v]['weight'] for u, v, d in edges]

            for node in G.nodes():
                G.nodes.get(node)[
                    'size'] = 1000 if node == actor1 or node == actor2 else 5

            sizes = [G.nodes.get(i)['size'] for i in G.nodes.keys()]

            nx.draw(G, pos,  node_size=sizes, edges=edges, with_labels=True,
                    edge_color=colors,  width=weights)

            plt.savefig('graph.png')
            print('Grafico salvo em graph.png')
    except:
        print('Não foi possível encontrar um caminho entre os dois atores\n')
