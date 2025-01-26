from flask import Flask, render_template

app = Flask("Kahoot")
app.secret_key = "123"


listings_data = [
    {
        "id": i + 1,
        "title": f"Оголошення №{i + 1}",
        "price": f"${10000 + (i * 1000):,}".replace(",", " "),
        "location": f"Квартал {i + 1}",
        "description": f"Детальний опис оголошення №{i + 1}. Чудова пропозиція в чудовому місці!"
    }
    for i in range(1200)
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about_us")
def about():
    return render_template("about.html")

@app.route("/listings")
def listings():
    return render_template("listings.html", listings=listings_data)

@app.route("/listings/<int:listing_id>")
def listing_details(listing_id):
    listing = next((item for item in listings_data if item["id"] == listing_id), None)
    if listing is None:
        return "Оголошення не знайдено", 404
    return render_template("listing_details.html", listing=listing)


app.run()
