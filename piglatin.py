s = input("enter sentence: ")

vowels = ["a", "e", "i", "o", "u"]

words = s.split()
for i, word in enumerate(words):

  letters = list(word)
  first_vowel = 0

  for j, letter in enumerate(letters):
    if letter.lower() in vowels:
      first_vowel = j
      break

  if first_vowel == 0:
    word = word + "yay"

  else:
    word = word[first_vowel:len(word)] + word[0:first_vowel] + "ay"
 
  words[i] = word.lower()

s = " ".join(words)
print(s)