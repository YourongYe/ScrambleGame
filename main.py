import sys
MARK = '#'

def traverse(board,dict,x,y,word):
  if x<0 or y<0 or x>=len(board) or y>=len(board[0]):
    return
  
  if board[x][y] == MARK: 
    return

  word += board[x][y]
  if word in dict:
    print(word)
  
  origin = board[x][y]
  board[x][y] = MARK
  traverse(board,dict,x+1,y,word)
  traverse(board,dict,x-1,y,word)
  traverse(board,dict,x,y+1,word)
  traverse(board,dict,x,y-1,word)
  board[x][y] = origin

puzzle_board = [['r','l','d','y'],
               ['o','a','r','a'],
               ['w','h','e','l'],
               ['o','g','o','l']]

dict = {"hello","world","yara","roar","woa","are"}     

if puzzle_board == None:
  print("Empty board!")
  sys.exit()

for x in range(len(puzzle_board)):
  for y in range(len(puzzle_board[0])):
    traverse(puzzle_board,dict,x,y,'')

#print(puzzle_board)
