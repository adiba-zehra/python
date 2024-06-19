elements = list(map(int, input("Enter elements separated by spaces: ").split()))
specific_element = int(input("Enter the element to count: "))
print(f"The element {specific_element} occurs {elements.count(specific_element)} times.")
