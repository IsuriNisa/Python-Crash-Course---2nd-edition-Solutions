guests = ['John', 'Lily', 'Anne', 'Mike']

guests.remove('Mike')
guests.append('Jack')
guests.insert(0,'Merry')
guests.insert(2,'Tom')
guests.append('Harry')

print("Sorry!!! I can invite only two people")

print(f"sorry!!! {guests.pop()} there is no space in the table")
print(f"sorry!!! {guests.pop()} there is no space in the table")
print(f"sorry!!! {guests.pop()} there is no space in the table")
print(f"sorry!!! {guests.pop()} there is no space in the table")
print(f"sorry!!! {guests.pop()} there is no space in the table\n")

print(guests)

print(f"\nHello {guests[0]} you still in the list")
print(f"Hello {guests[1]} you still in the list\n")

del guests[0]
del guests[0]

print(guests)