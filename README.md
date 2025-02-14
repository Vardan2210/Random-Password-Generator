# Random-Password-Generator
Password Generator
Overview
This is a Python program that generates a random password following a specific pattern: word – number – alphanumeric – word – number – alphanumeric. The generated password is displayed in a pop-up dialog box.
Features
	•	Generates a random password in the specified pattern.
	•	Uses external text files for word and alphanumeric lists.
	•	Displays the generated password via a Tkinter pop-up.

Requirements
	•	Computer running Windows, Linux, or MacOS
	•	Python (version 3 or higher)
	•	Visual Studio Code (or any preferred code editor)
	•	Two text files:
	1	words.txt: Contains a list of 450,000+ English words.
	2	alphanumericals.txt: Contains a list of common alphanumeric characters.
Dependencies
	•	random: For generating random numbers and selections.
	•	tkinter: For displaying the generated password in a pop-up dialog box.

Installation and Setup
	1	Install Python: Download and install Python 3 from python.org.
	2	Install Visual Studio Code: Download and install from VSCode.
	3	Download Word and Alphanumeric Lists:
	◦	Words file from: GitHub English Words
	◦	Alphanumericals file (custom or from a suitable source)
	4	Place ** and ** in the same directory as the script.

How It Works
	1	Reads words.txt and alphanumericals.txt into lists.
	2	Randomly selects a word, number (0–9), and alphanumeric character.
	3	Concatenates them in the order: word, number, alphanumeric.
	4	Repeats the above steps twice.
	5	Displays the final password using a Tkinter message box.
Example Password Format:
planet7Zebra2X

Usage
	1	Run the script with: python password_generator.py
	2	A pop-up window will display the generated password.

Resources Used
	•	Python Tutorial (YouTube): Python Full Course
	•	Tkinter Pop-up Tutorial (YouTube): Tkinter Dialog Box
	•	Random Number Function (GeeksForGeeks): Python randint
	•	Remove Trailing Newline (Kite): Remove newline

Closing Files
	•	Ensures both words.txt and alphanumericals.txt are closed after reading to prevent resource leaks.
Author
Vardan Chikara

