#!/usr/bin/python
print("running")
import os
print("import complete")
def files(path):
  for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        yield file
for file in files("/files"):
  print(file)
