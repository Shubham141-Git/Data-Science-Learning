# Without __init__.py file, we import in following way
from utils import calc # here we are importing the module from the package and then we have to specify the module name to access the class and function in the module.

c=calc.Calulcator()

ans=c.add(1,2,3)
print(ans)
c.get_history()


# With __init__.py file, we can import in following way
from utils import Calculator # here we are directly importing the class from the package without specifying the module name.

CC=Calculator()
ans=CC.add(1,2,3)
print(ans)