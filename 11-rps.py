def rps(p1, p2):
    data = [
        ['paper', 'paper', 'Draw!'],
        ['scissors', 'scissors', 'Draw!'],
        ['rock', 'rock', 'Draw!'],
        ['paper', 'scissors', 'Player 2 won!'],
        ['paper', 'rock', 'Player 1 won!'],
        ['scissors', 'paper', 'Player 1 won!'],
        ['scissors', 'rock', 'Player 2 won!'],
        ['rock', 'scissors', 'Player 1 won!'],
        ['rock', 'paper', 'Player 2 won!'],
    ]
    for i in range(len(data)):
        if data[i][0] == p1 and data[i][1] == p2:
            return data[i][2]
