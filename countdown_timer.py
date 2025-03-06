import time

# In Python, the following values are considered False in a boolean context:
#0 (integer zero) 0.0(float zero) None Empty sequences(e.g., "", [], ())
 #Empty dictionaries({})
# quotient, remainder = divmod(dividend, divisor)
# /r is carriage return character, it will overwrite the output like 02:04 --> 02:03, without it will print both 02:04 and 02:03
def countdown_timer(seconds):
    while seconds:
     minutes, secs = divmod(seconds, 60)
     timer = f"{minutes:02d}:{secs:02d}" # 02d is format specifier, 0- pad with zeroes, 2- 2 characters wide, d - integer
     print(timer)
     time.sleep(1) #A countdown timer needs to wait for 1 second between each update. otherwise, it will countdown instantly making it useless
     seconds -=1  # decrease seconds by 1
    print("Time's up! ")

try:
    second_input = int(input("Please enter the number of seconds you want to countdown to: "))
    if second_input > 0:  # Ensure the input is a positive integer
        countdown_timer(second_input)
    else:
        print("Please enter a positive number of seconds.")
except ValueError:  # Handle non-integer input
    print("Invalid input! Please enter a valid integer.")