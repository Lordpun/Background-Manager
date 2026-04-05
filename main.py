from pathlib import Path
import sys
import json
import random
import background

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

  if not configPath.exists():
    sys.exit("No config found\nPlease make one at the path ~/.config/BgManager/config.json\nFormatting instructions are in the script's readme")

  config = getConfig()

  if not config[command]:
    sys.exit(f"Command {command} not found")

  info = config[command]

  files = [f for f in Path(info["Folder"]).iterdir() if f.is_file()]
  selection = random.choice(files)
  background.setWallpaper(selection)

  if info["ChangeTerminal"]:
    background.setTerminalColor()

getArgs()
getCommand()

if command == "":
  sys.exit()