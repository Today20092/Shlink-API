#SingleInstance Force
#Requires AutoHotkey >= 2.0 

; add the space at the end
pythonPath :="C:\Users\Ayoub\Documents\Shlink API\shorten-url.py "

^Numpad1::{

    LongUrl := A_Clipboard

    ToolTip "Shortening URL"
    SetTimer () => ToolTip(), -5000
    ; This needs to be changed to your path to the python file
    RunWait(pythonPath LongUrl,,"Hide")

    Tooltip "Your short url has been copied to clipboard: `n" . A_Clipboard
    SetTimer () => ToolTip(), -5000
}

