# kalkulator.py



class Kalkulator:

  def Add(x, y)
    return x + y
    
  def Minus(x, y, r=false)
    if r: 
      return y - x
    else:
      return x - y


def main():
  
  kal = Klakulator()
  print("Podaj liczbę X:)
  x = int(input())
  print("podaj liczbę Y:)
  y = int(input())
  print("Wybierz działanie:")
  print("[1] X + Y")
  print("[2] X - Y")
  print("[3] Y - X")
  odp = input()
  if odp = "1":
    print(kal.Add(x,y)
  elif odp = "2":
    print(kal.Minux(x,y)
  elif odp = "3":
    print(kal.Minus(x,y,True)
  else:
    print("Nie wskazano poprawnie działania")
    
    
  
  
  
if __name__ == "__main__":
  main()
