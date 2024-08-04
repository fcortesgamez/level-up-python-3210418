def sort_words(sentence):
  words = sentence.split()
  words = [w.lower() + w for w in words]
  words.sort()
  words = [w[len(w)//2:] for w in words]
  return words

