from flask import Flask, render_template
import os

# Initialize Flask App
# Setting the template folder to the current directory or a specific templates folder
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    """
    Serves the main game interface.
    The frontend is handled entirely by index.html for zero-latency gameplay.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Print helpful startup instructions
    print("\n" + "="*50)
    print("🐍 Premium Snake Game Server Starting...")
    print("🌐 Open your browser and go to: http://localhost:5000")
    print("="*50 + "\n")
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)