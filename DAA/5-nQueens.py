class Solution:
    def solve(self, n):
        board = [[0 for _ in range(n)] for _ in range(n)]
        cols = [0] * n
        ndiagonal = [0] * (2 * n - 1)
        rdiagonal = [0] * (2 * n - 1)
        results = []

        def is_safe(row, col):
            return cols[col] == 0 and ndiagonal[row + col] == 0 and rdiagonal[row - col + n - 1] == 0

        def place_queen(row):
            if row == n:
                results.append([row[:] for row in board])
                return

            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 1
                    cols[col] = 1
                    ndiagonal[row + col] = 1
                    rdiagonal[row - col + n - 1] = 1

                    place_queen(row + 1)

                    board[row][col] = 0
                    cols[col] = 0
                    ndiagonal[row + col] = 0
                    rdiagonal[row - col + n - 1] = 0

        place_queen(0)
        return results

if __name__ == "__main__":
    s = Solution()
    n = int(input("Enter size of Board (Min-4/Max-8): "))

    if 4 <= n <= 8:
        solutions = s.solve(n)
        for solution in solutions:
            for row in solution:
                print(' '.join(map(str, row)))
            print("\n")
    else:
        print("Please enter a valid size for the board (between 4 and 8).")