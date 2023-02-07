import lexer
import parser_
import interpreter

def main():
  while True:
    try:
      inp = input("> ")
      
      if inp == "":
        continue
      
      l = lexer.Lexer(inp)
      tks = lexer.lex(l)
      
      if not tks:
        continue
      
      p = parser_.Parser(tks)
      tree = p.parse()
      
      if tree == None:
        continue
      
      i = interpreter.Interpreter()
      value = i.visit(tree)
      
      if value != None:
        print(f"< {value}")
    except Exception as e:
      print(e)

if __name__ == "__main__":
  main()