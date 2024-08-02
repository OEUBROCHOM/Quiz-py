word = input("Enter a string word: ")
n = int(input("Enter the number n: "))
if word == "good" and 7 <= n <= 15:
    print("It's good")
elif word == "bad" and (n < 7 or n > 15):
    print("It's bad")
else:
    print("Again")

