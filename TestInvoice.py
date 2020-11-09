import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def product():
    product = {'qnt': 2.0, 'unit_price': 3.0, 'discount': 10.0}
    return product

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalculateTotalImpurePrice(invoice, products):
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculatetotalDiscount(invoice, products):
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    assert invoice.totalPurePrice(products) == 69.38

# Test for the ability to correctly add a product
def test_CanAddProduct(invoice, product):
    assert invoice.addProduct(product['qnt'], product['unit_price'], product['discount']) == product

# Test for the ability to correctly display a summary list of products
def test_CanDisplayProducts(invoice, products):
    assert invoice.displayProducts(products) == 'Pen\t\t10\t\t3.75\t\t5\nNotebook\t\t5\t\t7.5\t\t10\n'