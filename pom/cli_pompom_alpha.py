import time

def pomodoro_timer(work_duration, short_break, long_break, cycles):
    """
    A CLI Pomodoro Timer.
    
    Args:
        work_duration (int): Work duration in minutes.
        short_break (int): Short break duration in minutes.
        long_break (int): Long break duration in minutes.
        cycles (int): Number of work/break cycles before a long break.
    """
    for cycle in range(1, cycles + 1):
        print(f"\nCycle {cycle}/{cycles}")
        print("Work time! Stay focused.")
        countdown(work_duration * 60)

        if cycle < cycles:
            print("\nShort break! Relax for a bit.")
            countdown(short_break * 60)
        else:
            print("\nLong break! Take a longer rest.")
            countdown(long_break * 60)

    print("\nPomodoro session complete! Great job!")

def countdown(seconds):
    """
    Countdown timer that displays time remaining in minutes and seconds.
    
    Args:
        seconds (int): Duration of the countdown in seconds.
    """
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

if __name__ == "__main__":
    print("Welcome to the CLI Pomodoro Timer!")
    
    # Get user input for durations
    try:
        work_duration = int(input("Enter work duration (in minutes): "))
        short_break = int(input("Enter short break duration (in minutes): "))
        long_break = int(input("Enter long break duration (in minutes): "))
        cycles = int(input("Enter number of cycles before a long break: "))
        
        # Start the Pomodoro timer
        pomodoro_timer(work_duration, short_break, long_break, cycles)
    except ValueError:
        print("Invalid input! Please enter numbers only.")
