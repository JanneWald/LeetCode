def isAnagram(self, s, t):
  letters = {}
  if len(s) != len(t):
      return False

  for letter in s:
      if letter in letters:
          letters[letter] += 1
      else:
          letters[letter] = 1

  # Check t
  for letter in t:
      if letter not in letters:
          return False
      else:
          if letters[letter] == 0:
              return False
          else:
              letters[letter] -= 1

  return True
