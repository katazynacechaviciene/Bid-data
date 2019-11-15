import sys 

def greet (name: str, shout_count: int=1):
     if len(sys.argv)!=2:
     print (f"Hello, {sys.argv[1]}
     {int(sys.argv[2]) * '!'}")
     else:
     print (f"Hello, {sys.argv[1]}!")
  greet(sys.argv[:3])

