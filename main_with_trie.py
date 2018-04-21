import sys
MARK = '#'

########################################################
class TrieTree:
  def __init__(self):
    self.m_char_map = {}
    self.m_is_word = False
  
  def insert(self,word,index=0):
    cur_char = word[index]
	
    if index == len(word)-1:
      self.m_char_map[cur_char] = TrieTree()
      self.m_is_word = True
      return

    if cur_char not in self.m_char_map:
      t = TrieTree()
      t.insert(word,index+1)
      self.m_char_map[cur_char] = t
    else:
      t = self.m_char_map[cur_char]
      t.insert(word,index+1)
    
  def search(self,word,index=0):
    if index > len(word)-1:
      return False
    
    cur_char = word[index]

    if cur_char not in self.m_char_map:
      return False
	
    if self.m_is_word and index==len(word)-1:
      return True
      
    return self.m_char_map[cur_char].search(word,index+1)
########################################################

def traverse(board,tree,x,y,word):
  if x<0 or y<0 or x>=len(board) or y>=len(board[0]):
    return
  
  if board[x][y] == MARK: 
    return

  word += board[x][y]
  if tree.search(word):
    print(word)
  
  origin = board[x][y]
  board[x][y] = MARK
  traverse(board,tree,x+1,y,word)
  traverse(board,tree,x-1,y,word)
  traverse(board,tree,x,y+1,word)
  traverse(board,tree,x,y-1,word)
  board[x][y] = origin

puzzle_board = [['r','l','d','y'],
               ['o','a','r','a'],
               ['w','h','e','l'],
               ['o','g','o','l']]

puzzle_dict = {"hello","world","yara","roar","woa","are"}
trie_tree = TrieTree()
for w in puzzle_dict:
  trie_tree.insert(w)

if puzzle_board == None:
  print("Empty board!")
  sys.exit()

for row in range(len(puzzle_board)):
  for col in range(len(puzzle_board[0])):
    traverse(puzzle_board,trie_tree,row,col,'')

#print(puzzle_board)
