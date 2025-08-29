

dic = {"animal":"hours"}

while True:
  dic_key = input("Enter the key : ").lower()
  dic_value = input("Enter the value : ").lower()

  dic[f"{dic_key}"] = f"{dic_value}"

 

  print("========Final output======")
  print(dic)
  for key in dic: 
    print(f"{key}   =    {dic[key]}")

  print("===============Search Specific Data==============")
  name = input("Enter the key which value you find : ").lower()
  if dic[name].isalpha():
    print(f"{name} value is {dic[name]}")
  else:
    print(f"Sorry you pass {name} is not into data")
  

  Answer = input("Are you intrested to put more data ?y/n").lower()
  if Answer=="y":
    pass
  else:
    break

