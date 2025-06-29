Friends = {"name": "Rohit", "last name": "Yadav", "DOB": 2005}

def add_to_dict(Friends):
    Friends["age"] = 19
    return Friends

def update_dict(Friends):
    Friends["name"] = "Amit"
    return Friends

def delete_from_dict(Friends):
    del Friends['last name']
    return Friends

def get_all_keys(Friends):
    return list(Friends.keys())

def get_all_values(Friends):
    return list(Friends.values())

# Call and print results
add_to_dict(Friends)
update_dict(Friends)
delete_from_dict(Friends)

print("All Keys:", get_all_keys(Friends))
print("All Values:", get_all_values(Friends))
print("Final Dictionary:", Friends)
