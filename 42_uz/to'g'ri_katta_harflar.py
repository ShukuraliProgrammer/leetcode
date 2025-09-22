
def detectCapitalUse(word: str) -> bool:
    return (word.istitle() or word.isupper() or word.islower())

word = "sdsdsd"
print(detectCapitalUse(word))