#include <iostream>
using namespace std;

class Solution
{
public:
    void solve(int** board, int row, int n, int cols[], int ndiagonal[], int rdiagonal[])
    {
        if (row == n)
        {
            for(int i=0; i<n; i++){
                for(int j=0; j<n; j++){
                    cout<<board[i][j]<<" ";
                }
                cout<<endl;
            }
            cout<<endl<<endl;
            return;
        }

        for (int col = 0; col < n; col++)
        {
            if (cols[col] == 0 && ndiagonal[row + col] == 0 && rdiagonal[row - col + n - 1] == 0)
            {
                board[row][col] = 1;
                cols[col] = 1;
                ndiagonal[row + col] = 1;
                rdiagonal[row - col + n - 1] = 1;

                solve(board, row + 1, n, cols, ndiagonal, rdiagonal);

                board[row][col] = 0;
                cols[col] = 0;
                ndiagonal[row + col] = 0;
                rdiagonal[row - col + n - 1] = 0;
            }
        }
    }
};


int main()
{
    Solution s;

    int n;
    cout << "Enter size of Board (Min-4/Max-8): ";
    cin >> n;

    int** board = new int*[n];
    int cols[n];

    for (int i = 0; i < n; i++)
    {
        cols[i] = 0;
        board[i] = new int[n];
        for (int j = 0; j < n; j++)
        {
            board[i][j] = 0;
        }
    }
    int ndiagonal[2 * n - 1];
    int rdiagonal[2 * n - 1];
    for (int i = 0; i < 2 * n - 1; i++)
    {
        ndiagonal[i] = 0;
        rdiagonal[i] = 0;
    }

    s.solve(board, 0, n, cols, ndiagonal, rdiagonal);

    return 0;
}