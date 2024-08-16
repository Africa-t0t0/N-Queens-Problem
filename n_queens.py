class QueensSolution(object):
    _large = None
    _solution_ls = None
    _table_ls = None
    _max_queens = None

    def __init__(self,  large: int) -> None:
        self._large = large
        self._solution_ls = list()

    def _get_large(self) -> int:
        return self._large

    def _get_table(self) -> list:
        if self._table_ls is None:
            self._set_table()
        return self._table_ls

    def _get_max_queens(self) -> int:
        max_queens = self._max_queens
        return max_queens

    def _set_table(self) -> None:
        large = self._get_large()
        table = [[0 for _ in range(large)] for _ in range(large)]
        self._table_ls = table

    def _set_max_queens(self, value: int) -> None:
        self._max_queens = value

    @staticmethod
    def _print_current_table(table_ls: list) -> None:
        print("------------------")
        for array in table_ls:
            print(array)

    @staticmethod
    def _set_queen_greedy(position_x: int, position_y: int, table_ls: list):
        # set the X axis
        table_ls[position_x] = [1 for _ in table_ls[position_x]]
        # set the Y axis
        for array in table_ls:
            array[position_y] = 1
        # set diagonal
        aux_x_up_right = position_x
        aux_x_up_left = position_x
        aux_x_down_right = position_x
        aux_x_down_left = position_x
        aux_y_up_right = position_y
        aux_y_up_left = position_y
        aux_y_down_right = position_y
        aux_y_down_left = position_y
        while True:
            flag_change = False
            # check up right diagonal
            if aux_y_up_right + 1 < len(table_ls) and (aux_x_up_right - 1 < len(table_ls) and (aux_x_up_right > 0)):
                aux_y_up_right += 1
                aux_x_up_right -= 1
                table_ls[aux_x_up_right][aux_y_up_right] = 1
                flag_change = True
            # # check up left diagonal
            if aux_y_up_left - 1 >= 0 and aux_x_up_left - 1 >= 0:
                aux_y_up_left -= 1
                aux_x_up_left -= 1
                table_ls[aux_x_up_left][aux_y_up_left] = 1
                flag_change = True
            # check down right diagonal
            if aux_y_down_right + 1 < len(table_ls) and aux_x_down_right + 1 < len(table_ls):
                aux_y_down_right += 1
                aux_x_down_right += 1
                table_ls[aux_x_down_right][aux_y_down_right] = 1
                flag_change = True
            # check down left diagonal
            if aux_y_down_left - 1 >= 0 and aux_x_down_left + 1 < len(table_ls):
                aux_y_down_left -= 1
                aux_x_down_left += 1
                table_ls[aux_x_down_left][aux_y_down_left] = 1
                flag_change = True

            if not flag_change:
                break
        table_ls[position_x][position_y] = "X"
        return table_ls

    def greedy_solution(self):
        table_ls = self._get_table()
        max_queens = 0

        for index in range(len(table_ls)):
            for index2 in range(len(table_ls)):
                if table_ls[index][index2] == 0:
                    table_ls = self._set_queen_greedy(position_x=index,
                                                      position_y=index2,
                                                      table_ls=table_ls)
                    max_queens += 1
        self._set_max_queens(value=max_queens)
        self._print_current_table(table_ls)


QueensSolution(large=12).greedy_solution()
