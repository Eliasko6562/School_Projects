#include <stdio.h>

#define ROWS 3
#define COLS 3


void init_board(char board[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            board[i][j] = ' ';
        }
    }
}

void topLegend() {
    for (int i = 0; i < COLS; i++)
    {
        printf("   (%d)", i);
    }
    printf("\n");
}

void print_board(char board[ROWS][COLS]) {
    topLegend();
    for (int i = 0; i < ROWS; i++) {
        printf("(%d)", i);
        for (int j = 0; j < COLS; j++) {
            printf("|%c|", board[i][j]);
        }
        printf("\n");
        printf("   ---------\n");
    }
}

void make_move(char board[ROWS][COLS], int row, int col, int player) {
    if (board[row][col] == ' ') {
        board[row][col] = player == 1 ? 'X' : 'O';
    } 
}

int main() {
    int currentPlayer = 0;
    int row, col;
    char board[ROWS][COLS];
    init_board(board);
    print_board(board);
    while (1) {
        printf("Player %d, enter row and column: ", currentPlayer + 1);
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
        currentPlayer = 1 - currentPlayer;
    }




    return 0;
}