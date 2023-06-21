def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]
  
def capitals(word):
    uppers = []
    for i in range(len(word)):
        if word[i].isupper():
            uppers.append(i)
    return uppers
