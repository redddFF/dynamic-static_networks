import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import random

# Créer le graphe initial avec une structure en chemin (5 nœuds connectés en série)
G = nx.path_graph(5)
movements = []  # Liste pour stocker les mouvements dynamiques
current_step = [0]  # Étape actuelle (utiliser une liste pour une valeur mutable)

# Générer des mouvements dynamiques (ajouts/suppressions d'arcs et de nœuds)
# 1. Ajout dynamique d'arcs
for _ in range(5):
    u, v = random.randint(0, 4), random.randint(0, 4)
    if u != v and not G.has_edge(u, v):
        # Ajouter un mouvement d'ajout d'arc entre deux nœuds aléatoires
        movements.append(("add_edge", (u, v)))

# 2. Suppression dynamique d'arcs
for _ in range(3):
    if G.edges:
        edge = random.choice(list(G.edges))
        # Ajouter un mouvement de suppression d'un arc existant
        movements.append(("remove_edge", edge))

# 3. Ajout dynamique de nœuds (nœuds 5, 6 et 7)
for i in range(5, 8):
    # Ajouter un mouvement d'ajout de nœud et connexion à un nœud existant
    movements.append(("add_node", i))
    movements.append(("add_edge", (i, random.randint(0, 4))))

# 4. Suppression dynamique de nœuds (nœuds 5, 6 et 7)
for i in range(5, 8):
    # Ajouter un mouvement de suppression du nœud
    movements.append(("remove_node", i))

# Fonction pour dessiner le graphe avec des commentaires
def draw_graph(G, title, comments):
    """
    Dessine le graphe actuel avec le titre spécifié et ajoute des annotations.
    """
    ax.clear()  # Effacer l'affichage précédent
    pos = nx.spring_layout(G)  # Disposition du graphe
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', ax=ax)
    ax.set_title(title)  # Ajouter le titre

    # Ajouter des annotations pour chaque mouvement
    for i, comment in enumerate(comments):
        ax.text(0.05, 0.95 - 0.05 * i, comment, transform=ax.transAxes, fontsize=10, verticalalignment='top', color='red')

    plt.draw()  # Redessiner le graphe

# Fonction pour mettre à jour le graphe avec commentaires
def update_graph(step):
    """
    Met à jour le graphe jusqu'à l'étape donnée et affiche des commentaires.
    """
    G.clear()  # Réinitialiser le graphe
    G.add_edges_from(nx.path_graph(5).edges)  # Restaurer le graphe initial

    # Liste des commentaires pour chaque étape
    comments = []

    # Appliquer les mouvements jusqu'à l'étape actuelle
    for i in range(step):
        action, data = movements[i]
        if action == "add_edge":
            # Ajouter un arc entre deux nœuds
            G.add_edge(*data)
            comments.append(f"Ajout de l'arc: {data}")
        elif action == "remove_edge" and G.has_edge(*data):
            # Supprimer un arc existant
            G.remove_edge(*data)
            comments.append(f"Suppression de l'arc: {data}")
        elif action == "add_node":
            # Ajouter un nœud au graphe
            G.add_node(data)
            comments.append(f"Ajout du nœud: {data}")
        elif action == "remove_node" and G.has_node(data):
            # Supprimer un nœud du graphe
            G.remove_node(data)
            comments.append(f"Suppression du nœud: {data}")

    # Redessiner le graphe avec le titre et les commentaires
    draw_graph(G, f"Étape : {step}/{len(movements)}", comments)

# Fonction pour le bouton "Suivant"
def next_step(event):
    """
    Passe à l'étape suivante et met à jour le graphe avec les commentaires.
    """
    if current_step[0] < len(movements):
        current_step[0] += 1
        update_graph(current_step[0])

# Fonction pour le bouton "Précédent"
def prev_step(event):
    """
    Revient à l'étape précédente et met à jour le graphe avec les commentaires.
    """
    if current_step[0] > 0:
        current_step[0] -= 1
        update_graph(current_step[0])

# Configuration de la figure et des axes pour le dessin et les boutons
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.2)

# Création des boutons "Précédent" et "Suivant"
ax_prev = plt.axes([0.1, 0.05, 0.1, 0.075])
ax_next = plt.axes([0.8, 0.05, 0.1, 0.075])
btn_prev = Button(ax_prev, 'Précédent')
btn_next = Button(ax_next, 'Suivant')

# Connexion des boutons aux fonctions correspondantes
btn_prev.on_clicked(prev_step)
btn_next.on_clicked(next_step)

# Afficher le graphe initial
update_graph(current_step[0])

# Afficher la fenêtre de visualisation
plt.show()
