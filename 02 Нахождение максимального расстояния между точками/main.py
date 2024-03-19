# Четыре точки заданы своими координатами X(x1, x2), Y(y1, y2), Z(z1, z2), P(p1, p2).
# Выяснить, какие из них находятся на максимальном расстоянии друг от друга и вывести на экран значение этого расстояния.

import math


class Solution:
    def __init__(self, x: list, y: list, z: list, p: list):
        self.X = x
        self.Y = y
        self.Z = z
        self.P = p

    @staticmethod
    def distance(point1: list, point2: list) -> float:
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def find_max_distance(self) -> [(float, str, str)]:
        dists = {}

        dists['XY'] = self.distance(self.X, self.Y)
        dists['XZ'] = self.distance(self.X, self.Z)
        dists['XP'] = self.distance(self.X, self.P)

        dists['YZ'] = self.distance(self.Y, self.Z)
        dists['YP'] = self.distance(self.Y, self.P)

        dists['ZP'] = self.distance(self.Z, self.P)

        max_distance = max(dists.values())

        max_distance_pairs = [(key[0], key[1]) for key, value in dists.items() if value == max_distance]

        return [(max_distance, point1, point2) for point1, point2 in max_distance_pairs]

    def __str__(self) -> str:
        return f'X={self.X}, Y={self.Y}, Z={self.Z}, P={self.P}'


X = [-5, 5]
Y = [5, -5]
Z = [5, 5]
P = [-5, -5]

solution = Solution(x=X, y=Y, z=Z, p=P)
max_distance_pairs = solution.find_max_distance()

for distance, point1, point2 in max_distance_pairs:
    print(f'Максимальная дистанция: {distance} между точками {point1} и {point2}')
