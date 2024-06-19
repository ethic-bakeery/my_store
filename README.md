# Online Store Web Application

Welcome to the Online Store Web Application! This application allows users to create accounts, browse products and services, add items to their cart, make payments, and manage their profiles. Products are delivered to the specified delivery address.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication
- Browse products and services
- Add products to cart
- Update and delete cart items
- User profile management
- Admin functionalities for product management
- Payment processing
- Delivery based on specified address

## Technologies Used

- Backend: Django, Django REST Framework
- Frontend: React
- Database: SQLite (default, can be switched to PostgreSQL, MySQL, etc.)
- Other: HTML, CSS, JavaScript

## API Endpoints

### User

- `POST /register/`: Register a new user
- `POST /login/`: Login a user
- `GET /user/profile/<int:pk>/`: Get user profile
- `PUT /user/profile/<int:pk>/`: Update user profile

### Products

- `GET /products/`: List all products
- `POST /products/create/`: Create a new product (admin)
- `PUT /products/update/<int:pk>/`: Update a product (admin)
- `DELETE /products/delete/<int:pk>/`: Delete a product (admin)

### Cart

- `POST /cart/add/`: Add item to cart
- `DELETE /cart/delete/<int:pk>/`: Delete item from cart

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.

