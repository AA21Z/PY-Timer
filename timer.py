import time

if __name__ == "__main__":
    seconds = input("Please provide length of time for timer: ")
    if seconds == "":
        # If empty value provided will default to value 5 (seconds)
        seconds = 5
    elif int(seconds) <= 0:
            raise ValueError
    print(f"Timer starting for {seconds} seconds.") 

    #Begin timer function for amount of seconds provided
    time.sleep(int(seconds))
    #End timer
    print("Time's up!!")
