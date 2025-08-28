try:
  with open('Sample.txt' , mode="r") as my_file:
    Line = 1
    for x in my_file.readlines():
      print(f"Line : {Line} : {x}")
      Line+=1
except FileNotFoundError:
  print("Error : the file 'Sample.txt' was not found")