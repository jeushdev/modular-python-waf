from app import create_app

# Instantiate the application out of the factory dynamically
app = create_app()

@app.route('/')
def home():
    return "<h1>WAF Sandbox Root</h1><p>Secure backend environment is running cleanly.</p>"

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    return "<h3>Success: Request passed through the firewall cleanly!</h3>"

if __name__ == '__main__':
    app.run(debug=True)