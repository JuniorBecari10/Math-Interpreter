from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
  END = 0
  NUM = 1
  
  PLUS = 2
  MINUS = 3
  TIMES = 4
  DIVIDE = 5
  
  LPAREN = 6
  RPAREN = 7

@dataclass
class Token:
  type: TokenType
  value: any
  pos: int
  
  def __repr__(self):
    return f"Token(type: {self.type}, value: {self.value}, pos: {self.pos})"