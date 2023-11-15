class Dictionary:
  # Define the class constructor
  def __init__(self, initial_size=3):
    # Set the initial size of the dictionary
    self.initial_size = initial_size
    # Create an array to store key-value pairs
    self.entries = [None] * self.initial_size
    # Initialize the number of entries to 0
    self.entries_count = 0

  # Check if the dictionary needs to be resized and resize it if necessary
  def resize_or_not(self):
    if self.entries_count < len(self.entries) - 1:
      return

    # Calculate the new size of the dictionary
    new_size = len(self.entries) + self.initial_size

    print(f"[resize] from {len(self.entries)} to {new_size}")

    # Create a new array with the updated size
    new_array = [None] * new_size
    # Copy existing entries to the new array
    for i in range(len(self.entries)):
      new_array[i] = self.entries[i]

    # Update the reference to the new array
    self.entries = new_array

  # Return the number of entries in the dictionary
  def size(self):
    return self.entries_count

  # Set the value of a given key
  def set(self, key, value):
    for i in range(len(self.entries)):
      # Update the value of an existing key-value pair
      if self.entries[i] is not None and self.entries[i].key == key:
        self.entries[i].value = value
        return
    # Resize the dictionary if necessary
    self.resize_or_not()
    # Create a new key-value pair
    new_pair = KeyValuePair(key, value)
    self.entries[self.entries_count] = new_pair
    self.entries_count += 1

  # Get the value of a given key
  def get(self, key):
    for i in range(len(self.entries)):
      if self.entries[i] is not None and self.entries[i].key == key:
        return self.entries[i].value
    return None

  # Remove a key-value pair from the dictionary
  def remove(self, key):
    for i in range(len(self.entries)):
      if self.entries[i] is not None and self.entries[i].key == key:
        # Move the last entry to the current position
        self.entries[i] = self.entries[self.entries_count - 1]
        # Remove the last entry
        self.entries[self.entries_count - 1] = None
        # Decrement the number of entries
        self.entries_count -= 1
        return True
    return False

  # Print the contents of the dictionary
  def print(self):
    print("----------")
    print(f"[size] {self.size()}")
    for i in range(len(self.entries)):
      if self.entries[i] is None:
        print(f"[{i}]")
      else:
        print(f"[{i}] {self.entries[i].key}:{self.entries[i].value}")
    print("==========")


# Define a nested KeyValuePair class to store key-value pairs
class KeyValuePair:

  def __init__(self, key, value):
    self.key = key
    self.value = value

if __name__ == "__main__":
    dic = Dictionary()
    dic.print()
    dic.set("Sinar", "sinar@gmail.com")
    dic.set("Elvis", "elvis@gmail.com")
    dic.print()

    dic.set("Tane", "tane@gmail.com")
    dic.set("Gerti", "gerti@gmail.com")
    dic.set("Arist", "arist@gmail.com")
    dic.print()

    print(dic.get("Tane"))
    print(dic.get("Sinar"))
    print(dic.get("Elviaaa"))

    dic.remove("Sinar")
    dic.remove("Elvis")
    dic.remove("Arist")
    dic.print()

    dic.set("Sinar", "sinar@gmail.com")
    dic.print()
