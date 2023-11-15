def hash32(string: str):
    Offset = 2166136261
    Prime = 16777619
    binary = string.encode('ascii')
    hash = Offset
    for i in range(len(binary)):
        hash = hash ^ binary[i]
        hash = hash  * Prime
    print(hash)
if __name__ == "__main__":
    string = "This is Original Text"
    hash32(string)
