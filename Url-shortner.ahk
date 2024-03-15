#SingleInstance Force
#Requires AutoHotkey >= 2.0 

^Numpad1::{

    LongUrl := A_Clipboard

    ToolTip "Shortening URL"
    SetTimer () => ToolTip(), -5000
    # This needs to be changed to your path to the python file
    RunWait("C:\Users\Ayoub\Downloads\Librewolf Downloads\Shlink API\shorten-url.py " . LongUrl,,"Hide")

    Tooltip "Your short url has been copied to clipboard: `n" . A_Clipboard
    SetTimer () => ToolTip(), -5000
}

