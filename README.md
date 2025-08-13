# 🛒 Django E-Commerce Website

A simple e-commerce web application built with **Django** and **Bootstrap** that supports:
- Product listings and detail pages
- Add to Cart functionality
- Buy Now button for instant checkout
- LocalStorage-based cart persistence
- Checkout form to collect shipping details

---

## 📌 Features

- **Home Page** with product listings
- **Detail Page** for each product
- **Add to Cart**: Add products to a persistent cart stored in browser's LocalStorage
- **Buy Now**: Directly go to checkout with the selected product only
- **Checkout Page**:
  - Shows cart items with quantity and price
  - Calculates total automatically
  - Collects shipping details
- Dark theme UI with smooth animations

---

## 📂 Project Structure
ecomsite/
shop
├── shop/templates/
│ ├── index.html # Homepage with navbar & product list
│ ├── detail.html # Product detail page with Add to Cart & Buy Now
│ ├── checkout.html # Checkout page with order summary & shipping form
│
├── shop/static/
│ ├── css/ # Custom styles
│ 
│
├── manage.py
└── README.md

