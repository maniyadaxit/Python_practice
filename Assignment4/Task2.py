name = input("Enter the name of file : ")


with open(f"{name}.txt" , mode="a+") as my_file:
  content = input("Enter text to write to the file : ")
  my_file.write(content)
  print(f"Data sussess fully enter the file : {name}.txt")
  additional_text = input("Enter additional text to append : ")
  my_file.write(f"\n{additional_text}")
  print("Data succesfully appended.")

  print(f"Final content of {name}.txt")
  my_file.seek(0)
  for x in my_file.readlines():
    print(f"{x}")