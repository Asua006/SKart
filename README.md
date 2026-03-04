# SKart E-Commerce Platform

SKart is a Django-based web application designed to facilitate online shopping. It features a dynamic product catalog, category-based filtering, and a functional cart management system.

## Features

* **Product Display**: Dynamic rendering of products by category using a carousel interface.
* **Shopping Cart**: LocalStorage-based cart system allowing users to add, remove, and view items.
* **Product Details**: Dedicated views for individual product information and pricing.
* **Search Functionality**: Query-based product search to locate specific items across the store.
* **Order Placement**: Checkout form to collect user details and finalize orders.

## Project Structure

The project follows the standard Django directory structure:

* **shop/**: The primary application folder containing logic and templates.
* **templates/shop/**: HTML files for the frontend, including the base layout (`basic.html`) and specific pages like `index.html`, `cart.html`, and `productView.html`.
* **static/**: Directory for CSS and JavaScript assets.
* **media/**: Storage for uploaded product images.

## Installation

1. Clone the repository to your local machine.
2. Ensure Python and Django are installed.
3. Apply migrations using `python manage.py migrate`.
4. Start the development server with `python manage.py runserver`.
5. Access the application at `http://127.0.0.1:8000/`.

## Technology Stack

* **Backend**: Django (Python)
* **Frontend**: HTML5, CSS3, JavaScript (jQuery)
* **Styling**: Bootstrap 5
* **Database**: SQLite (Default)

---
