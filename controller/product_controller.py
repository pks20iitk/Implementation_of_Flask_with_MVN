from app import app


@app.route("/product/add")
def add_product():
    return "This is product add operation and add you can remove product"