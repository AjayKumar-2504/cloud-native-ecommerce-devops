from fastapi import FastAPI

app = FastAPI(
    title="E-Commerce Product Service",
    version="1.0.0"
)


products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 65000
    },
    {
        "id": 2,
        "name": "Keyboard",
        "price": 2500
    },
    {
        "id": 3,
        "name": "Mouse",
        "price": 1200
    }
]


@app.get("/")
def root():
    return {
        "service": "product-service",
        "status": "running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/products")
def get_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:
        if product["id"] == product_id:
            return product

    return {
        "error": "Product not found"
    }
