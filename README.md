# Background Manager

This just a simple script to change your background from a folder of images and the terminal color too  
  
This is designed for KDE and Kitty Terminal, so if you wish to use this script but don't have one of them, you'll probably have to edit it to accommodate

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

### Calling the script  

Simply run `python3 path/to/script/main.py/ command`
If you do not add command it will return an error.  
  
You can put this wherever, such as an alias for an example.  

## Dependencies

* Python
* KDE
* Kitty Terminal

As mentioned above, you can always edit the script for any other DE or terminal

### Installing

Simply clone the repo and run the script
`git clone https://github.com/Lordpun/Background-Manager`

Make a config at the path in the config section