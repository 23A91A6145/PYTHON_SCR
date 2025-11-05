from _ast import Delete

    # They are mainly CRUD operations
# 1. Create , 2. Read, 3. Update, 4. Delete.

#  Opening a file
f = open(r"C:\Users\chara\Downloads\resume_c.pdf", 'rb')
data = f.read() # reading a file
print(data)  # will print raw bytes

# closing a file
f.close()

# file properties
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

# writting a file
