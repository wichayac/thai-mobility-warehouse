from pathlib import Path
import shutil
import hashlib

source = Path("sandbox/milestone_02/source.txt")
destination = Path("sandbox/milestone_02/output/source.txt")

destination.parent.mkdir(parents=True, exist_ok=True)

shutil.copy2(source, destination)

print(source.exists())
print(destination.exists())

with open(source, "rb") as source_file:
    source_content = source_file.read()
with open(destination, "rb") as destination_file:
    destination_content = destination_file.read()

if hashlib.sha256(content).hexdigest() == hashlib.sha256(content).hexdigest():
    print("Hashes match: True")
