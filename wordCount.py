test_string = "my mom is very funny and epic when she makes me choccy milk"
#original string

def wordCount(test_string):
  print ("The original string is : " + test_string)
  # using split() function
  res = len(test_string.split())
  # total no of words
  print ("The number of words in string are : " + str(res))
  return str(res)

wordCount(test_string)
#code from: https://www.tutorialspoint.com/count-words-in-a-sentence-in-python-program