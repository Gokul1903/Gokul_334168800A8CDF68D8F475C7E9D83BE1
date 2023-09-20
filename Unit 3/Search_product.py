def linear_search_product(product,target):
    name=[]
    for i in range(len(product)):
        if target == product[i]:
            name.append(i)
        else:
            continue
    return name
        

product=['tv','fan','tv','fridge','tv']
target=input("Enter the target value : ")
target=target.lower()
fin=linear_search_product(product,target)
print("The indices of targeted value is",fin)
if fin:
    print(f"The targeted value {target} is in the list.")
else:
    print(f"The targeted value {target} is not in the list.")
