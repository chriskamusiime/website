import shutil
from pathlib import Path

# Path to your source folder with audio files
source_dir = Path("")  # <- change this!

for i in range(0, 10):
    lektion_str = f'Lektion_0{i}'
    destination_dir = Path(lektion_str)
    destination_dir.mkdir(exist_ok=True)

    for file in source_dir.iterdir():
        if file.is_file() and lektion_str in file.name:
            dest_path = destination_dir / file.name
            shutil.copy(file, dest_path)
            print(f"🎧 Copied: {file.name} to {destination_dir}")
