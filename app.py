from flask import Flask, request

from views.products import product_app


app = Flask(__name__)

app.register_blueprint(product_app, url_prefix="/products")


@app.route("/", methods=["GET", "POST"])
def delivery_products():
    print(request.environ)
    if request.method == "GET":
        return " Доставка продуктов питания "


    name = request.form.get("name")
    return f"Delivery of {name}!"


@app.route("/delivery/")
@app.route("/delivery/<name>/")
def delivery(name="products"):
    return f"Delivery  of {name}!"


if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True,
    )