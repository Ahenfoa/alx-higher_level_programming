#!/usr/bin/python3
print(''.join([chr(122-i//2) if i%2 == 0 else chr(90-i//2) for i in range(50, -2, -2)]))
