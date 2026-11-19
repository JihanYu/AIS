from pathlib import Path

base_dir = Path(__file__).resolve().parent
file_path = base_dir.parent/ "build" / "keys.txt"

lines=[]
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        lines.append(line.rstrip('\n'))

for l in lines:
    print(l)

