# Prompt for Creating React Frontend for Azure SQL Django API

**Goal:** Create a modern, responsive React application to serve as the frontend for an existing Django REST API.

## 1. Project Setup
- **Framework:** React 18+ (use Vite for scaffolding).
- **Styling:** Tailwind CSS (configured for a premium, vibrant look).
- **Routing:** React Router DOM v6+.
- **HTTP Client:** Axios (or Fetch) with a configured base instance.
- **State Management:** React Context or just local state/props for simplicity (or TanStack Query if you prefer).

## 2. API Backend Details
- **Base URL:** `http://localhost:8000/api`
- The backend handles CORS (ensure it's enabled on the backend or set up a proxy in Vite).
- **Resources:**

### A. Stores
- **Endpoint:** `/stores/`
- **Fields:** `store_id` (integer, unique), `store_location` (string).
- **Actions:** List, Create, Update (`/stores/<id>/`), Delete (`/stores/<id>/`), Delete All (`/stores/deleteAll/`).

### B. Products
- **Endpoint:** `/products/`
- **Fields:** `id` (auto), `name` (string), `description` (text), `price` (decimal).
- **Actions:** List, Create, Update (`/products/<id>/`), Delete (`/products/<id>/`), Delete All (`/products/deleteAll/`).

### C. Users
- **Endpoint:** `/users/`
- **Fields:** `id`, `username`, `email`.
- **Actions:** List, Create, View Details.

### D. Customers (New)
- **Endpoint:** `/customers/`
- **Fields:** `id`, `name`, `email`, `phone`, `created_at`.
- **Actions:** List, Create, Update, Delete.

### D. Orders
- **Endpoint:** `/orders/`
- **Fields:** 
    - `id`
    - `user` (Read-only in serializer, derived from session/first user on backend). 
    - `status` ('PENDING', 'COMPLETED', 'CANCELLED').
    - `created_at`
    - `items` (Array of objects: `{ product: <product_id>, quantity: <int> }`).
- **Actions:** 
    - **List:** Show ID, User, Status, Date, Total Items.
    - **Create:** Form to select multiple products and quantities. Submitted payload should be `{ items: [{ "product": 1, "quantity": 2 }, ...] }`. User is handled by backend.
    - **View:** Detail view showing order items.
    - **Delete:** (`/orders/<id>/`).

### E. Reviews (MongoDB)
- **Endpoint:** `/reviews/`
- **Fields:** `_id` (string), `product_id` (int), `customer_id` (int), `rating` (1-5), `comment` (string), `created_at`.
- **Actions:** List (supports `?product_id=<id>`), Create, Update, Delete.

## 3. UI/UX Requirements
- **Navigation:** A top or side navigation bar to switch between:
    - Dashboard (Overview)
    - Stores
    - Products
    - Users
    - Orders
- **Design System:** 
    - Use a "Premium/Vibrant" aesthetic. 
    - Use cards for lists/grids (e.g., Product Grid).
    - Use tables for data-heavy views (e.g., Orders List).
    - Use modals or drawer forms for "Create/Edit" actions to keep it single-page feel.
    - **"Wow" Factor:** Add hover effects, smooth transitions between pages, and perhaps a subtle gradient background.
- **Product Reviews (Customer Reviews):** 
    - The backend now requires `customer_id` when creating a review.
    - When fetching reviews (`GET /api/reviews/?product_id=<id>`), the response includes `customer_name`.
    - You may need to create a Customer first (`POST /api/customers/`) or select from a list to attach to a review.

## 4. Implementation Steps
1.  Initialize Vite project with React + Tailwind.
2.  Setup `api.js` Axios instance.
3.  Create reusable components (Card, Button, Input, Modal).
4.  Implement "Stores" and "Products" CRUD pages first.
5.  Implement "Orders" page with a "Create Order" wizard/form (selecting products).
6.  Implement "Reviews" section linked to Products.
7.  Add finishing touches (animations, toast notifications for success/error).

---
**Note:** The backend automatically assigns the first user if no auth token is provided, so you can skip complex login/auth pages for this specific version unless you want to implement JWT handling.
