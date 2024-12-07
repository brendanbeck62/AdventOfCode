import time
import random
import sys

while True:
    print(f'''First Line {random.randint(1,10)}
Second Line {random.randint(1,10)}        
Third Line  {random.randint(1,10)}''')
    sys.stdout.write("\x1b[1A"*4) # Cursor up 3 lines
    time.sleep(0.5)