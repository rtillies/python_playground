
def palindrome(string):
  stripped_string = string.replace(" ","")
  # import ipdb; ipdb.set_trace()
  l = 0
  r = len(stripped_string) - 1
  while (l < r):
    if stripped_string[l].lower() == stripped_string[r].lower():
      l += 1
      r -= 1
    else:
  	  return False
  return True


print(palindrome('nurses run'))
print(palindrome('abba'))
print(palindrome('Racecar'))
print(palindrome('d'))
