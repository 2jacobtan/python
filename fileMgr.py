'''
Utility for managing files in current directory tree.
Uses regex (regular expressions).
* Currently set up to move subdirectory files to current working directory
'''
VERSION = '3'

import os, re
from glob import glob
from shutil import move

#regex for re.match()
REG_EXP = r"(?i).+\.(sub|idx)"

def files_match(regex, top):
  '''
  return list of regex-matched file names in os.walk(top)
  print each item checked; '>' prefix, for each successful match
  '''
  matches=[] #list of stuff to be managed
  for root, dirs, files in os.walk(top): #walk each immediate subdirectory
    for x in files: #iterate filenames
      dir_file = os.path.join(root,x)
      m = re.match(regex, x)      
      if m:
        matches.append(dir_file)
        print('>',end='') #print a '>' prefix for each matched item
      print(' ', dir_file) #print the item checked
  return matches

def main():
  print( 'Welcome to fileMgr - v{!s}\n'.format(VERSION) )

#0 print directory to work in
  print("_0__Directory to work in__")
  print(os.path.abspath('.')) #or use os.getcwd()
  print()

#1 generate, via regex, list of stuff to be managed
  #also print each relevant item checked
  print("_1__Checked items (no changes made yet)__")
  m_stuff=[] #list of stuff to be managed
  for top in [x.rstrip(r'\/') for x in glob('*/')]: #iterate immediate subdirectories
    m_stuff.extend( files_match(REG_EXP, top) )
  print()
  
#2 show stuff to be managed
  print( '_2__Matched items (to be managed); regex = r"{}"__'.format(REG_EXP) )
  for x in m_stuff:
    print(' ', x)
  print( "Total, {!s} items.".format(len(m_stuff)) )
  print()
  
#3 to manage
  #explain action to be taken
  print( "To move above {!s} files to this directory:".format(len(m_stuff)) )
  print(' ', os.path.abspath('.'))
  
  while True: #sentinel loop
    #ask user for permission
    response = input("Proceed? (y/n): ")
    #yes
    if (response == 'y'):
      # manage contents listed in m_stuff (list)
      for x in m_stuff:
        move( x, '.')
      # print all contents after renaming
      print("_3__Contents, after__")
      for x in os.listdir('.'):
        print(' ', x)
      break #done
    #no
    elif response == 'n':
      break #done
  print()

#4 goodbye
  print("_4__End of program__")
  print("Goodbye.")

#boilerplate
if __name__ == "__main__":
  main()
