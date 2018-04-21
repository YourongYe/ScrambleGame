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
    if index>len(word)-1:
      return False
    
    cur_char = word[index]

    if cur_char not in self.m_char_map:
      return False
	
    if self.m_is_word and index==len(word)-1:
      return True
      
    return self.m_char_map[cur_char].search(word,index+1)

  
new_tree = TrieTree()
new_tree.insert("hello")
new_tree.insert("world")
new_tree.insert("orld")
new_tree.insert("worldd")
print(new_tree.search("hello"))
print(new_tree.search("world"))
print(new_tree.search("worldd"))
print(new_tree.search("worlddd"))
print(new_tree.search("orld"))
