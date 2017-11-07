
from functools import partial
from math import fsum, sqrt
from pprint import pprint
from random import sample
from typing import Iterable, Tuple, List, Sequence, Dict
from dis import dis
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Alias dla struktury
from collections import defaultdict

Point = Tuple[int, ...]
Centroid = Point

points = [
        (10, 41, 23),
        (22, 30, 29),
        (11, 42, 5),
        (20, 32, 4),
        (12, 40, 12),
        (21, 36, 23),
    ]


def mean(data: Iterable[float]) -> float:
    """Acurate arithmetic mean"""
    data = list(data)
    return fsum(data) / len(data)


def dist_(p, q):
    """Euclidean distance function for multi-dimensional data"""
    return sqrt(fsum([(x - y) ** 2 for x, y in zip(p, q)]))


# Przykład na lokalizację funkcji w celu przyspieczenia
def dist(p: Point, q: Point, fsum=fsum, sqrt=sqrt, zip=zip) -> float:
    """Euclidean distance function for multi-dimensional data"""
    return sqrt(fsum([(x - y) ** 2 for x, y in zip(p, q)]))


# O co chodzi?
print(dis(dist))


def assign_data(centroids: Sequence[Centroid], data: Iterable[Point]) -> Dict[Centroid, List[Point]]:
    """Group the data points to the centroid"""
    d = defaultdict(list)
    for point in data:
        closest_centroid = min(centroids, key=partial(dist, point))
        d[closest_centroid].append(point)
    return dict(d)


for point in points:
    print(point, dist(point, (9, 39, 20)))


# --- Niesamowity ciąg myślowy
centroids = [(9, 39, 20), (12, 36, 25)]
point = (11, 42, 5)
# mamy jednen point i zasatanawiamy sie do którego centroids jest blizej?
[dist(point, centroid) for centroid in centroids]
# następnie wystarczy użyć min()
min([dist(point, centroid) for centroid in centroids])
# problem w tym że zwraca odległość a nie centroid do którego jest najbliżej
# Czy jest proste rozwiązanie?
min(centroids, key=lambda centroid: dist(point, centroid))
#    ^== Big idea, little code
# używając partial() mozna jeszcze bardziej skrócić
min(centroids, key=partial(dist, point))

# --- partial
pow(2, 5)

twopow = partial(pow, 2)  # freeze first arg in pow()
twopow(5)


# Example
"""Obliczyć srednie dla i-th elementów"""
group = [
    (10, 41, 23),
    (22, 30, 29),
    (11, 42, 5),
    (20, 32, 4),
    (12, 40, 12),
]
pprint(group, width=40)
list(zip(*group))
tuple(map(mean, zip(*group)))


def compute_centroids(groups: Iterable[Sequence[int]]) -> List[Centroid]:
    """Compute the centroid of each group"""
    return [tuple(map(mean, zip(*group))) for group in groups]


def k_mean(data: Iterable[Point], k: int=2, iterations: int=50) -> List[Centroid]:
    data = list(data)
    centroids = sample(data, k)
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroids(labeled.values())
    return centroids


points = [
    (10, 41, 23),
    (22, 30, 29),
    (11, 42, 5),
    (20, 32, 15),
    (12, 40, 12),
    (21, 36, 23),
]

centroids = k_mean(points, k=2)
d = assign_data(centroids, points)
pprint(d, width=45)

# --- Rysujemy

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

"""Klastry z kolorami"""
for points, color in zip(d.values(), ['r', 'b']):
    plot_data = list(zip(*points))
    """TIP: moża czytelniej i prościej
    X = plot_data[0]
    Y = plot_data[1]
    Z = plot_data[2]
    """
    X, Y, Z = plot_data
    ax.scatter(X, Y, Z, c=color, marker='o')

"""Centroids"""
for point, color in zip(d.keys(), ['r', 'b']):
    X = point[0]
    Y = point[1]
    Z = point[2]
    ax.scatter(X, Y, Z, c=color, marker='*')

plt.show()