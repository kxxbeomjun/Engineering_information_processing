#공정처 과제
#10/1 final try draft

#displayBoard 함수 정의
def displayBoard(board):  
  # 3X3 행렬로 print하기 

  empty_str = ''
  for a in range(0, 9):
    symbol = board[a]
    if symbol == empty_str:
      symbol = '-'

    #use format function to print board 조금 더 간단하게 
    print(symbol,' ', end = '')
    if a == 2 :
      print()
    elif a == 5 :
      print()
  print()

#getMove 함수 정의
def getMove(board, locations, player): 
  empty_str = ''
  approval_move = False
  while not approval_move:
    move = input(player+ ', ' + 'enter your move: ')

    #case1 : player puts wrong number 예외처리1
    if move not in locations:
      print('You must enter 1 to 9. Please enter again')
    #case2 : player puts used number 예외처리2
    elif board[int(move) - 1] != empty_str:
      print('That location of the board already used')
    else:
      approval_move = True
      return move
  
#Win 함수 정의
def win(board, symbol):
  empty_str = ''
  winning = False

  #if 문 이용, win 함수에 어떤 player이 이기는지 표시해야함
  #X와 O이 이기는 경우 나누기
  if symbol == 'X': # X가 이기는 경우 
    sum = 15
  elif symbol == 'O' : # O이 이기는 경우
    sum = 3

  #board판에서 표시된 pattern에 따라 숫자로 인식해서 sum값 더하기 
  pattern = [5 if a =='X' else 1 if a =='O' else 0 for a in board]

  #if 문 이용해서 경우의 수 나누기
  #가로3가지 세로3가지 대각선 2가지 총 8가지에 대한 이기는 경우의 수 모두 적기
  if pattern[0] + pattern[1] + pattern[2] == sum:
      winning = True
  elif pattern[3] + pattern[4] + pattern[5] == sum:
      winning = True
  elif pattern[6] + pattern[7] + pattern[8] == sum:
      winning = True
  elif pattern[0] + pattern[3] + pattern[6] == sum:
      winning = True
  elif pattern[1] + pattern[4] + pattern[7] == sum:
      winning = True
  elif pattern[2] + pattern[5] + pattern[8] == sum:
      winning = True
  elif pattern[0] + pattern[4] + pattern[8] == sum:
      winning = True
  elif pattern[2] + pattern[4] + pattern[6] == sum:
      winning = True 
    
  return winning

#tie함수 정의
def tieGame(board):
  empty_str = ''
  tie_game = True 
  #for문 이용하기 
  for position in board:
    if position == empty_str:
      tie_game = False

  return tie_game

# --- main
# init
empty_str = ''
board = [empty_str for k in range(1, 10)]
locations = [str(x) for x in range(1,10)]

# program greeting
print('This program will allow two players to play the game of tic-tac-toe.')
print("Player 1 has 'X', and player 2 has 'O'.")

# get players
name_player1 = input('Enter the name of player 1: ')
name_player2 = input('Enter the name of player 2: ')

# display board locations
print('Enter your mark using the board positions shown below.\n')
displayBoard(locations) #index 2d -list

# start game
player = name_player1
player_symbol = 'X'

print(name_player1, "you start. You are playing 'X'")
displayBoard(board)   #play board 2d -list
game_over = False
while not game_over:
  move = getMove(board,locations, player)
  board[int(move) - 1] = player_symbol
  displayBoard(board)
  if win(board, player_symbol):
    print(player + ', ' + 'you win!')
    game_over = True
  elif tieGame(board):
    print('Tie Game!')
    game_over = True
  else:
    if player == name_player1:
      player = name_player2
      player_symbol = 'O'
    else:
      player = name_player1
      player_symbol = 'X'

