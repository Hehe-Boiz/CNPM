from CodeCommerce.model import Category, Product

def get_categories():
    return Category.query.all()

def get_products(kw=None, category_id=None):
    product = Product.query

    if category_id:
        product = product.filter(Product.category_id==category_id)

    if kw:
        product = product.filter(Product.name.contains(kw))

    return product.all()