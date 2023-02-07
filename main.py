import lexer

def main():
  while True:
    inp = input("> ")
    
    l = lexer.Lexer(inp)
    tks = lexer.lex(l)
    
    if tks == None:
      continue
    
    print(tks)

if __name__ == "__main__":
  main()