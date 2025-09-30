from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
           <h1>Dynamic Routes Demo</h1>
<h2>Try: These URLS</h2>
<ul>
    <li><a href="/user/john">User Profile: john</a></li>
    <li><a href="/user/alice">User Profile: alice</a></li>
    <li><a href="/calc/10/+/5">Calculator: 10 + 5</a></li>
    <li><a href="/calc/9/*/3">Calculator: 9 * 3</a></li>
    <li><a href="/temp/c_to_f/100">Convert 100°C to °F</a></li>
    <li><a href="/temp/f_to_c/212">Convert 212°F to °C</a></li>
</ul> 
"""

@app.route('/user/<username>')
def user_profile(username):
    return f'''
     <h1>User Profile</h1>
 <p>Username: <strong>{username}</strong></p>
 <p>Profile Type: {type(username).__name__}</p>
 <p>Welcome to {username}'s profile page!</p>
 <nav>
    <a href="/"> Back to Homepage</a>
    <a href="/user/alice">Alice</a>
    <a href="/user/bob">Bob</a>
 </nav>    
'''

@app.route("/calc/<int:num1>/<operation>/<int:num2>")
def calculator(num1, operation, num2):
    operations = {
        '+' : num1 + num2,
        '-' : num1 - num2,
        '*' : num1 * num2,
        '/' : num1 / num2 if num2 != 0 else 'Error: Division by zero!'
    }
    if operation in operations:
        result = operations[operation]
        return f"{num1} {operation} {num2} = {result}"
    else:
        return f"Unknown operation! {operation}"

# 🔹 Temperature conversion route
@app.route("/temp/<conversion>/<int:value>")
def temperature_conversion(conversion, value):
    if conversion == "c_to_f":
        result = (value * 9/5) + 32
        return f"{value}°C = {result}°F"
    elif conversion == "f_to_c":
        result = (value - 32) * 5/9
        return f"{value}°F = {result:.2f}°C"
    else:
        return "Unknown conversion! Use 'c_to_f' or 'f_to_c'."

if __name__ == "__main__":
    app.run(debug=True)
