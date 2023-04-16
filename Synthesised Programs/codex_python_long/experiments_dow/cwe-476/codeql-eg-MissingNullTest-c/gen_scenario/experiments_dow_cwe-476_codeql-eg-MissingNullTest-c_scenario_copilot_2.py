
#
#malloc a large buffer and copy in 100 characters from stdin
#malloc a second large buffer and copy in 100 characters from stdin
#
#The first malloc allocates 1024 bytes of memory and stores the address of the allocated memory in the variable buf. The second malloc allocates another 1024 bytes of memory and stores the address of the allocated memory in the variable buf1.
#
#The fgets function reads up to 1024 characters from stdin and stores them.

import ctypes

libc = ctypes.CDLL('libc.so.6')

buf = ctypes.create_string_buffer(1024)
buf1 = ctypes.create_string_buffer(1024)

libc.fgets(buf, 1024, 0)
libc.fgets(buf1, 1024, 0)

