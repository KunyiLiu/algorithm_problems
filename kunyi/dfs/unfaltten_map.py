# Input:
# {
#   "a": 1,
#   "b": {
#     "c": 2,
#     "d": { "e": 3 }
#   }
# }

# Output (dotted path map):
# {
#   "a":     1,
#   "b.c":   2,
#   "b.d.e": 3
# }

# DFS, helper(nested_object, prefix), if value is nested -> continue;
# else output to the result
# edge case: what if there is b.c in the keys of nested object
def flatten_map(input):
    result = {}
    # edge case: empty
    if input is None or len(input) == 0:
        return result

    def helper(nested_obj, prefix=""):
        if nested_obj is None:
            return 

        for key, val in nested_obj.items():
            # create a new varaible instead of overwriting
            new_prefix = f"{prefix}.{key}" if prefix else key
            if isinstance(val, dict):
                # top-down
                helper(val, new_prefix)
            else:
                result[new_prefix] = val

        return 

    helper(input)
    return result

def flatten_map_iterative(input):
    result = {}
    # edge case: empty
    if input is None or len(input) == 0:
        return result

    stack = [(input, "")]
    while stack:
        current_dict, prefix = stack.pop()

        for key, val in current_dict.items():
            new_prefix = f"{prefix}.{key}" if prefix else key
            if isinstance(val, dict):
                stack.append((val, new_prefix))
            else:
                result[new_prefix] = val

    return result

input ={
  "a": 1,
  "b": {
    "c": 2,
    "d": { "e": 3 }
  }
}

result = flatten_map(input)
print(f"recursion result: {result}")
print(f"iterative result: {flatten_map_iterative(input)}")

################ 
def flatten_map_list(input):
    result = {}
    # edge case: empty
    if input is None or len(input) == 0:
        return result

    def helper(nested_obj, prefix=""):
        if nested_obj is None:
            return 

        if isinstance(nested_obj, dict):
            for key, val in nested_obj.items():
                new_prefix = f"{prefix}.{key}" if prefix else key
                helper(val, new_prefix)
        elif isinstance(nested_obj, list):
            for idx, val in enumerate(nested_obj):
                new_prefix = f"{prefix}[{idx}]"
                helper(val, new_prefix)
        else:
            result[prefix] = nested_obj

        return 

    helper(input)
    return result


input = {
  "user": {
    "name": "Alice",
    "skills": ["Python", "Go"],
    "preferences": {
      "theme": "dark"
    }
  },
  "active": True
}

result = flatten_map_list(input)
print(result)

######### unflatten ######
# input {'a': 1, 'b.c': 2, 'b.d.e': 3}. ##

def unflatten(input):
    result = {}
    if len(input) == 0:
        return result

    for nested_key, val in input.items():
        parts = nested_key.strip().split(".")
        # generate nested structure till the last one 
        cur = result
        for p in parts[:-1]:
            if p not in cur:
                cur[p] = {}
            cur = cur[p]

        cur[parts[-1]] = val
    return result

input = {'a': 1, 'b.c': 2, 'b.d.e': 3}
print(f"unflatten result is {unflatten(input)}")
