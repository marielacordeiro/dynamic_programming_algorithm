from cmath import inf
import os
import sys
visited = {}
best = 0


def read_file(test_case: str):
    matrix = []

    with open(f'testes/{test_case}') as f:
        n = f.readline()
        for line in f:
            matrix.append(list(line.split()))

    return matrix, n


def print_field(list):
    for y in range(len(list)):
        for x in range(len(list[0])):
            print(list[y][x], end=' ')
            if x == len(list[0])-1:
                print('\n')


def RecursivePath(i, j, size, grid):

    if (i < 0 or j > size - 1):
        return -inf

    if (i == 0 and j == size - 1):
        return int(grid[0][size - 1])

    if (grid[i][j] == "x"):
        return -inf

    return max(RecursivePath(i - 1, j, size, grid),
               RecursivePath(i - 1, j + 1, size, grid),
               RecursivePath(i, j + 1, size, grid)) + int(grid[i][j])


def RecursivePathMemory(i, j, size, grid):

    global visited
    global path
    global best

    coord = f"{i} {j}"

    if (i < 0 or j > size - 1):
        return -inf

    if coord in visited:
        return visited.get(coord)

    if (grid[i][j] == "x"):
        return -inf

    if (i == 0 and j == size - 1):
        return int(grid[i][j])

    up = RecursivePathMemory(i - 1, j, size, grid)
    diagonal = RecursivePathMemory(i - 1, j + 1, size, grid)
    right = RecursivePathMemory(i, j + 1, size, grid)

    best = max(up, diagonal, right)

    visited.update({coord: best + int(grid[i][j])})

    return visited.get(coord)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Por favor insira uma das alternativas (1 - recursao simples / 2 - recursao com memorizacao) precedida pelo nome do arquivo python.")
        sys.exit()
    else:
        op = sys.argv[1]

    if op.isdigit():
        for file in os.listdir('testes'):
            visited.clear()
            matrix, size = read_file(file)
            size = int(size.strip())
            match op:
                case "1":
                    res = RecursivePath(size - 1, 0, size, matrix)
                case "2":
                    res = RecursivePathMemory(size - 1, 0, size, matrix)
                case _:
                    print("serio? essa escolha nao e valida.")
                    break
            if (res == -inf):
                print(
                    "provavelmente esse arquivo tem algum erro que torna impossivel encontrar um caminho valido.")
            else:
                print(res)

    else:
        print("Apenas as opcoes informadas sao validas.")
