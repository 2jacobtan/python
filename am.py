'''Abstract Maths'''

def show_divide(x,d):
  print( "%d = %d * %d" % (x,d,x/d) )
  

def gcd(a, b):
  '''Euclidean Algorithm'''
  #first two terms
  print(a)
  print(b, sep='\n', end='')
  
  #permanently store first two terms
  x = a
  y = b
  
  while (1):
    r=a % b
    q=a // b
    print(" (-%d)" % q)
    print(r, end='')
    if (r==0):
      print()
      show_divide(x,b)
      show_divide(y,b)
      print("Done.")
      return b
    a=b;b=r #for next iteration

def main():
  #test gcd()
  a = 7684
  b = 4148
  print( gcd(a,b) )
  
if __name__ == "__main__":
  main()