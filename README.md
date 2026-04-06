# Background Manager

This just a simple script to change your background from a folder of images and the terminal color too  
  
This is designed for KDE and Kitty Terminal, so if you wish to use this script but don't have one of them, you'll probably have to edit it to accommodate

## Dependencies

* Python
* Extcolors
* KDE
* Kitty Terminal

As mentioned above, you can always edit the script for any other DE or terminal

### Installing

#### Installing the script
Simply clone the repo and run the script
`git clone https://github.com/Lordpun/Background-Manager`

Enter the folder
`cd Background-Manager`

Setup the virtual enviroment
`python -m venv .venv`

Install extcolors
`pip install extcolors`

Exit
`deactivate`

#### Setting up the run scritp

Make it executable
`chmod +x run.sh`

#### Config

Make a config at the path in the config section below
Edit it to your choice

## How to use

### Making the config

In order to use this, you need to make the config yourself.  
The path is set to ~/.config/BgManager/config.json

The config structure is:  
```
{
  "Command": {
    "Folder": "Path",
    "ChangeTerminal": Bool
  }
}
```

For each set of wallpapers you have (Assuming you have multple sets), you need to create a new command section following the same formatting    
Avoid the name update, the script will not recgonize it as a custom command.  
  
ChangeTerminal is optional. It's only needed if you don't wish for it to change the terminal color.

#### Custom presets

You can set a custom color for a background if you don't like the picked color

```
{
  "Command": {
    "Type": "Custom",
    "Backgrounds": [
      {
        "Background": "Path",
        "ChangeTerminal": Bool
        "Color": "Hex code"
      }
    ]
  }
}
```
  
If you have ChangeTerminal set to false, you don't need Color

### Calling the script  

#### Running normally

Run `path/to/script/run.sh command`

#### Updating just the terminal color
If you wish to simply update the terminal color, but don't wish to randomly select a background: simply just run `path/to/script/run.sh update`