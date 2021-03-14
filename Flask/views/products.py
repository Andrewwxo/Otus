from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

product_app = Blueprint("product_app", __name__)

PRODUCTS = {
    1: "Fruits",
    2: "Vegetables",
    3: "Meat",
    4: "Bread"
}

@product_app.route("/", endpoint="list")
def product_list():
    return render_template("products/index.html", products=PRODUCTS)

@product_app.route("/<int:product_id>/", endpoint="details")
def product_details(product_id):
    if product_id not in PRODUCTS:
        raise NotFound(f"Product with id {product_id} doesn't exist!")
    product_name = PRODUCTS[product_id]

    return render_template("products/index.html",
                           product_id=product_id,
                           product_name=product_name,
                           )
@product_app.route("/add", methods=["GET", "POST"], endpoint="add")
def product_add():
    return render_template("products/add.html")