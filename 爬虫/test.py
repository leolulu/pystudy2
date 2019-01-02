import os
from retry import retry

print(
    os.getcwd()
)

print(
    os.path.abspath(__file__)
)
