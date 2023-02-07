def print_error(pos: int, msg: str):
  print(" " * 2, end="")
  print(" " * (pos - 1), end="")
  
  print("^")
  
  print(msg)