#include <stdio.h>
#include <stdlib.h>

#define ROWS 12
#define COLS 12
#define WIN 5


// Function to initialize the board
void init_board(char board[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            board[i][j] = ' ';
        }
    }
}

// Function to check if the board is full
void isArrayFull(char board[ROWS][COLS]) {
    int usedTiles = 0;
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (board[i][j] != ' ') {
                usedTiles += 1;
            }
        }
    }
    if (usedTiles == ROWS * COLS) {
        printf("The board is full and without a winner, it's a draw!\n");
        exit(0);
    }
}

// Function to print the top legend
void topLegend() {
    printf("    ");
    for (int i = 0; i < COLS; i++)
    {
        printf("(%.2d)", i);
    }
    printf("\n");
}

// Function to print the board
void print_board(char board[ROWS][COLS]) {
    topLegend();
    for (int i = 0; i < ROWS; i++) {
        printf("(%.2d)", i);
        printf("| ");
        for (int j = 0; j < COLS; j++) {
            printf(" %c| ", board[i][j]);
        }
        printf("\n");
        printf("    -");
        for (int h = 0; h < COLS; h++) {
            printf("----");
        }
        printf("\n");
    }
}

// Function to make a move
void make_move(char board[ROWS][COLS], int row, int col, int player) {
    if (board[row][col] == ' ') {
        board[row][col] = player == 1 ? 'X' : 'O';
    }
}

// Function to check for winning combinations
void checkWinningCombinations(char board[ROWS][COLS], int row, int col) {
    int countO = 0;
    int countX = 0;
    int i, j;
    // Check for winning combinations in rows
    for (i = 0; i < ROWS; i++) {
        if (board[i][col] == 'O') {
            countO += 1;
            countX = 0;
        } else if (board[i][col] == 'X') {
            countX += 1;
            countO = 0;
        } else {
            countO = 0;
            countX = 0;
        }
        if (countO == WIN) {
            printf("Player O wins!\n");
            exit(0);
        } else if (countX == WIN) {
            printf("Player X wins!\n");
            exit(0);
        }

    }
    countO = 0;
    countX = 0;
    // Check for winning combinations in columns
    for (j = 0; j < COLS; j++) {
        if (board[row][j] == 'O') {
            countO += 1;
            countX = 0;
        } else if (board[row][j] == 'X') {
            countX += 1;
            countO = 0;
        } else {
            countO = 0;
            countX = 0;
        }
        if (countO == WIN) {
            printf("Player O wins!\n");
            exit(0);
        } else if (countX == WIN) {
            printf("Player X wins!\n");
            exit(0);
        }
    }
    countO = 0;
    countX = 0;
    // Check for winning combinations in diagonals
    for (i = 0; i < ROWS; i++) {
        for (j = 0; j < COLS; j++) {
            if (i == j) {
                if (board[i][j] == 'O') {
                    countO += 1;
                    countX = 0;
                } else if (board[i][j] == 'X') {
                    countX += 1;
                    countO = 0;
                } else {
                    countO = 0;
                    countX = 0;
                }
                if (countO == WIN) {
                    printf("Player O wins!\n");
                    exit(0);
                } else if (countX == WIN) {
                    printf("Player X wins!\n");
                    exit(0);
                }
            }
        }
    }
    // Check for winning combinations in inverted diagonals
    countO = 0;
    countX = 0;
    for (i = 0; i < ROWS; i++) {
        for (j = 0; j < COLS; j++) {
            if (j == i + 1) {
                if (board[i][j] == 'O') {
                    countO += 1;
                    countX = 0;
                } else if (board[i][j] == 'X') {
                    countX += 1;
                    countO = 0;
                } else {
                    countO = 0;
                    countX = 0;
                }
                if (countO == WIN) {
                    printf("Player O wins!\n");
                    exit(0);
                } else if (countX == WIN) {
                    printf("Player X wins!\n");
                    exit(0);
                }
            }
        }
    }
}

int main() {
    int currentPlayer = 0;
    int row, col;
    char board[ROWS][COLS];
    init_board(board);
    print_board(board);
    while (1) {
        printf("Player %d(%c), enter row and column: ", currentPlayer + 1, currentPlayer == 1 ? 'X' : 'O');
        scanf("%d %d", &row, &col);
        if (row < 0 || row >= ROWS || col < 0 || col >= COLS)
        {
            printf("Invalid move outside of play field, try again.\n");
            continue;
        } else if (board[row][col] != ' ') {
            printf("Invalid move, tile is already taken, try again.\n");
            continue;
        }  
        
        make_move(board, row, col, currentPlayer);
        print_board(board);
        checkWinningCombinations(board, row, col);
        isArrayFull(board);
        currentPlayer = 1 - currentPlayer;
    }
    return 0;
}