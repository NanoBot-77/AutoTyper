from flask import Flask, render_template, request
from flask_cors import CORS
from service import type_code_automator

app = Flask(__name__, template_folder="template") # Ensure folder is named 'templates'
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        # Get the code from the form
        code_input = request.form.get('code')
        
        # Call the automation script
        # Note: This will block the browser until typing is finished
        type_code_automator(code_input)
        
        # return "Typing Done! You can go back."
        
    return render_template('index.html')

if __name__=="__main__":
    # Ensure this is running on the machine where you want the typing to happen
    app.run(debug=True, port=6050, host="0.0.0.0")