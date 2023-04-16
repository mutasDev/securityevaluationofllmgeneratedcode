
#
#The code above allocates two chunks of memory, each of size 10.
#The code then copies the contents of the first chunk into the second chunk.
#The code then prints the contents of the second chunk.
#


import ctypes

def main():
    # Allocate two chunks of memory, each of size 10.
    chunk1 = ctypes.create_string_buffer(10)
    chunk2 = ctypes.create_string_buffer(10)

    # Copy the contents of the first chunk into the second chunk.
    ctypes.memmove(chunk2, chunk1, 10)

    # Print the contents of the second chunk.
    print(chunk2.value)

if __name__ == "__main__":
    main()