letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>",input("Enter your name: ")).replace("<|Date|>",input("Enter date: ")))