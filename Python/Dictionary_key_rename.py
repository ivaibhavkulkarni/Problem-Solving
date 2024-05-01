fruits = {
    'apples' : 20,
    'banana' : 50,
    'papaya' : 60

}




old_key = input()
new_key = input()

new_dict = {}
for k, v in fruits.items():
    if k == old_key:
        new_dict[new_key] = v
    else:
        new_dict[k] = v
print(list(new_dict.items()))