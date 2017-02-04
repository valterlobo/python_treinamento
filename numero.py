#numero.py

try:
   print(1 / 0)   
except Exception as e:
  print("Something bad happened -> " + str(e) )
  #raise RuntimeError("Something bad happened")   
   
