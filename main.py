import timer

def main():
    """
    Main function to ask the user for input and run the timer.
    """
    try:
        user_input = input(
        "Enter the timer duration in seconds "
        "(or press Enter/Return for default 10 seconds): "
        )
        if user_input.strip() == "":
            duration = 10  # Default duration
        else:
            duration = int(user_input)
            if duration <= 0:
                raise ValueError("Timer duration must be greater than 0 seconds.")
    except ValueError:
        print("Invalid input! Please enter a positive integer.")
        return

    # Run the timer with the provided duration
    timer.run_timer(duration)

if __name__ == "__main__":
    main()