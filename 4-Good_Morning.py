# Import Time...............!!!!!!!!!!
print()
import time

timestamp = time.strftime('%H:%M:%S')
print("TIME=", timestamp)
hour = int(time.strftime('%H'))
print("\nHours Is=", hour)
timestamp = time.strftime('%M')
print("Minute Is=", timestamp)
timestamp = time.strftime('%S')
print("Second Is", timestamp)

print()
if 0 <= hour <= 11:
    print("\t*****GOOD MORNING*****")
elif 11 <= hour <= 17:
    print("\t*****GOOD EVENING*****")
if 17 <= hour <= 24:
    print("\t*****GOOD NIGHT*****")
