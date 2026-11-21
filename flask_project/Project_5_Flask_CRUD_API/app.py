from flask import Flask, request

app = Flask(__name__)

products = []
next_id = 1

@app.route('/api/products', methods = ["POST"])
def create_product():
    global next_id

    data = request.get_json()

    if not data:
        return {"error":"Request body is required"}, 400
    
    name = data.get("name")
    price = data.get("price")
    category = data.get("category")

    if not name or price is None or not category:
        return {"error":"name, price and category are required"},400
    
    new_product = {
        "id" : next_id,
        "name" : name,
        "price" : price,
        "category" : category
    }
    products.append(new_product)
    next_id += 1

    return {
        "message":"Product created successfully",
        "data" : new_product
    },201 

@app.route('/api/products',methods=['GET'])
def get_products():
    return{
        "count":len(products),
        "data": products
    },200

@app.route('/api/products/<int:product_id>', methods = ['PUT'])
def update(product_id):

    product = next(
        (p for p in products if p['id'] == product_id),None)
    
    if product is None:
        return {"error":"product not found"},404

    data = request.get_json()

    if not data:
        return{"error":"Body is required"},400
    
    name = data.get("name")
    price = data.get("price")
    category = data.get("category")

    if not name or price is None or not category:
            return {"error":"name, price and category are required"},400

    product["name"] = name
    product["price"] = price
    product["category"] = category

    return {"messege":"Product updated successfully",
            "data":product},200
    
@app.route("/api/products/<int:product_id>", methods=["PATCH"])
def patch_product(product_id):

    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )

    if product is None:
        return {
            "error": "Product not found"
        }, 404

    data = request.get_json()

    if not data:
        return {
            "error": "Request body is required"
        }, 400

    allowed_fields = ["name", "price", "category"]

    for key in data:
        if key not in allowed_fields:
            return {
                "error": f"Invalid field: {key}"
            }, 400

    if "name" in data:
        product["name"] = data["name"]

    if "price" in data:
        product["price"] = data["price"]

    if "category" in data:
        product["category"] = data["category"]

    return {
        "message": "Product partially updated",
        "data": product
    }, 200

@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):

    product = next(
        (p for p in products if p["id"] == product_id),
        None
    )

    if product is None:
        return {
            "error": "Product not found"
        }, 404

    products.remove(product)

    return {
        "message": "Product deleted successfully",
        "data": product
    }, 200

if __name__ == '__main__':
    app.run(debug=True)