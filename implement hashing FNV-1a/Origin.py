class Hash:

  def Hash32(self, strInput):
    # Set the offset basis and FNV prime values for 32-bit hash
    OffsetBasis = 2166136261
    FNVPrime = 16777619

    # Convert the input string to a byte array using ASCII encoding
    data = strInput.encode('ascii')

    # Initialize the hash value to the offset basis
    hash = OffsetBasis

    # Apply the FNV algorithm to each byte in the data array
    for i in range(len(data)):
      hash = hash ^ data[i]
      hash = hash * FNVPrime

    # Print the input string and its 32-bit hash value in decimal and hexadecimal
    print(strInput + ", " + str(hash) + ", " + hex(hash))

    # Return the 32-bit hash value
    return hash

  def Hash64(self, strInput):
    # Set the offset basis and FNV prime values for 64-bit hash
    OffsetBasis = 14695981039346656037
    FNVPrime = 1099511628211

    # Convert the input string to a byte array using ASCII encoding
    data = strInput.encode('ascii')

    # Initialize the hash value to the offset basis
    hash = OffsetBasis

    # Apply the FNV algorithm to each byte in the data array
    for i in range(len(data)):
      hash = hash ^ data[i]
      hash = hash * FNVPrime

    # Print the input string and its 64-bit hash value in decimal and hexadecimal
    print(strInput + ", " + str(hash) + ", " + hex(hash))

    # Return the 64-bit hash value
    return hash

hash = Hash()
hash.Hash32("This is Original Text")
hash.Hash64("This is Original Text")
