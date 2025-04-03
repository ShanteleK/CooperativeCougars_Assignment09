#main.py
from dbconnector_Package.dbconnector import *
from product_Package.product import *


import pyodbc


if __name__ == "__main__":

    db_manager = dbconnector()
    conn = db_manager.connect_to_database()
    
 
    product_manager = Product(conn)
    random_product = product_manager.fetch_random_product()

   
    manufacturer_name = product_manager.fetch_manufacturer(random_product["ManufacturerID"])


    brand_name = product_manager.fetch_brand(random_product["BrandID"])

