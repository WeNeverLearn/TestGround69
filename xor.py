import string

# The cipher text
cipherText = ''

# Possible characters
allChars = "d=,8hal:W;SvU{3bF0VH\\[.nQ?Y^>/L6R#yM<\"IqPp_E4iA%sN7x'em|f2 c~z}JruGjkOK`&$]9TZwDXCt@5g()-!1*B+o"

# Length of all possible characters
l = len(allChars)

# User input
string = input("Clear/Cipher Text: ")
key = input("Key: ")

# if the length is not same, exit
if len(string) != len(key):
    print("Both Clear Text and key should be of same length.")
    exit(-1)


charKey = zip(list(string), list(key))

# Encrypt
for c, k in charKey:
    cipherChar = allChars[(allChars.index(c) ^ allChars.index(k)) % l]
    cipherText+=cipherChar

print(cipherText)
