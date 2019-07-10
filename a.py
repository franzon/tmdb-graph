import pandas as pd
import networkx as nx
import json
import matplotlib.pyplot as plt

G = nx.Graph()

movies = 5000
actors = 10

dataset = pd.read_csv('./tmdb.csv')[:movies]
dataset.drop(['crew'], inplace=True, axis=1)

for index, row in dataset.iterrows():
    movie_id = row['movie_id']
    title = row['title']
    cast = json.loads(row['cast'])
    for actor in cast[:actors]:
        if not G.has_node(actor['name']):
            G.add_node(actor['name'])
            
        for another_actor in cast[:actors]:
            if actor['name'] != another_actor['name']:
                G.add_edge(actor['name'], another_actor['name'])
        

# plt.figure(3,figsize=(100,100)) 
# pos = nx.circular_layout(G)
# nx.draw(G,pos, with_labels = True)
# plt.show()
# plt.savefig('foo.png')

print('Número total de Atores: ', len(G))
try:
    res = nx.shortest_path(G, 'Antonio Banderas', 'Robert Pattinson')
    dist = len(res) - 2

    if (dist == 0):
        print("Atores já atuaram juntos")
    
    elif (dist > 1):
        print("Distância entre atores: {}".format(dist),"\n", res)
except:
    print("Não encontrado na base")
