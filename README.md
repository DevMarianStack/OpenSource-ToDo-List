# To-Do List Application

This project contains two versions of a To-Do List application:

1. **Website Version**: A simple web-based To-Do List application using HTML, CSS, and JavaScript.
2. **PC Version**: A console-based To-Do List application using Python, with instructions to create an executable.

## Project Structure

/todo-list
/website
index.html
styles.css
script.js
/pc
main.py
requirements.txt
README.md
README.md

## Website Version

1. Navigate to the `website` folder.
2. Open `index.html` in your web browser.

### Features

- Add tasks.
- Remove tasks by clicking on them.

## PC Version

1. Navigate to the `pc` folder.
2. Install Python if not already installed. You can download it from [Python's official website](https://www.python.org/).
3. Create the executable using PyInstaller:
   ```bash
   pip install pyinstaller
   pyinstaller --onefile main.py

	4.	The executable will be created in the dist folder within the pc directory. You can distribute and run this .exe file on Windows systems.

Features

	•	Add tasks by typing them in.
	•	Remove tasks by entering their number.

Contributing

Feel free to fork the repository and contribute improvements or features. Please submit a pull request with a description of your changes.

License

This project is licensed under the MIT License. See the LICENSE file for details.

### Creating the Executable

1. **Install PyInstaller**:
   - Open a command prompt or terminal and install PyInstaller:
     ```bash
     pip install pyinstaller
     ```

2. **Generate the Executable**:
   - Navigate to the `pc` directory in your command prompt or terminal and run:
     ```bash
     pyinstaller --onefile main.py
     ```
   - This command creates a standalone executable in the `dist` folder.

3. **Distribute the Executable**:
   - You can now distribute the `.exe` file found in the `dist` folder.
