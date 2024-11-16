# 📡 Projet de Réseaux d'Interconnexion Statique et Dynamique avec Python

Ce projet présente des exemples de **réseaux d'interconnexion** en utilisant Python et la bibliothèque **NetworkX**. Il inclut des implémentations pour des réseaux statiques (anneau, mesh, arbre, hypercube) ainsi qu'un réseau dynamique avec des ajouts et suppressions de nœuds et d'arcs en temps réel.

## 🗂️ Structure du Projet

```
NetworkX_Project/
├── static/
│   ├── ring_network.py         # Réseau en Anneau
│   ├── mesh_network.py         # Réseau en Mesh
│   ├── tree_network.py         # Réseau en Arbre
│   └── hypercube_network.py    # Réseau en Hypercube
├── dynamic/
│   └── dynamic_network.py      # Réseau Dynamique
├── requirements.txt            # Fichier des dépendances
└── README.md                   # Documentation du projet
```

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir Python installé (version 3.8 ou supérieure). Les bibliothèques nécessaires pour ce projet sont :

- **NetworkX** : pour la création et la manipulation des graphes.
- **Matplotlib** : pour la visualisation des graphes.

### Installation des dépendances

Pour installer les bibliothèques requises, utilisez la commande suivante :

```bash
pip install -r requirements.txt
```

Ou installez-les directement :

```bash
pip install networkx matplotlib
```

## 🛠️ Exemples de Réseaux Statique

Les réseaux statiques sont des réseaux dont la topologie ne change pas après leur création.

### 1. Réseau en Anneau (`ring_network.py`)

Le réseau en anneau est une topologie où chaque nœud est connecté à deux nœuds voisins, formant ainsi un cycle fermé.

Exécution :

```bash
python static/ring_network.py
```

Visualisation :
- Les nœuds sont disposés en forme de cycle.
- Chaque nœud est connecté uniquement à ses voisins immédiats.

### 2. Réseau en Mesh (`mesh_network.py`)

Le réseau en mesh (ou maillé) est une topologie où chaque nœud est connecté à tous les autres nœuds.

Exécution :

```bash
python static/mesh_network.py
```

Visualisation :
- Tous les nœuds sont connectés entre eux.
- Cette topologie est hautement redondante.

### 3. Réseau en Arbre (`tree_network.py`)

Le réseau en arbre est une structure hiérarchique où chaque nœud est connecté à un ou plusieurs nœuds enfants, formant ainsi une arborescence.

Exécution :

```bash
python static/tree_network.py
```

Visualisation :
- La racine de l'arbre se trouve en haut, avec les nœuds enfants en dessous.
- Idéal pour des structures hiérarchiques comme les systèmes de fichiers.

### 4. Réseau en Hypercube (`hypercube_network.py`)

Le réseau en hypercube est une topologie multi-dimensionnelle où les nœuds sont organisés selon des dimensions binaires.

Exécution :

```bash
python static/hypercube_network.py
```

Visualisation :
- Chaque nœud représente une coordonnée dans un espace binaire.
- Utilisé pour des architectures parallèles.

## 🔄 Exemple de Réseau Dynamique

Les réseaux dynamiques sont des réseaux dont la topologie peut changer au fil du temps, avec des ajouts et suppressions de nœuds et d'arcs.

### Réseau Dynamique (`dynamic_network.py`)

Ce script montre l'évolution d'un réseau dynamique :
- Ajout aléatoire d'arcs.
- Suppression aléatoire d'arcs.
- Ajout et suppression de nœuds.

Exécution :

```bash
python dynamic/dynamic_network.py
```

Visualisation :
- Le graphe est mis à jour en temps réel avec des changements dynamiques.
- Utile pour simuler des réseaux évolutifs comme les réseaux sociaux ou les réseaux de capteurs.

## ⚙️ Commandes Utiles

- **Installation des dépendances** :

  ```bash
  pip install -r requirements.txt
  ```

- **Exécution des scripts** :

  ```bash
  python static/ring_network.py
  python static/mesh_network.py
  python static/tree_network.py
  python static/hypercube_network.py
  python dynamic/dynamic_network.py
  ```

## 📊 Technologies Utilisées

- **Python** : Langage de programmation principal.
- **NetworkX** : Bibliothèque pour la création et la manipulation de graphes.
- **Matplotlib** : Bibliothèque pour la visualisation des graphes.

## 🚀 Objectifs du Projet

- Illustrer différentes topologies de réseaux statiques.
- Démontrer l'évolution d'un réseau dynamique en temps réel.
- Offrir une base pour l'analyse et la visualisation des réseaux interconnectés.

## 📝 Références

- [Documentation NetworkX](https://networkx.github.io/documentation/stable/)
- [Documentation Matplotlib](https://matplotlib.org/stable/contents.html)

## 👨‍💻 Auteur

- Ce projet a été réalisé dans le cadre d'un projet académique pour illustrer les concepts des réseaux d'interconnexion statiques et dynamiques.

---

