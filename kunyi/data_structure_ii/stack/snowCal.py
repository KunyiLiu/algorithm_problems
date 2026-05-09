def snowCal(program):
    function_dict = {}

    # create a shared pointer, so can skip using while loop iter()
    # or just use a flat loop to handle parsing (parsing the function) => function_dict + main_program
    # execute the main_program using dfs

    result = 0
    main_program = [] 

    # dfs
    def execute(line):
        nonlocal result
        parts = line.strip().split()
        if parts[0] == "ADD":
            result += int(parts[1])
            return
        if parts[0] == "MUL":
            result *= int(parts[1])
            return

        # parts[0] == 'INV'
        for l in function_dict[parts[1]]:
            execute(l)

        return

    # parsing
    # Further: what if nested => use stack to record the function name ["outer", "inner"], pop when it is end

    func_name_stack = []
    for line in program:
        parts = line.strip().split()
        if not parts:
            continue
        
        cmd = parts[0]
        if cmd == "FUN":
            func_name_stack.append(parts[1])
            function_dict[parts[1]] = []
        elif cmd == "END":
            func_name_stack.pop()
        else:
            if func_name_stack:
                # still in function
                function_dict[func_name_stack[-1]].append(line)
            else:
                main_program.append(line)

    for l in main_program:
        execute(l)

    return result



program = ["FUN INCREMENT", "ADD 1", "END", "FUN INCREMENT2", "ADD 1", "MUL 2", "END", "MUL 2", "INV INCREMENT2", "ADD 3", "INV INCREMENT"]

result = snowCal(program)
print(f"Result is {result}")

program = ["FUN INCREMENT", "ADD 1", "END", "FUN INCREMENT2", "INV INCREMENT", "MUL 2", "END", "MUL 2", "INV INCREMENT2", "ADD 3", "INV INCREMENT"]

result = snowCal(program)
print(f"Result is {result}")

"""
what if nested function 
"""
program = ["FUN INCREMENT2", "FUN INCREMENT", "ADD 1", "END", "MUL 2", "END", "MUL 2", "INV INCREMENT2", "ADD 3", "INV INCREMENT"]

result = snowCal(program)
print(f"Result is {result}")

