# A Script for Autotype the codes

# how to run:

Create a Virtualenv using the following Command:

Windows (Tested on Win10):

py -m venv v
v\Scripts\activate

Linux/macOS:

python3 -m venv v
source v/bin/activate


# Install the required updated dependencies on the created Virtual ENV

Windows :

py -m pip install --upgrade -r req.txt

Linux/macOS:

python3 -m pip install --upgrade -r req.txt


# Now Run the main.py

Windows:

py main.py

Linux/macOS:

python3 main.py

The main.py will create a web Interface to copy things (text only) and then automatically starts to type when you press the type button (5 secs delay for switching to the Code editor/Notepad), open the webUI on mobile device and start to type enjoy :)