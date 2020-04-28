def order(sentence):
  positions = {}
  string = []
  for word in sentence.split():
      for char in word:
          if char.isdigit():
              positions[char] = word
  for i in range(len(positions)):
      i += 1
      string.append(positions[str(i)])
  finalstring = ' '.join(string)
  return finalstring
