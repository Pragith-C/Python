"""Assignment 2 functions."""
"""By Pragith Chenthuran"""

from typing import List


THREE_BY_THREE = [[1, 2, 1],
                  [4, 6, 5],
                  [7, 8, 9]]

FOUR_BY_FOUR = [[1, 2, 6, 5],
                [4, 5, 3, 2],
                [7, 9, 8, 1],
                [1, 2, 1, 4]]

UNIQUE_3X3 = [[1, 2, 3],
              [9, 8, 7],
              [4, 5, 6]]

UNIQUE_4X4 = [[10, 2, 3, 30],
              [9, 8, 7, 11],
              [4, 5, 6, 12],
              [13, 14, 15, 16]]


def compare_elevations_within_row(elevation_map: List[List[int]], map_row: int,
                                  level: int) -> List[int]:
    """Return a new list containing the three counts: the number of
    elevations from row number map_row of elevation map elevation_map
    that are less than, equal to, and greater than elevation level.

    Precondition: elevation_map is a valid elevation map.
                  0 <= map_row < len(elevation_map).

    >>> compare_elevations_within_row(THREE_BY_THREE, 1, 5)
    [1, 1, 1]
    >>> compare_elevations_within_row(FOUR_BY_FOUR, 1, 2)
    [0, 1, 3]

    """
    less_level = 0
    equal_level = 0
    more_level = 0
    for i in range(len(elevation_map[map_row])):
        if elevation_map[map_row][i] < level:
            less_level += 1
        elif elevation_map[map_row][i] == level:
            equal_level += 1
        elif elevation_map[map_row][i] > level:
            more_level += 1
    new_elevation_map = [less_level, equal_level, more_level]
    return new_elevation_map


def update_elevation(elevation_map: List[List[int]], start: List[int],
                     stop: List[int], delta: int) -> None:
    """Modify elevation map elevation_map so that the elevation of each
    cell between cells start and stop, inclusive, changes by amount
    delta.

    Precondition: elevation_map is a valid elevation map.
                  start and stop are valid cells in elevation_map.
                  start and stop are in the same row or column or both.
                  If start and stop are in the same row,
                      start's column <=  stop's column.
                  If start and stop are in the same column,
                      start's row <=  stop's row.
                  elevation_map[i, j] + delta >= 1
                      for each cell [i, j] that will change.

    >>> THREE_BY_THREE_COPY = [[1, 2, 1],
    ...                        [4, 6, 5],
    ...                        [7, 8, 9]]
    >>> update_elevation(THREE_BY_THREE_COPY, [1, 0], [1, 1], -2)
    >>> THREE_BY_THREE_COPY
    [[1, 2, 1], [2, 4, 5], [7, 8, 9]]
    >>> FOUR_BY_FOUR_COPY = [[1, 2, 6, 5],
    ...                      [4, 5, 3, 2],
    ...                      [7, 9, 8, 1],
    ...                      [1, 2, 1, 4]]
    >>> update_elevation(FOUR_BY_FOUR_COPY, [1, 2], [3, 2], 1)
    >>> FOUR_BY_FOUR_COPY
    [[1, 2, 6, 5], [4, 5, 4, 2], [7, 9, 9, 1], [1, 2, 2, 4]]

    """
    start_row = start[0]
    start_column = start[1]
    stop_row = stop[0]
    stop_column = stop[1]
    while start_row <= stop_row and start_column <= stop_column:
        start = [start_row, start_column]
        if start_column == stop_column:
            elevation_map[start_row][start_column] += delta
            start_row += 1
        elif start_row == stop_row:
            elevation_map[start_row][start_column] += delta
            start_column += 1
        elif start == stop:
            elevation_map[start_row][start_column] += delta
            start_column += 1

    
def get_average_elevation(elevation_map: List[List[int]]) -> float:
    """Return the average elevation across all cells in the elevation map
    elevation_map.

    Precondition: elevation_map is a valid elevation map.

    >>> get_average_elevation(UNIQUE_3X3)
    5.0
    >>> get_average_elevation(FOUR_BY_FOUR)
    3.8125
    """
    total = 0
    for total_elements in elevation_map:
        for element in total_elements:
            total += element
    return total/(len(elevation_map)**2)
        

def find_peak(elevation_map: List[List[int]]) -> List[int]:
    """Return the cell that is the highest point in the elevation map
    elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  Every elevation value in elevation_map is unique.

    >>> find_peak(UNIQUE_3X3)
    [1, 0]
    >>> find_peak(UNIQUE_4X4)
    [0, 3]
    """

    max_num = 0
    for total_elements in range(len(elevation_map)):
        for element in range(len(elevation_map[total_elements])):
            if elevation_map[total_elements][element] > max_num:
                max_num = elevation_map[total_elements][element]
                max_point = [total_elements, element]
    return max_point


