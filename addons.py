from pathlib import Path
import json
import subprocess

addonsList = Path.home() / ".config" / "BgManager" / "addons.json"

def getAddonsFile():
  if not addonsList.exists():
    with open(addonsList, "w") as file:
      json.dump([], file)

  with open(addonsList, "r") as file:
    return json.load(file)

def getAddonScripts():
  addons = getAddonsFile()

  for addon in addons:
    subprocess.run(addon, shell=True)