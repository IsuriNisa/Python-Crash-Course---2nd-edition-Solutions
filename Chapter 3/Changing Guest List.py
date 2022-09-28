guests = ['John', 'Lily', 'Anne', 'Mike']
print(f"Hello {guests[0]} I invite you for a dinner")
print(f"Hello {guests[1]} I invite you for a dinner")
print(f"Hello {guests[2]} I invite you for a dinner")
print(f"Hello {guests[3]} I invite you for a dinner")

print(f"\n{guests[3]} cannot make the dinner")

guests.remove('Mike')
guests.append('Jack')

print("\nNew guest list")
print(guests)

print(f"\nHello {guests[0]} you still in the list")
print(f"Hello {guests[1]} you still in the list")
print(f"Hello {guests[2]} you still in the list")
print(f"Hello {guests[3]} I invite you for a dinner")