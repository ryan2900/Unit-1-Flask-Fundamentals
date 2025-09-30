from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return f"""<h2>Query Parameters </h2
            <ul>
                <li> Searching: 
                    <ul> 
                        <li><a href="/search">/search</a></li>
                        <li><a href="/search?q=python&page=2">/search?q=python&page=2</a></li>
                    </ul>
                </li>
                <li> Products: 
                    <ul> 
                        <li><a href="/products">/products</a></li>
                        <li><a href="/products?page=3&max_price=100.50">/products?page=3&max_price=100.50</a></li>
                    </ul>
                </li>
            </ul>
"""


@app.route("/search")
def search():
    query = request.args.get("q", "Nothing!")
    page = request.args.get("page", "1")
    return f"Searching for: '{query}' on page {page}"


@app.route("/products")
def products():
    page = request.args.get("page", "1", type=int)
    price = request.args.get("max_price", type=float)
    return f"Page:{page} (type: {type(page)}), Max Price:{price}"


if __name__ == "__main__":
    app.run(debug=True)