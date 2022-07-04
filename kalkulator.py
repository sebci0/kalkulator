# kalkulator.py



class Kalkulator:

  def Add(self, x, y):
    return x + y
    
  def Minus(self, x, y, r=False):
    if r: 
      return y - x
    else:
      return x - y


def main():
  
  kal = Kalkulator()
  print("Podaj liczbę X:", end='')
  x = int(input())
  print("podaj liczbę Y:", end='')
  y = int(input())
  print("Wybierz działanie:")
  print("[1] X + Y")
  print("[2] X - Y")
  print("[3] Y - X")
  print(":", end='')
  odp = input()
  if odp == "1":
    print("Wynik:", kal.Add(x,y))
  elif odp == "2":
    print("Wynik:", kal.Minus(x,y))
  elif odp == "3":
    print("Wynik:", kal.Minus(x,y,True))
  else:
    print("Nie wskazano poprawnie działania")
    
    
  
  
  
if __name__ == "__main__":
  main()
