import lexer
import parser_

def main():
  while True:
    inp = input("> ")
    
    if inp == "":
      continue
    
    l = lexer.Lexer(inp)
    tks = lexer.lex(l)
    
    if tks == None:
      continue
    
    p = parser_.Parser(tks)
    tree = p.parse()
    
    if tree == None:
      continue
    
    print(tree)

if __name__ == "__main__":
  main()