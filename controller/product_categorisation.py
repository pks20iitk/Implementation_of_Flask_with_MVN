from app import app


@app.route("/product/categories")
def product_categorization():
    return "This is product categorization operation and add you can remove product"