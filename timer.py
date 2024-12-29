import time

def run_timer(seconds:int = 5):
    """
     A Python timer that run for a specified number of seconds,
     otherwise will default to 5 seconds

     - seconds (int): Length of time to run in seconds. Defaults to 5s.
    """
    if int(seconds) <= 0:
        raise ValueError("Timer duration must be greater than 0 seconds.")
    
    print(f"Timer starting for {seconds} seconds.")
    time.sleep(int(seconds))
    print("Time's up!!")

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
