def encrypt(string:str,shift:int) -> str:
    new_str = []
    for index in range(len(string)):
        new_str.append(chr(ord(string[index]) + shift))
    new_str = ''.join(new_str)
    return new_str.replace('#', ' ')

def decrypt(string:str,shift:int) -> str:
    result = string
    result = result.replace(' ', '#')
    result = list(result)
    for index in range(len(result)):
        result[index] = chr(ord(result[index]) - shift)
    return ''.join(result)

text = input("Enter the text: ")
shift = int(input("Enter the shift: "))

print(encrypt(text,shift))
print(decrypt(encrypt(text,shift),shift))