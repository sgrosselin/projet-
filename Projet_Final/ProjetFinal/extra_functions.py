def get_float_input(prompt):
    while True:
        # Constantly check if a value was entered followed by Enter
        try:
            # Put the value entered by user in "entree"
            entree = input(prompt)
            # Try to transform it into a float, if it cannot, we go to "except"
            value = float(entree)
            break
        except ValueError:
            # If input is not a float we get a ValueError
            print("Invalid input, please try again.")
    return value