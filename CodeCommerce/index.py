from flask import render_template, request
import dao
from CodeCommerce.__init__ import app


@app.route('/')
def index():
    return render_template("index.html", category=dao.get_categories(), products=dao.get_products(category_id=request.args.get('category_id'), kw=request.args.get('kw')))


if __name__ == "__main__":
    app.run(debug=True)
