## 8-16. Imports: 
# 
# Using a program you wrote that has one function in it, 
#   store that function in a separate file. 
# 
# Import the function into your main program file, and call 
#   the function using each of these approaches:
# 
#          import module_name
#          from module_name import function_name
#          from module_name import function_name as fn 
#          import module_name as mn
#          from module_name import *

# Method number 1
import Sandwiches
Sandwiches.make_sandwich('nutella','bananas')

# Method number 2
from Sandwiches import make_sandwich
make_sandwich('peperoni')

# Method number 3
from Sandwiches import make_sandwich as ms
ms('cucumber', 'ketchup', 'lettuce')

# Method number 4
import Sandwiches as sand
sand.make_sandwich('cat')

# Method number 5\
from Sandwiches import *
Sandwiches.make_sandwich('egg')