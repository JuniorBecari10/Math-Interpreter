from tokens import *
import util

WHITESPACE = " \n\t"
DIGITS = "0123456789"

class Lexer:
  def __init__(self, exp: str):
    self.exp = exp
    self.cursor = 0
  
  def next_char(self):
    self.cursor += 1
  
  def ch(self) -> str:
    return self.exp[self.cursor] if self.cursor < len(self.exp) else "\0"
  
  def next_token(self) -> Token:
    if self.ch() in WHITESPACE:
      self.next_char()
    
    if self.ch() in DIGITS or self.ch() == ".":
      pos = self.cursor
      
      while self.ch() in DIGITS or self.ch() == ".":
        self.next_char()
      
      vl = self.exp[pos:self.cursor]
      
      # check for 2 or more dots
      count = 0
      for c in vl:
        if c == ".":
          count += 1
      
      if count > 1:
        util.print_error(pos, "Number with more than 1 dot")
        return None
      
      return Token(TokenType.NUM, vl, pos)

def lex(l: Lexer):
  tks = []
  
  while l.ch() != "\0":
    tk = l.next_token()
    
    if tk == None:
      return None
    
    tks.append(tk)
  
  return tks