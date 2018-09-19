from os.path import dirname,join

print(
    join(dirname(dirname(__file__)),'\public')
)