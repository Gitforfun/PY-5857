import re

pattern = r"^[a-z]+\.py$"  # raw

rows = [
    'test.pyc',
    'simple.txt',
    'app.py'
]

for row in rows:
    print(re.findall(pattern, row))
