# Simple Product API with Flask
This is simple product API with Flask and Postgres

## Endpoint

 - "/products", POST, to add product into database
 - "/products", GET, to get list of products with sorting, sorting works with url parameters
 - "/products/< id >" , GET, to get detail of product
 
 ## Sort
 Sorting works with url parameters where will use "sort" with usage :
 
 - "newest" for sorting from newest product
 - "highest" for sorting from highest price 
 - "lowest" for sorting from lowest price
 - "az" for sorting product name (A-Z)
 - "za" for sorting product name (Z-A)

## Data Model
Product data model consist of 6 column of id, name, price, description, quantity and created_at.