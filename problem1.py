def remove_duplicates(x):
  '''
  ### add to this
  returns a new list without duplicate values

  >>> remove_duplicates([63,67,27,25,63,8])
  [63,67,27,25,8]
  >>> remove_duplicates([1,1,1,1])
  [1]
  >>> remove_duplicates([1,2,3])
  [1,2,3]
  '''
  new_list = []
  for item in x:
    if item not in new_list:
      new_list.append(item)
  return new_list
