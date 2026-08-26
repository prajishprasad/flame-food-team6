from flask import Flask, render_template, request, redirect, url_for, session

# Initialize the app
app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for sessions (to store cart data)

# Dummy data: cafes and menus
cafes = {
    "Cafe One": [
        {"name": "Coffee", "price": "Rs. 100"},
        {"name": "Sandwich", "price": "Rs. 70"},
        {"name": "Muffin", "price": "Rs. 80"},
    ],
    "Cafe Two": [
        {"name": "Tea", "price": "Rs. 20"},
        {"name": "Burger", "price": "Rs. 150"},
        {"name": "Fries", "price": "Rs. 120"},
    ],
    "Cafe Three": [
        {"name": "Pizza", "price": "Rs. 150"},
        {"name": "Pasta", "price": "Rs. 110"},
        {"name": "Salad", "price": "Rs. 100"},
    ],
    "Cafe One": ["Coffee", "Sandwich", "Muffin"],
    "Cafe Two": ["Tea", "Burger", "Fries"],
    "Cafe Three": ["Pizza", "Pasta", "Salad"],
    "Cafe Four": ["Idli", "Dosa", "Filter Coffee"]
}

@app.route("/")
def home():
    """Show list of cafes"""
    return render_template("index.html", cafes=cafes)

@app.route("/cafe/<name>")
def show_cafe(name):
    """Show menu of a cafe"""
    menu = cafes.get(name, [])
    return render_template("cafe.html", cafe=name, menu=menu)

@app.route("/add_to_cart/<cafe>/<item>")
def add_to_cart(cafe, item):
    """Add an item to the cart (stored in session)"""
    cart = session.get("cart", [])
    cart.append({"cafe": cafe, "item": item})
    session["cart"] = cart
    return redirect(url_for("view_cart"))

@app.route("/cart")
def view_cart():
    """View items in cart"""
    cart = session.get("cart", [])
    return render_template("cart.html", cart=cart)

@app.route("/checkout")
def checkout():
    """Clear the cart (no real payment)"""
    session["cart"] = []
    return "Thanks for ordering! Your cart is now empty."
    
if __name__ == "__main__":
    app.run(debug=True)
