from sanic import Sanic, response
from sanic.response import html, json, file, redirect, file_stream
from sanic.request import Request

app = Sanic("MYSitebyMUSAPAPPY")

# Configure Sanic to serve static files
app.static("/static", "./static")

# Route to serve index.html the main page
@app.route("/")
async def index(request):
    return await file("templates/index.html")

# Route for Portfolio Page
@app.route("/portfolio")
async def portfolio(request):
    return await file("templates/portfolio.html")

# Route to handle form submissions
@app.route("/submit_form", methods=["POST"])
async def submit_form(request: Request):
    # Access form data
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Process the data (e.g., save to database, send an email, etc.)
    print(f"Name: {name}, Email: {email}, Message: {message}")

    # Redirect to the Thank You page
    return redirect("/thank_u")

    # Respond to the client
    return json({"status": "success", "message": "Thank you for your message!"})

# Route to serve the Thank You page
@app.route("/thank_u")
async def thank_you(request):
    return await file("thank_u.html")

# Route to serve CSS file
@app.route("/styles.css")
async def css(request):
    return await file("static/styles.css")

# Route to serve JavaScript file
@app.route("/script.js")
async def js(request):
    return await file("script.js")



# Start the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
