# 🍜 Dapur Nusantara

<div align="center">

![Dapur Nusantara](https://img.shields.io/badge/Dapur-Nusantara-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?style=for-the-badge&logo=postgresql)

**Platform Manajemen Restoran Modern untuk Kuliner Nusantara** 🇮🇩

[Features](#-features) • [Tech Stack](#-tech-stack) • [Installation](#-installation) • [API Documentation](#-api-documentation) • [Database Schema](#-database-schema)

</div>

---

## 📖 Tentang Proyek

**Dapur Nusantara** adalah sistem manajemen restoran berbasis API yang dirancang khusus untuk mengelola operasional restoran kuliner Nusantara. Aplikasi ini menyediakan solusi lengkap mulai dari manajemen menu, pemesanan, pembayaran, hingga sistem kupon diskon.

### 🎯 Tujuan

- Mempermudah pengelolaan restoran dengan sistem digital yang terintegrasi
- Mendukung berbagai tipe layanan: Dine-in, Takeaway, dan Delivery
- Integrasi dengan berbagai payment gateway Indonesia
- Sistem kupon dan promosi yang fleksibel
- Tracking dan logging pembayaran yang transparan

---

## ✨ Features

### 👥 User Management
- Multi-role system (Customer, Staff, Admin)
- Autentikasi dan authorization
- Manajemen profil pengguna

### 🍽️ Menu Management
- Kategorisasi menu yang terstruktur
- Upload gambar menu
- Status ketersediaan real-time
- Waktu persiapan makanan

### 📦 Order System
- **3 Tipe Pesanan**: Dine-in, Takeaway, Delivery
- **6 Status Order**: Pending → Confirmed → Preparing → Ready → Completed/Cancelled
- Nomor meja untuk dine-in
- Alamat pengiriman untuk delivery
- Catatan khusus per item

### 💳 Payment Integration
- **Multiple Payment Methods**:
  - Cash
  - Credit/Debit Card
  - E-Wallet
  - QRIS
  - Bank Transfer
- Payment gateway integration ready
- Payment URL generation
- Transaction logging
- Refund support

### 🎟️ Coupon System
- Diskon persentase atau nominal tetap
- Minimum pembelian
- Batas maksimal diskon
- Limit penggunaan
- Periode validitas
- Tracking penggunaan coupon

### 📊 Analytics & Logging
- Payment event logging
- Order history tracking
- Gateway response storage
- IP address tracking

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern web framework untuk Python
- **SQLAlchemy** - ORM untuk database operations
- **Pydantic** - Data validation menggunakan Python type hints
- **PostgreSQL 16** - Relational database
- **Alembic** - Database migration tool

### Key Libraries
- **uuid-ossp** - UUID generation
- **psycopg2** - PostgreSQL adapter
- **python-jose** - JWT tokens
- **passlib** - Password hashing
- **python-multipart** - File upload support

---

## 🚀 Installation

### Prerequisites
```bash
- Python 3.11+
- PostgreSQL 16
- pip
```

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/dapur-nusantara.git
cd dapur-nusantara
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Database
```bash
# Buat database PostgreSQL
createdb dapurnusantara

# Import schema
psql -U postgres -d dapurnusantara -f database/schema.sql
```

### 5. Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit konfigurasi database
nano .env
```

**.env example:**
```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/dapurnusantara
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 6. Run Application
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Aplikasi akan berjalan di `http://localhost:8000`

---

## 📚 API Documentation

Setelah aplikasi berjalan, akses dokumentasi interaktif di:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Quick API Examples

#### Register User
```bash
POST /api/v1/users/register
{
  "email": "customer@example.com",
  "password": "securepass123",
  "full_name": "John Doe",
  "phone": "081234567890",
  "role": "customer"
}
```

#### Create Order
```bash
POST /api/v1/orders
{
  "order_type": "dine_in",
  "table_number": "A5",
  "items": [
    {
      "menu_item_id": "uuid-here",
      "quantity": 2,
      "notes": "Pedas level 3"
    }
  ],
  "coupon_code": "DISKON20"
}
```

#### Process Payment
```bash
POST /api/v1/payments
{
  "order_id": "uuid-here",
  "payment_method": "qris",
  "payment_gateway": "midtrans",
  "amount": 150000
}
```

---

## 🗄️ Database Schema

### Core Tables

#### Users
Menyimpan data pengguna (customer, staff, admin)

#### Categories & Menu Items
Struktur kategori dan menu restoran

#### Orders & Order Items
Sistem pemesanan dengan detail item

#### Payments & Payment Logs
Pembayaran dan logging transaksi

#### Coupons & Order Coupons
Sistem voucher dan tracking penggunaan

### Entity Relationship
```
Users (1) ──── (N) Orders
Orders (1) ──── (N) Order Items
Orders (1) ──── (N) Payments
Menu Items (N) ──── (1) Categories
Orders (N) ──── (N) Coupons (through Order_Coupons)
Payments (1) ──── (N) Payment Logs
```

---

## 📁 Project Structure

```
<rootPath>
└── microservices
    └── <service_name>
        ├── app
        │   ├── __init__.py
        │   ├── main.py
        │   ├── core
        │   │   ├── __init__.py
        │   │   ├── config.py
        │   │   └── security.py
        │   ├── api
        │   │   ├── __init__.py
        │   │   └── v1
        │   │       ├── __init__.py
        │   │       └── endpoints
        │   │           ├── __init__.py
        │   │           ├── <service_name>_endpoint.py
        │   │           └── auth.py
        │   ├── models
        │   │   ├── __init__.py
        │   │   ├── <service_name>.py
        │   │   └── user_model.py
        │   ├── schemas
        │   │   ├── __init__.py
        │   │   ├── <service_name>.py
        │   │   └── user_schema.py
        │   ├── crud
        │   │   ├── __init__.py
        │   │   ├── <service_name>.py
        │   │   └── user_crud.py
        │   ├── db
        │   │   ├── __init__.py
        │   │   ├── base.py
        │   │   └── session.py
        │   ├── auth
        │   │   ├── __init__.py
        │   │   ├── jwt.py
        │   │   └── oauth2.py
        │   ├── tests
        │   │   ├── __init__.py
        │   │   ├── test_example.py
        │   │   └── test_auth.py
        ├── alembic
        │   ├── env.py
        │   ├── script.py.mako
        │   └── versions
        ├── scripts
        │   └── init_db.py
        ├── .env
        ├── .gitignore
        ├── requirements.txt
        ├── Dockerfile
        └── README.md
```

---

## 🔐 Security Features

- Password hashing dengan bcrypt
- JWT token authentication
- Role-based access control (RBAC)
- SQL injection protection via SQLAlchemy
- CORS configuration
- Request validation dengan Pydantic

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_orders.py
```

---

## 📈 Roadmap

- [ ] Dashboard admin real-time
- [ ] Notifikasi real-time (WebSocket)
- [ ] Mobile app integration
- [ ] Inventory management
- [ ] Employee scheduling
- [ ] Multi-branch support
- [ ] Loyalty program
- [ ] Analytics & reporting dashboard

---

## 🤝 Contributing

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buka Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@Ferd1y](https://github.com/Ferd1y)
- Email: FerdySaputra3828@gmail.com

---

## 🙏 Acknowledgments

- FastAPI documentation
- SQLAlchemy community
- PostgreSQL team
- Indonesian culinary heritage 🇮🇩

---

<div align="center">

**Made with ❤️ for Indonesian Culinary Industry**

⭐ Star this repo if you find it helpful!

</div>
