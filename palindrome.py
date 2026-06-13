a=input("Enter a word:")
reversed_word=""
for i in a:
    reversed_word = i + reversed_word
    
if a == reversed_word:
    print(f'{a} is a palindrome ')
else:
    print(f'{a} is not a palindrome ')

