# Assignment 4

## Task 1: Read a File and Handle Errors

```python
try:
  with open('Sample.txt' , mode="r") as my_file:
    Line = 1
    for x in my_file.readlines():
      print(f"Line : {Line} : {x}")
      Line+=1
except FileNotFoundError:
  print("Error : the file 'Sample.txt' was not found")

```

\*\*
Error : the file 'Sample.txt' was not found
\*\*

## Task 2: Write and Append Data to a File

```python
name = input("Enter the name of file : ")


with open(f"{name}.txt" , mode="a+") as my_file:
  content = input("Enter text to write to the file : ")
  my_file.write(content)
  print(f"Data sussess fully enter the file : {name}.txt")
  additional_text = input("Enter additional text to append : ")
  my_file.write(f"\n {additional_text}")
  print("Data succesfully appended.")

  print(f"Final content of {name}.txt")
  my_file.seek(0)
  for x in my_file.readlines():
    print(f"{x}")
```

\*\*
Output:
Enter the name of file : Output
Enter text to write to the file : Hello! Python
Data sussess fully enter the file : Output.txt
Enter additional text to append : This is my appended content
Data succesfully appended.
Final content of Output.txt
Hello! Python

This is my appended content
\*\*
