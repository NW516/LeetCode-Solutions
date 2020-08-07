filename = "onecharinput.txt"

#with open(filename) as f:
#  while True:
#    c = f.read(1)
#    if not c:
#      print("End of file")
#      break
#    print("Read a character: ", c)


with open("onecharinput.txt") as fileobj:
    for line in fileobj:  
       for ch in line: 
           print("Read a character: ", ch)
