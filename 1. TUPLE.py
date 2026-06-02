--- Def: A tuple is an ordered collection of items that cannot be changed after creation.

-- Creating a Tuple
  numbers = (10, 20, 30)
  print(numbers)

  --Output:
  (10, 20, 30)


  --- Accessing Items
  numbers  = (10, 20, 30)
  print(numbers[1])

  ---Output:
    20


--- Change Attempt
numbers  = (10, 20, 30)
numbers[0] = 99
print(numbers)

--- Output:
TypeError: 'tuple object does not support item assignment
note: Because tuple is immutable
  
