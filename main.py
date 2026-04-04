from pathlib import Path
import sys
import json
import background

command = ""

def getArgs():
  global command
  if len(sys.argv) > 1:
    command = sys.argv[1]

configPath = Path.home() / ".config" / "BgManager" / "config.json"

def getConfig():
  with open('data.json', 'r') as configFile:
    return json.load(configFile)

def getCommand():
  if command == "update":
    background.setTerminalColor()

  if not configPath.exists():
    sys.exit("No config found\nPlease make one at the path ~/.config/BgManager/config.json\nFormatting instructions are in the script's readme")

  if not config[command]:
    sys.exit(f"Command {command} not found")

getArgs()
getCommand()

if command == "":
  sys.exit()