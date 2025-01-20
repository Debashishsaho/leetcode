class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows_count, cols_count = len(mat), len(mat[0])
        number_position_index = {}
        for row_index in range(rows_count):
            for col_index in range(cols_count):
                number = mat[row_index][col_index]
                number_position_index[number] = (row_index, col_index)
        row_counters = [0] * rows_count
        col_counters = [0] * cols_count
        for index, number in enumerate(arr):
            if number in number_position_index:
                row_index, col_index = number_position_index[number]
                row_counters[row_index] += 1
                col_counters[col_index] += 1
                if row_counters[row_index] == cols_count or col_counters[col_index] == rows_count:
                    return index
        return -1