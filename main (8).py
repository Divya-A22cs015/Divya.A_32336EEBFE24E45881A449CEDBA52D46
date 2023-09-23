#Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.

def linear_search_product(productList, targetProduct):
  indices=[]
  for index, product in enumerate(productList):
    if product==targetProduct:
      indices.append(index)
  return indices

#Example usage:
products=["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target="shoes"
target2="apple"
target3="boot"
result=linear_search_product(products, target)
result2=linear_search_product(products,target2)
result3=linear_search_product(products,target3)
print("target1 is in",(result),"and target2 is in",(result2),"and target3 is in",(result3))