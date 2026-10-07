# 1. Import the whole module → use module.function()
import math_module
print(math_module.add_m(4, 5))


# 2. Import a specific function → use function() directly
from math_module import add_m
print(add_m(4, 5))


# 3. Import the package → access its submodules through package
import mathpackage
print(mathpackage.addition.add_p(1, 2))
print(mathpackage.subtraction.sub_p(1, 2))


# 4. Import specific functions from submodules → use functions directly
from mathpackage.addition import add_p
from mathpackage.subtraction import sub_p
print(add_p(1, 2))
print(sub_p(1, 2))


# 5. Import submodules → use package.submodule.function()
import mathpackage.addition
import mathpackage.subtraction
print(mathpackage.addition.add_p(1, 2))
print(mathpackage.subtraction.sub_p(1, 2))