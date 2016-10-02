class Island(object):
    def __init__(self, num_of_rows, num_of_cols):
        """Функция инициализирует объект класса"""
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols
        self.cells = []
        self.heights = []
        self.coordinates_of_heights = {}
        self.rainwater = 0

    def add_row_from_string(self, string, num_of_row):
        """Функция обрабатывает введенную строку острова"""
        row = [int(x) for x in string.split()]
        self.add_heights(row, num_of_row)
        self.cells.append(row)

    def add_heights(self, row, num_of_row):
        """Функция добавляет недостающие высоты в список высот"""
        for num_of_col, x in enumerate(row):
            self.add_coordinates_of_heights(x, num_of_row, num_of_col)
            if x not in self.heights:
                self.heights.append(x)

    def is_edge_cell(self, x, y):
        """Функция проверяет, является ли ячейка граничной"""
        if x == 0 or x == self.num_of_rows - 1:
            return True
        elif y == 0 or y == self.num_of_cols - 1:
            return True
        else:
            return False

    def in_island(self, x, y):
        """Функция проверяет, в границах ли острова ячейка"""
        if (0 <= x < self.num_of_rows and 0 <= y < self.num_of_cols):
            return True
        else:
            return False

    def add_coordinates_of_heights(self, x, num_of_row, num_of_col):
        """Функция создает словарь, ключ - высота, значение - координаты высот"""
        if x not in self.coordinates_of_heights:
            self.coordinates_of_heights[x] = [(num_of_row, num_of_col)]
        else:
            self.coordinates_of_heights[x].append((num_of_row, num_of_col))

    def identify_areas(self, height):
        """Функция обрабатывает ячейки переданной высоты"""

        def get_neighbors(list_of_cells):
            """Функция ищет соседей для элементов списка в списке cells
            Также, между делом, вычисляет минимального соседа для ячеек"""
            result = []
            nonlocal minimum
            for cell in list_of_cells:
                if self.in_island(cell[0], cell[1] + 1):
                    if (cell[0], cell[1] + 1) in cells:
                        result.append(cells.pop(cells.index((cell[0], cell[1] + 1))))
                    else:
                        if (self.cells[cell[0]][cell[1] + 1] < minimum and
                            self.cells[cell[0]][cell[1] + 1] != height):
                            minimum = self.cells[cell[0]][cell[1] + 1]
                if self.in_island(cell[0] + 1, cell[1]):
                    if (cell[0] + 1, cell[1]) in cells:
                        result.append(cells.pop(cells.index((cell[0] + 1, cell[1]))))
                    else:
                        if (self.cells[cell[0] + 1][cell[1]] < minimum and
                            self.cells[cell[0] + 1][cell[1]] != height):
                            minimum = self.cells[cell[0] + 1][cell[1]]
                if self.in_island(cell[0], cell[1] - 1):
                    if (cell[0], cell[1] - 1) in cells:
                        result.append(cells.pop(cells.index((cell[0], cell[1] - 1))))
                    else:
                        if (self.cells[cell[0]][cell[1] - 1] < minimum and
                            self.cells[cell[0]][cell[1] - 1] != height):
                            minimum = self.cells[cell[0]][cell[1] - 1]
                if self.in_island(cell[0] - 1, cell[1]):
                    if (cell[0] - 1, cell[1]) in cells:
                        result.append(cells.pop(cells.index((cell[0] - 1, cell[1]))))
                    else:
                        if (self.cells[cell[0] - 1][cell[1]] < minimum and
                            self.cells[cell[0] - 1][cell[1]] != height):
                            minimum = self.cells[cell[0] - 1][cell[1]]
            return result

        cells = self.coordinates_of_heights[height]

        while cells:
            minimum = 1001
            start_cell = cells.pop(0)
            is_edge = self.is_edge_cell(start_cell[0], start_cell[1])

            current_area = [start_cell]
            neighbors = get_neighbors([start_cell])
            while neighbors:
                if not is_edge:
                    for neighbor in neighbors:
                        if self.is_edge_cell(neighbor[0], neighbor[1]):
                            is_edge = True
                            break

                current_area.extend(neighbors)
                neighbors = get_neighbors(neighbors)

            if not is_edge and minimum > height: # Для всех неграничных областей,
                                                 # которые являются минимумами,
                                                 # добавляем дождевой воды
                self.rainwater += (minimum - height) * len(current_area)
                for item in current_area:
                    self.coordinates_of_heights[minimum].append(item)
                    self.cells[item[0]][item[1]] += minimum - height

def main():
    num_of_islands = int(input('Введите количество островов: '))
    for _ in range(num_of_islands): # Пробегаемся по всем островам
        island = Island(*[int(x) for x in input('Введите размеры: ').split()])
        # Инициализируем остров
        for num_of_row in range(island.num_of_rows): # Заполняем остров
            island.add_row_from_string(input(), num_of_row)
        island.heights.sort() # Сортируем список высот

        for height in island.heights:
            island.identify_areas(height) # Обрабатываем высоты
        print(island.rainwater)

if __name__ == '__main__':
    main()
