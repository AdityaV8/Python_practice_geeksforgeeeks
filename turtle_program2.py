import turtle

# Screen setup
screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Tic Tac Toe - Click to Play!")
screen.bgcolor("lightblue")
screen.tracer(0)

# Game board (0=empty, 1=X, 2=O)
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = 1  # 1=X, 2=O

# Drawing turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(8)

def draw_board():
    """Draw the 3x3 grid"""
    pen.clear()
    pen.color("darkgreen")
    
    # Horizontal lines
    pen.penup()
    pen.goto(-200, 0)
    pen.pendown()
    pen.setheading(0)
    pen.forward(400)
    
    pen.penup()
    pen.goto(-200, 0)
    pen.setheading(90)
    pen.forward(133)
    pen.setheading(0)
    pen.forward(400)
    
    # Vertical lines
    pen.penup()
    pen.goto(0, 200)
    pen.setheading(-90)
    pen.forward(400)
    
    pen.penup()
    pen.goto(0, 200)
    pen.setheading(0)
    pen.forward(133)
    pen.setheading(-90)
    pen.forward(400)

def draw_x(row, col):
    """Draw X at position (row, col)"""
    x = -133 + col * 133
    y = 133 - row * 133
    pen.color("blue")
    pen.penup()
    pen.goto(x-60, y-60)
    pen.pendown()
    pen.setheading(45)
    pen.forward(120)
    pen.penup()
    pen.goto(x-60, y+60)
    pen.pendown()
    pen.setheading(-45)
    pen.forward(120)

def draw_o(row, col):
    """Draw O at position (row, col)"""
    x = -133 + col * 133
    y = 133 - row * 133
    pen.color("red")
    pen.penup()
    pen.goto(x, y-60)
    pen.pendown()
    pen.setheading(0)
    pen.circle(60)

def check_winner():
    """Check rows, columns, and diagonals for winner"""
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != 0:
            return row[0]
    
    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]
    
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    
    # Check for tie
    if all(all(cell != 0 for cell in row) for row in board):
        return 3  # Tie
    
    return 0  # No winner yet

def show_winner(winner):
    """Display winner message"""
    msg = ""
    color = "black"
    if winner == 1:
        msg = "X WINS! 🎉 Click to play again!"
        color = "blue"
    elif winner == 2:
        msg = "O WINS! 🎉 Click to play again!"
        color = "red"
    elif winner == 3:
        msg = "TIE GAME! Click to play again!"
    
    pen.penup()
    pen.goto(0, -250)
    pen.color(color)
    pen.write(msg, align="center", font=("Arial", 24, "bold"))
    
    # Reset game
    global board, current_player
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current_player = 1

def onclick(x, y):
    """Handle mouse clicks on the board"""
    global current_player
    
    # Convert screen coordinates to board position
    col = int((x + 200) // 133)
    row = 2 - int((y + 200) // 133)
    
    # Check if valid position
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == 0:
        # Place mark
        board[row][col] = current_player
        
        # Draw mark
        if current_player == 1:
            draw_x(row, col)
        else:
            draw_o(row, col)
        
        # Check for winner
        winner = check_winner()
        if winner != 0:
            screen.ontimer(lambda: show_winner(winner), 500)
            return
        
        # Switch player
        current_player = 3 - current_player
        
        screen.update()

# Initial setup
draw_board()
screen.update()

# Bind mouse click event
screen.onclick(onclick)

# Keep window open
screen.mainloop()
