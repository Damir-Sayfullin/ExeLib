# Exelib - Library for Executable Files
### <a href=https://github.com/Damir-Sayfullin/ExeLib/blob/main/README-ru.md>На русском</a>
## About the Project
<p align="center">
    <a href=https://www.python.org/downloads/release/python-3917><img src="https://img.shields.io/badge/Python-3.9-green?style=for-the-badge" alt="Python Version"></a>
    <a href=https://github.com/Damir-Sayfullin/ExeLib/releases/tag/v1.0.0><img src="https://img.shields.io/badge/Version-1.0.0-red?style=for-the-badge" alt="Version"></a><br>
    <a href=https://github.com/Damir-Sayfullin/ExeLib/stargazers><img src="https://img.shields.io/github/stars/Damir-Sayfullin/ExeLib?style=for-the-badge&color=yellow" alt="Stars"></a>
    <a href=https://github.com/Damir-Sayfullin/ExeLib/watchers><img src="https://img.shields.io/github/watchers/Damir-Sayfullin/ExeLib?style=for-the-badge" alt="Watchers"></a>
</p>
 
The ExeLib project is a graphical application created using the tkinter library in Python. This application allows users to organize a collection of links to executable files (exe files) on their computer. Users can add links to files by specifying the filename and file path. They can also rename links and directly launch the selected exe file from the application. The collection of links is saved in a JSON file (paths.json) for future use. It is a useful tool for organizing and quickly accessing various exe files on user's computers.

<a href="https://ibb.co/kD5zHqz"><img src="https://i.ibb.co/FYmcx8c/Exe-Lib-Image.png" alt="Exe-Lib-Image" width=600></a> 

## Installation
There are two ways to install and run the ExeLib application:
1. Clone the repository using `git clone https://github.com/Damir-Sayfullin/ExeLib.git`  and run `Tkinter.py`.
2. Download the installer  `ExeLib-setup.exe` or the application `ExeLib.exe` from the release assets. Current version: [v1.0.0](https://github.com/Damir-Sayfullin/ExeLib/releases/tag/v1.0.0)

## Usage
- Add an executable file to the library by clicking the `Добавить` button. Select the file in the file dialog and enter the file name.
- To remove an executable file from the library, select it from the list and click the `Удалить` button.
- To rename an executable file in the library, select it from the list and click the `Переименовать` button. Enter a new file name and select a new file if you want to change it.
- To launch the selected executable file, select it from the list and click the `Запустить` button.
- To save the changes and the list of executable files, click the `Сохранить` button. They will be saved to the paths.json file, which is created in the same folder as Tkinter.py or the ExeLib application.

## Documentation
### Methods
`__init__(self, master)` - constructor of the ExeLibrary class. Takes a master object, which is the root tkinter window.

`_add_path(self)` - method for adding a new link to an exe file to the collection. Opens a file dialog where the user can select an exe file, and then prompts the user for the file name.

`_remove_path(self)` - method for removing the selected link to an exe file from the collection. Removes the selected item from the list of links.

`_rename_path(self)` - method for renaming the selected link to an exe file. Prompts the user for a new file name and a new file path.

`_run_path(self)` - method for running the selected exe file. Retrieves the path to the selected file, determines the directory of the file, and executes it using subprocess.run().

`_save_paths(self)` - method for saving the list of links to exe files to the paths.json file. Serializes the list of links and saves it to the file.

`_load_paths(self)` - method for loading the list of links to exe files from the paths.json file. Deserializes the list of links from the file and adds them to the list.
