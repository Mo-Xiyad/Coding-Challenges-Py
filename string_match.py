###. TASK. ###

'''
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


===Test Example===
string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
'''

def string_match(a, b):
  shorter = min(len(a), len(b))
  count = 0
  
  for i in range(shorter-1):
    substring_a = a[i:i+2]
    substring_b = b[i:i+2]
    if substring_a == substring_b:
      count += 1
  return count
