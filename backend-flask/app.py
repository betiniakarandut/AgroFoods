from productsdao import connection

def get_all_products(cnx):

    cursor = cnx.cursor()

    query = "SELECT p.product_name, p.price_per_unit, u.unit_name FROM products p INNER JOIN units u ON p.um_id = u.um_id"

    cursor.execute(query)
    res = cursor.fetchall()

    rows = []
    for (product_name, price_per_unit, unit_name) in res:
        rows.append({
            "product_name": product_name,
            "price_per_unit": price_per_unit,
            "unit_name": unit_name
        })


    return rows


def insert_products(cnx):

    cursor = cnx.cursor()

    query = "INSERT INTO products (product_name, price_per_unit, um_id) VALUES('Spinnach', 5000, 2)"
    cursor.execute(query)
    cnx.commit()



def delete_products(cnx):
    cursor = cnx.cursor()

    query = "DELETE FROM products WHERE product_id = 24"
    cursor.execute(query)
    cnx.commit()


if __name__ == "__main__":
    # cnx = connection()
    # insert_products(cnx)
    # print("All products initially: ", get_all_products(cnx))
    # print('\n')
    # print('Current stock')
    # delete_products(cnx)
    # print("All products after delete: ", get_all_products(cnx))
    # cnx.close()