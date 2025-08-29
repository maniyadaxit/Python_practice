# Assignment 5

## Task 1: Create a Dictionary of Student Marks

```python


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

```

```output
Enter the key : daxit
Enter the value : maniya
========Final output======
{'animal': 'hours', 'daxit': 'maniya'}
animal   =    hours
daxit   =    maniya
===============Search Specific Data==============
Enter the key which value you find : daxit
daxit value is maniya
Are you intrested to put more data ?y/ny
Enter the key : pal
Enter the value : maniya
========Final output======
{'animal': 'hours', 'daxit': 'maniya', 'pal': 'maniya'}
animal   =    hours
daxit   =    maniya
pal   =    maniya
===============Search Specific Data==============
Enter the key which value you find : pal
pal value is maniya
Are you intrested to put more data ?y/n
```

## Task 2: Demonstrate List Slicing

```python
List1 = [1,2,3,4,5,6,7,8,9,10]

Extended_element = List1[0:5]
reverse_element = Extended_element[::-1]

print(Extended_element)
print(reverse_element)
```

```output

[1, 2, 3, 4, 5]
[5, 4, 3, 2, 1]
```
