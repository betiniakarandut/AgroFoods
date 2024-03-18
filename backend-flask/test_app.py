"""Test app.py"""
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend-flask/')))

from productsdao import connection
from app import (
    get_all_products,
    insert_products,
    delete_products
)


def test_get_all_products():
    """Test get_all_products(cnx)

    Argument
        cnx[str]

    Returns
        all products in the store
    """

    cnx = connection()

    products = get_all_products(cnx)

    assert isinstance(products, list)
    assert (len(products) > 0)


def test_insert_products():
    """Test insert_products(cnx)

    Argument
        cnx[str]

    Returns
        inserts a new product into the database
    """
    cnx = connection()

    insert_products(cnx)

    products = get_all_products(cnx)

    assert any(product["product_name"] == 'Spinnach' for product in products)


def test_delete_products():
    """Test delete_products(cnx)

    Argument
        cnx[str]

    Returns
        Deletes/Removes any given product from database
    """
    cnx = connection()

    delete_products(cnx)
    products = get_all_products(cnx)
    assert not any(product['product_name'] == 'Pineapple' for product in products)

