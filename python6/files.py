#!/usr/bin/env python3

#open file and read contents
with open ("Python_06.txt","r") as file_read, open ("Python_06.uc.txt","w") as file_write:
    for line in file_read:
        line = line.rstrip()
        line = line.upper()
        file_write.write(f"{line}\n")
print(f"wrote to file Python_06.uc.txt")