# %%

import sys
import os.path
from importlib import import_module

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.school import School

s = School("test")
print(s.name)
