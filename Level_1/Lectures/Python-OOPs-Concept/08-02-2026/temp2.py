'''  
from package_name import *
This imports:

everything from the package/module

so we can directly use functions/classes without writing module name again and again.'''

from utils import * # here we are importing everything from the package and we can directly use the functions and classes without specifying the module name.   


CC=Calculator()
ans=CC.add(1,2,3)
print(ans)