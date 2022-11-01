def is_vowel(char: str) -> bool:
  vowels: "set[str]" = set(['a', 'e', 'i', 'o', 'u'])
  return char in vowels
