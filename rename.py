'''
Utility for renaming files in current directory.
Uses regex (regular expressions).
'''

import os, re

def main():
  print()
  
  # store current directory
  c_dir = os.getcwd()

  # print current directory
  print("_0__Current directory__")
  print(c_dir)
  print()

  names_old_new = {} #dict for old_name:new_name
  
  # generate, via regex, list of stuff to be renamed
  #   old and new names are stored in names_old_new (dict)
  # also print current directory's contents
  print("_1__Contents, before__")
  '''regex for matching'''
  REG_EXP = "zzz([0-9] .+)"
  r_stuff=[] #list of stuff to be renamed
  for x in os.listdir(c_dir):
    print(' ', x) #print each item under the current directory
    m = re.match(REG_EXP, x)
    if m:
      r_stuff.append( x)
      '''generate a new name using the match object m'''
      names_old_new[x] = "zz%s" % m.group(1)
  print()
  
  # show stuff to be renamed
  print("_2__To be renamed, regex = ",repr(REG_EXP),"__", sep='')
  for x in r_stuff:
    print(' ', x, "_to_", names_old_new[x])
  print()
  
  # renaming
  while True: #sentinel loop
    #ask user for permission
    r = input("Proceed? (y/n): ")
    #yes
    if (r == 'y'):
      # rename contents listed in r_stuff (list)
      for x in r_stuff:
        os.rename( x, names_old_new[x] )
      # print all contents after renaming
      print("_3__Contents, after__")
      for x in os.listdir(c_dir):
        print(' ', x)
      break #done
    #no
    elif r == 'n':
      break #done


  print("\nGoodbye.")

if __name__ == "__main__":
  main()
