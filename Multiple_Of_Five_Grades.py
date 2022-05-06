def check(n):
  if n == '0':
    return True
  elif n == '5':
    return True
  else:
    return False
  
def get_multiple(i):
  if (len(str(i))) == 1:
    if i < 5:
      i = 5
    elif i >= 5 and i < 10:
      i = 10
  else:
    i = i+1
    n = str(i)
    s2 = n[len(n)//2 if len(n)%2 == 0
                 else (((len(n)//2))+1):]
    while (check(s2) is not True):
      check(s2)
      i = i+1
      n = str(i)
      s2 = n[len(n)//2 if len(n)%2 == 0
                 else (((len(n)//2))+1):]
      if s2 == '0':
        return i
      elif s2 == '5':
        return i
      else:  
        pass
  return i

def __gradeCalculator(grades):
    # Write your code here
    for i in grades:
      index = grades.index(i)
      if i < 38:
        grades[index] = i
      else:
        
        mut = get_multiple(i)
        
        dif = mut - i
        
        lit = [0,1,2]
        for item in lit:
          if item == dif:
            grades[index] = mut
    return grades
