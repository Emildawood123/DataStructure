# it is faild unfort.....
from sys import *
import ctypes


class OurArray:
  def Resize(self, source: ctypes.POINTER(ctypes.c_int), newSize: int):
    if newSize <= 0 or source is None or len(source.contents) == newSize:
      return

    # Allocate a new array of size newSize
    newArray = (ctypes.c_int * newSize)()

    # Copy the contents of the old array into the new array
    ctypes.memmove(newArray, source,
                   ctypes.sizeof(ctypes.c_int) * len(source.contents))

    # Update the reference to the source array with the new array
    print(len(newArray))
    source.contents = newArray


  def GetAt(self, source: ctypes.POINTER(ctypes.c_int), index: int):
    if index < 0 or source is None or index >= len(source.contents):
      return None

    # Compute the memory location of the element at the specified index
    elementPtr = ctypes.cast(source, ctypes.POINTER(ctypes.c_int))
    elementPtr = elementPtr[index]

    # Return the value at the memory location
    return elementPtr


if __name__ == '__main__':
  # Create an integer array of length 3 and print it
  arr = (ctypes.c_int * 3)(4654, 921, 762)

  # Create an instance of the OurArray class and call the Resize method to increase the size of the array to 5
  ourArray = OurArray()
  ourArray.Resize(ctypes.pointer(arr), 5)

  # Print the new array
  print(list(arr))

  # Call the GetAt method to get the element at index 1 and print it
  item = ourArray.GetAt(ctypes.pointer(arr), 1)
  print(item)

  # Print the element at index 1 to verify that it matches the value returned by the GetAt method
  print(len(arr))
