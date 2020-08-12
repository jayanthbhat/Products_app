# Products_app

## Django application to display Products by Category and Subcategory

## Add Products by filtering on category and subcategory using django forms and django templating.


### 0 - Create a virtual env for the project 
### 1 - Django Model for categories 
### 2 - Django Model for Subcategories linked to categories 
### 3 - Django Model for storing products with linked Subcategories 
### 4 - API to get all categories 

url: /api/list-categories/?category_id=1

### 5 - API to get subcategories for a category 

url: /api/list-subcategories/?category_id=2

### 6 - API to get all products for a category 

url: /api/list-product-categories/?category_id=1

### 7 - API to get all products for a subcategory 

url: /api/list-product-subcategories/?subcategory_id=2

### 8 - API to post new product under existing subcategory and category 
POST AND GET

url: /api/add-products/
