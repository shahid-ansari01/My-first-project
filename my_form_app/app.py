from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route to display the form
@app.route('/')
def index():
    return render_template('forms.html')  # Render the HTML form

# Route to handle form submission (POST)
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Process the form data (You can store it, display it, or do something else)
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Password: {password}")

        # Redirect to a thank you page or back to form
        return redirect(url_for('thank_you'))  # Redirect to a "thank you" page

# Thank you page after form submission
@app.route('/thank-you')
def thank_you():
    return "<h1>Thank You! Form submitted successfully.</h1>"

if __name__ == '__main__':
    app.run(debug=True)