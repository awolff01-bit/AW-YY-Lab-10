def rotate_by_n(x,n):
  '''
  list, int -> list

  takes in a list and a number, n, and returms a list with each value 
  shifted down n positions

  >>> rotate_by_n([1,2,3,4],3)
  [2,3,4,1]
  >>> rotate_by_n([1,2,3,4],1)
  [4,1,2,3]
  '''
  for i in range(n):
    last_item = x.pop()  #removes the last item
    x.insert(0, last_item) #puts it at the beginning
  return x
