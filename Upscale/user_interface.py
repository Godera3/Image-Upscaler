def get_upscaling_factor():
    """
    Prompt the user to enter an upscaling factor.
    :return: The chosen upscaling factor as an integer.
    """
    while True:
        try:
            factor = int(input("Enter upscaling factor (e.g., 2, 3, 4): "))
            if factor < 2:
                print("Please enter a factor of 2 or greater.")
            else:
                return factor
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
