Fruits = {"Mango", "Apple", "Cherry"}
Vegetables = {"Cabbage", "coliflower", "avocado"}

def add_to_sets(st, item):
    return st.add("Rakitm")

def remove_from_sets(st, item):
    return st.remove("Mango")

def union_of_sets(st1, st2):
    return st1.union(st2)

def intersection_of_sets(st1, st2):
    return st1.intersection(st2)

def difference_in_sets(st1, st2):
    return st1.difference(st2)

def is_subset_sets(st1, st2):
    st1.issubset(st2)

def is_superset(st1, st2):
    st1.issuperset(st2)

add_to_sets(Fruits, "Banana")
print(Fruits)
print(union_of_sets(Fruits, Vegetables))
print(intersection_of_sets(Fruits, Vegetables))
print(difference_in_sets(Fruits, Vegetables))
print(is_subset_sets(Fruits, Vegetables))
print(is_superset(Fruits, Vegetables))