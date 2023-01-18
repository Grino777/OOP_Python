class Vertex:
    '''для представления вершин графа (на карте это могут быть: здания, остановки, достопримечательности и т.п.)'''

    def __init__(self):
        self._links = []  # список связей с другими вершинами графа (список объектов класса Link)

    @property
    def links(self):
        return self._links


class Link:
    '''для описания связи между двумя произвольными вершинами графа (на карте: маршруты, время в пути и т.п.)'''

    def __init__(self, v1, v2, dist=1):
        self._v1 = v1  # объект класса Vertex (вершина графа)
        self._v2 = v2
        self._dist = dist  # длина связи (по умолчанию 1); это может быть длина пути, время в пути и др

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist


class LinkedGraph:
    '''для представления связного графа в целом (карта целиком)'''

    def __init__(self):
        self._links = []  # список из всех связей графа (из объектов класса Link);
        self._vertex = []  # список из всех вершин графа (из объектов класса Vertex).

    def add_vertex(self, vertex):
        '''для добавления новой вершины v в список _vertex (если она там отсутствует)'''
        if vertex not in self._vertex:
            self._vertex.append(vertex)

    def add_link(self, link):
        '''для добавления новой связи link в список _links (если объект link с указанными вершинами в списке отсутствует).
        при добавлении новой связи следует автоматически добавлять вершины этой связи в список _vertex, если они там отсутствуют.'''
        t = tuple(filter(lambda x: (id(x.v1) == id(link.v1) and id(x.v2) == id(link.v2)) or \
                                   (id(x.v2) == id(link.v1) and id(x.v1) == id(link.v2)), self._links))

        if len(t) == 0:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)

    def find_path(self, start_v, stop_v):
        '''должен возвращать список из вершин кратчайшего маршрута и список из связей этого же маршрута в виде кортежа:
            ([вершины кратчайшего пути], [связи между вершинами])'''
        self._start_v = start_v
        self._stop_v = stop_v
        return self._next(self._start_v, None, [], [])

    def _dist_path(self, links):
        return sum([x.dist for x in links if x is not None])

    def _next(self, current, link_prev, current_path, current_links):
        current_path += [current]
        if link_prev:
            current_links += [link_prev]

        if current == self._stop_v:
            return current_path, current_links

        len_path = -1
        best_path = []
        best_links = []
        for link in current.links:
            path = []
            links = []
            if link.v1 not in current_path:
                path, links = self._next(link.v1, link, current_path[:], current_links[:])
            elif link.v2 not in current_path:
                path, links = self._next(link.v2, link, current_path[:], current_links[:])

            if self._stop_v in path and (len_path > self._dist_path(links) or len_path == -1):
                len_path = self._dist_path(links)
                best_path = path[:]
                best_links = links[:]

        return best_path, best_links


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2, dist)

    def __repr__(self):
        return f'{self.v1.name} - {self.v2.name}'


# Тесты:
map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(map_metro._vertex[1].links)
print(len(map_metro._links))
print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])  # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7


