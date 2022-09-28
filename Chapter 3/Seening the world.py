places = ['Kandy', 'Beijing', 'Manali', 'London', 'Tokiyo']
# print the original order
print("2. Places I like to visit : ",places)

# Use sorted() function
print("\n3. After suing sorted function : ", sorted(places))

# Show still in original list
print("\n4. Show still in original list : ", places)

# Using sorted function get th reverse order
print("\n5. Using sorted get reverse : ", sorted(places,reverse=True))

# Show the list still in original list
print("\n6. Show the list : ", places)

# Use reverse function
places.reverse()
print("\n7. Get the reverse order : ", places)

# Again use reverse
places.reverse()
print("\n8. Again use reverse : ", places)

# Use sort
places.sort()
print("\n9. Use sort function : ", places)

# Use sort function to change order
places.sort(reverse=True)
print("\n10. Use sort to change the order : ",places)

