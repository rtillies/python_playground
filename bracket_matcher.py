
def bracket_matcher(string):
  if len(string) % 2 != 0:
    return False 
  else:
    string1 = string.replace('{}', '')
    string2 = string1.replace('[]', '')
    string3 = string2.replace('()', '')
    if string3 == '':
      return True
    elif string3 == string1:
      return False 
    else:
      return bracket_matcher(string3)
  


print(bracket_matcher('{}'))
print(bracket_matcher('{[]({}[()])}'))
print(bracket_matcher('{[]{(}[()])}'))
print(bracket_matcher("(([]){})"))
print(bracket_matcher("([[][]{({}({}))}])"))


