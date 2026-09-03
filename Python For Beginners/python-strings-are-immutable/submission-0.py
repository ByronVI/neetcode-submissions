def remove_fourth_character(word: str) -> str:
    before = word[:3]
    after = word[4:]
    new = before + after
    return new


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
