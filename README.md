# chat-room

## Server Program 
### Consisting of:
`chat_server.py`

chat-room server program uses python socket to create server for chat-room. 

It acts as an interface between different clients. It relays one client's message to all other client.

It stores information of all the connected clients while running, and stores messages of client programs in a queue to be broadcasted to all other clients.

It uses threads for simultaneously sending and receiving of messages.


## Client Program 
### Consisting of:
### `main.py`

It is used to start the client GUI application.

### `chatui.py`

It defines the structure of the GUI window and its elements. 

The GUI is created using PyQt6 Designer. PyQt6 Designer is a GUI application that helps create GUI's using PyQt6/PySide6 libraries/modules and save them as XML files with .ui file extension.

The .ui file can be used directly to import GUI or can be converted in .py file using the Python User Interface Compiler(pyuic) which makes it easier to make finer changes to UI.
the `chatui.py` file is generated after compiling `chatroom.ui` file using pyuic as:
>pyuic6 -x chatroom.ui -o chatui.py

the -x argument makes the UI class in object file executable by adding `if name == "__main__"` function to it, which has Objects declared which make UI run.

### `uifunction.py`

This file has a class which inherits the UI structure class from `chatui.py` and defines functions to its widgets like buttons, labels, etc.

### `net_ui_interface`

This file provides functions in `uifunction.py` network elements and functions to the UI elements.

 #### `message_labels` : Contains class for dialog labels in UI. Used by `uifunction.py`.