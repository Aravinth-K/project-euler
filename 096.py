"""
Su Doku (Japanese meaning number place) is the name given to a
popular puzzle concept. Its origin is unclear, but credit must
be attributed to Leonhard Euler who invented a similar, and
much more difficult, puzzle idea called Latin Squares. The
objective of Su Doku puzzles, however, is to replace the
blanks (or zeros) in a 9 by 9 grid in such that each row,
column, and 3 by 3 box contains each of the digits 1 to 9.

Below is an example of a typical starting puzzle grid and its
solution grid.

A well constructed Su Doku puzzle has a unique solution and
can be solved by logic, although it may be necessary to employ
"guess and test" methods in order to eliminate options (there
is much contested opinion over this). The complexity of the
search determines the difficulty of the puzzle; the example
above is considered easy because it can be solved by straight
forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/
Target As...'), contains fifty different Su Doku puzzles
ranging in difficulty, but all with unique solutions (the
first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit
numbers found in the top left corner of each solution grid;
for example, 483 is the 3-digit number found in the top left
corner of the solution grid above.
"""


def solve(mat):
    tcan = []  # list of candidates
    i = 0
    mincand = cand_i = cand_j = 10  # item with least > 1 candidates
    while (i < 9):
        j = 0
        while (j < 9):
            if mat[i][j] == 0:
                t = list(set(range(1, 10)) -
                         set([mat[x][y]
                              for x in range(i // 3 * 3, i // 3 * 3 + 3)
                              for y in range(j // 3 * 3, j // 3 * 3 + 3)] +
                             mat[i] + [mat[a][j] for a in range(9)]))
                if not t:  # can't find a candidate
                    return False
                if len(t) == 1:
                    if cand_i == i and cand_j == j:  # replacing current least
                        mincand = cand_i = cand_j = 10
                    mat[i][j] = t[0]
                    i = -1
                    continue
                if len(t) < mincand:  # saving shortest candidate list
                    tcan, mincand, cand_i, cand_j = t, len(t), i, j
            j += 1
        i += 1
    if mincand == 10:
        return mat
    else:
        for test in tcan:
            mtest = [r for r in mat]  # copy without reference
            mtest[cand_i][cand_j] = test
            mtry = solve(mtest)
            if mtry:
                return mtry
    return False


def main():
    a = open('p096_sudoku.txt', 'r').readlines()
    mt = []
    count = 0
    for x in a:
        if x[0] == 'G':
            mt = []
            print(x)
        else:
            mt.append(list(map(int, list(x)[0:9])))
            if len(mt) == 9:
                m = solve(mt)
                for r in m:
                    print(r)
                i = int(''.join(list(map(str, m[0][0:3]))))
                count += i
    print(count)


if __name__ == '__main__':
    main()
