#Import Numpy
import numpy as np

# Starting step
step = 15

# Roll the dice
dice = np.random.randint(1,7)
print(dice)
# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice >=3 and dice <6 :
     step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(step)