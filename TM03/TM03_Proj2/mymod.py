def ispalindrome(name):
    s=name[::-1]
    if (s == name): 
        print("Yes it is a palindrome.")
    print("No it is not a palindrome.")

def count_the_vowels(name):
    vowels="AEIOUaeiou"
    final = [each for each in name if each in vowels] 
    print("No. of Vowels: ",len(final)) 
def frequency_of_letters(name):
    print("Frequency of letters:",','.join(('{}-{}'.format(letter,name.lower().count(letter))
        for letter in set(name.lower())
        if letter in "abcdefghijklmnopqrstuvwxyz")))
