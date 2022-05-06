def miniMaxSum(arr):
    max_value = None
    mini_value = None
    for i in range(len(arr)):
      n_arr = list(arr)
      n_arr.pop(i)
      print(n_arr)
      value = sum(n_arr)
      print(value)
      n_arr = arr
      
      if max_value is None:
        max_value = value
        print(value)
        
      if mini_value is None:
        mini_value = value
        print(value)

      if max_value < value:
        max_value = value
        print(value)
        
      if mini_value > value:
        mini_value = value
        print(value)
      
    return mini_value, max_value
