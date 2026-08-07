text_1 = "bat"
text_2 = "cat"

text_3 = "bet"
text_4 = "bathe"

text_5 = "bat"
text_6 = "Bat"

print(f"{text_1} == {text_5}: {text_1==text_5}")   # True
print(f"{text_1} < {text_2}: {text_1 < text_2}")   # True
print(f"{text_1} < {text_3}: {text_1 < text_3}")   # True
print(f"{text_1} < {text_6}: {text_1 < text_6}")   # False
print(f"{text_3} < {text_4}: {text_3 < text_4}")   # False