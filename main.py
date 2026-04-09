from pathlib import Path
import sys
import json
import random
import subprocess
import background
import kvantum

command = ""

def getArgs():
  global command
  if len(sys.argv) > 1:
    command = sys.argv[1]

configPath = Path.home() / ".config" / "BgManager" / "config.json"

def getConfig():
  with open(configPath, 'r') as configFile:
    return json.load(configFile)

def getCommand():
  if command == "update":
    background.setTerminalColor()
    return

  if not configPath.exists():
    sys.exit("No config found\nPlease make one at the path ~/.config/BgManager/config.json\nFormatting instructions are in the script's readme")

  config = getConfig()

  if not config[command]:
    sys.exit(f"Command {command} not found")

  info = config[command]

  if info.get("Type") == "custom" and info.get("Backgrounds"):
    selection = random.choice(info["Backgrounds"])
    background.setWallpaper(selection["Background"])

    if selection.get("ChangeTerminal", True):
      background.setTerminalColor(selection.get("Color", "auto"))

    if selection.get("ChangeKvantum", False):
      kvantum.setKvantumColor(selection.get("Color", "auto"))

    if selection.get("Commands"):
      for item in selection.get("Commands"):
        subprocess.run(item, shell=True)
    return
  files = [f for f in Path(info["Folder"]).iterdir() if f.is_file()]
  selection = random.choice(files)
  background.setWallpaper(selection)

  if info.get("ChangeTerminal", True):
    background.setTerminalColor()

  if info.get("ChangeKvantum", False):
    kvantum.setKvantumColor()

  if info.get("Commands"):
    for item in info.get("Commands"):
      subprocess.run(item, shell=True)

getArgs()
getCommand()

if command == "":
  sys.exit()