def is_sink(elevation_map: List[List[int]], cell: List[int]) -> bool:
    """Return True if and only if cell exists in the elevation map
    elevation_map and cell is a sink.

    Precondition: elevation_map is a valid elevation map.
                  cell is a 2-element list.

    >>> is_sink(THREE_BY_THREE, [0, 5])
    False
    >>> is_sink(THREE_BY_THREE, [0, 2])
    True
    >>> is_sink(THREE_BY_THREE, [1, 1])
    False
    >>> is_sink(FOUR_BY_FOUR, [2, 3])
    True
    >>> is_sink(FOUR_BY_FOUR, [3, 2])
    True
    >>> is_sink(FOUR_BY_FOUR, [1, 3])
    False
    """

    row = cell[0]
    column = cell[1]
    em_len = len(elevation_map)
    if in_elevation_map(row, column, em_len):
        for i in range(row-1, row+2):
            for j in range(column-1, column+2):
                if in_elevation_map(i, j, em_len) and \
                   elevation_map[i][j] < elevation_map[row][column]:
                        return False
        return True
    else:
        return False


def find_local_sink(elevation_map: List[List[int]],
                    cell: List[int]) -> List[int]:
    """Return the local sink of cell cell in elevation map elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  elevation_map contains no duplicate elevation values.
                  cell is a valid cell in elevation_map.

    >>> find_local_sink(UNIQUE_3X3, [1, 1])
    [0, 0]
    >>> find_local_sink(UNIQUE_3X3, [2, 0])
    [2, 0]
    >>> find_local_sink(UNIQUE_4X4, [1, 3])
    [0, 2]
    >>> find_local_sink(UNIQUE_4X4, [2, 2])
    [2, 1]
    """
    cell_row = cell[0]
    cell_column = cell[1]
    em_len = len(elevation_map)
    sink = cell
    for i in range(cell_row-1, cell_row+2):
        for j in range(cell_column-1, cell_column+2):
            if in_elevation_map(i, j, em_len):
                if elevation_map[i][j] < elevation_map[sink[0]][sink[1]]:
                    sink = [i, j]
    return sink


def can_hike_to(elevation_map: List[List[int]], start: List[int],
                dest: List[int], supplies: int) -> bool:
    """Return True if and only if a hiker can go from start to dest in
    elevation_map without running out of supplies.

    Precondition: elevation_map is a valid elevation map.
                  start and dest are valid cells in elevation_map.
                  dest is North-West of start.
                  supplies >= 0

    >>> map = [[1, 6, 5, 6],
    ...        [2, 5, 6, 8],
    ...        [7, 2, 8, 1],
    ...        [4, 4, 7, 3]]
    >>> can_hike_to(map, [3, 3], [2, 2], 10)
    True
    >>> can_hike_to(map, [3, 3], [2, 2], 8)
    False
    >>> can_hike_to(map, [3, 3], [3, 0], 7)
    True
    >>> can_hike_to(map, [3, 3], [3, 0], 6)
    False
    >>> can_hike_to(map, [3, 3], [0, 0], 18)
    True
    >>> can_hike_to(map, [3, 3], [0, 0], 17)
    False

    """

    [s_row, s_col] = [start[0], start[1]]
    [d_row, d_col] = [dest[0], dest[1]]
    while supplies >= 0:
        start = [s_row, s_col]
        if start != dest:
            point_value = elevation_map[s_row][s_col]
            dif_col = abs((elevation_map[s_row][s_col-1])- point_value)
            dif_row = abs((elevation_map[s_row-1][s_col])- point_value)
            if s_row == d_row:
                supplies = supplies - dif_col
                s_col -= 1
            elif s_col == d_col:
                supplies = supplies - dif_row
                s_row -= 1
            else:
                if dif_row > dif_col:
                    supplies = supplies - dif_col
                    s_col -= 1
                else:
                    supplies = supplies - dif_row
                    s_row -= 1
        elif start == dest and supplies >= 0:
            return True
    return False


def get_lower_resolution(elevation_map: List[List[int]]) -> List[List[int]]:
    """Return a new elevation map, which is constructed from the values
    of elevation_map by decreasing the number of elevation points
    within it.

    Precondition: elevation_map is a valid elevation map.

    >>> get_lower_resolution(
    ...     [[1, 6, 5, 6],
    ...      [2, 5, 6, 8],
    ...      [7, 2, 8, 1],
    ...      [4, 4, 7, 3]])
    [[3, 6], [4, 4]]
    >>> get_lower_resolution(
    ...     [[7, 9, 1],
    ...      [4, 2, 1],
    ...      [3, 2, 3]])
    [[5, 1], [2, 3]]

    """
    new_em = []
    em_len = len(elevation_map)
    for add_row in range(0, em_len, 2):
        new_elevation_map = []
        for add_col in range(0, em_len, 2):
            total = 0
            count = 0
            matrix_row = 0
            while matrix_row < 2:
                row = matrix_row + add_row
                matrix_row += 1
                matrix_col = 0
                while matrix_col < 2 and \
                      in_elevation_map(row, matrix_col + add_col, em_len):
                    column = matrix_col + add_col
                    matrix_col += 1
                    count = count + 1
                    total = total + elevation_map[row][column]
            average = total // count
            new_elevation_map.append(average)
        new_em.append(new_elevation_map)
    return new_em


#Helper Function
def in_elevation_map(row: int, column: int, len_elevation_map: int) -> bool:
    """Return True if the row and column given is located inside the
    the elevation map of length and height, len_elevation_map.

    >>> in_elevation_map(0, 5, 3)
    False
    >>> in_elevation_map(0, 2, 3)
    True
    >>> in_elevation_map(2, 3, 4)
    True
    >>> in_elevation_map(4, 3, 4)
    False

    """
    if 0 <= row < len_elevation_map:
        if 0 <= column < len_elevation_map:
            return True
        return False
    return False
