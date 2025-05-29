# HonestyBox - Farm-Gate Sales Platform

<div align="center">
  <img src="https://img.shields.io/badge/Flask-2.3.3-green.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/Vue.js-3.3.4-brightgreen.svg" alt="Vue Version">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/Docker-Ready-blue.svg" alt="Docker Ready">
</div>

## 🌾 Overview

HonestyBox is a modern micro-SaaS platform designed to connect local farmers directly with consumers, eliminating middlemen and fostering community-supported agriculture. The platform enables farmers to list their fresh produce online, manage inventory in real-time, and build trust through verified profiles, while customers can discover local farms on an interactive map and access fresh, locally-sourced products.

### 🎯 Mission

Our mission is to strengthen local food systems by making farm-gate sales accessible, transparent, and efficient for both farmers and consumers. We believe in supporting sustainable agriculture and building stronger connections between those who grow our food and those who consume it.

## ✨ Key Features

### For Farmers 👨‍🌾
- **Easy Registration**: Simple onboarding process with farm location setup using latitude/longitude
- **Product Management**: Full CRUD operations for managing farm products with inline editing
- **Inventory Control**: Real-time inventory tracking with availability status
- **Dashboard Analytics**: Overview of products, availability status, and farm information
- **Mobile-Responsive**: Manage your farm from any device

### For Customers 🛒
- **Interactive Farm Map**: Discover local farms using an interactive Leaflet.js map
- **Product Browse**: View available products from each farm with pricing and availability
- **Farm Details**: Access farmer contact information and farm locations
- **Fresh Produce**: Direct access to locally-sourced, fresh products

### For Administrators 👤
- **Farmer Verification**: Approve or reject farmer registrations to maintain platform quality
- **User Management**: Overview of all registered farmers and their approval status
- **Platform Control**: Ensure only verified farmers can list products

## 🛠️ Technology Stack

### Backend
- **Framework**: Flask 2.3.3 (Python)
- **Database**: SQLAlchemy with SQLite (easily upgradeable to PostgreSQL)
- **Authentication**: JWT (JSON Web Tokens) with Flask-JWT-Extended
- **API**: RESTful API architecture
- **Security**: Password hashing with Werkzeug

### Frontend
- **Framework**: Vue 3.3.4 with Composition API
- **Build Tool**: Vite for fast development and optimized builds
- **State Management**: Pinia for reactive state management
- **Routing**: Vue Router with authentication guards
- **HTTP Client**: Axios for API communication
- **Maps**: Leaflet.js for interactive mapping
- **Styling**: Custom CSS with responsive design

### DevOps
- **Containerization**: Docker with multi-stage builds
- **Orchestration**: Docker Compose for local development
- **Web Server**: Nginx for frontend serving
- **API Gateway**: Nginx reverse proxy for backend

## 📋 Prerequisites

- **Docker & Docker Compose** (Recommended)
  - Docker Engine 20.10+
  - Docker Compose 1.29+

OR

- **Manual Installation**
  - Python 3.9+
  - Node.js 16+ and npm 7+
  - Git

## 🚀 Quick Start

### Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/jgalan247/farmersbox.git
   cd farmersbox
   ```

2. **Start the application**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5000/api

### Manual Installation

#### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the backend**
   ```bash
   python run.py
   ```

#### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env if needed
   ```

4. **Run the development server**
   ```bash
   npm run dev
   ```

## 👤 Default Credentials

### Super Admin Account
- **Email**: admin@honestybox.com
- **Password**: admin123

> ⚠️ **Important**: Change these credentials immediately in production!

## 📁 Project Structure

```
honestybox/
├── backend/                 # Flask backend application
│   ├── app/                # Application package
│   │   ├── __init__.py    # App factory
│   │   ├── models.py      # Database models
│   │   ├── config.py      # Configuration
│   │   ├── routes/        # API endpoints
│   │   │   ├── auth.py    # Authentication routes
│   │   │   ├── farmers.py # Farmer management
│   │   │   ├── products.py# Product CRUD
│   │   │   ├── admin.py   # Admin functions
│   │   │   └── public.py  # Public API
│   │   └── utils/         # Utility functions
│   │       └── auth.py    # Auth decorators
│   ├── requirements.txt   # Python dependencies
│   ├── run.py            # Application entry point
│   └── Dockerfile        # Backend container
├── frontend/             # Vue.js frontend
│   ├── src/             
│   │   ├── components/   # Reusable components
│   │   ├── views/       # Page components
│   │   ├── stores/      # Pinia state stores
│   │   ├── router/      # Vue Router config
│   │   ├── services/    # API services
│   │   └── assets/      # Static assets
│   ├── package.json     # Node dependencies
│   ├── vite.config.js   # Vite configuration
│   └── Dockerfile       # Frontend container
├── docker-compose.yml   # Container orchestration
└── README.md           # This file
```

## 🔧 Configuration

### Backend Configuration (.env)

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
DATABASE_URL=sqlite:///honestybox.db
```

### Frontend Configuration (.env)

```env
VITE_API_URL=http://localhost:5000/api
```

## 📱 Usage Guide

### For Farmers

1. **Register Your Farm**
   - Click "Register Farm" on the homepage
   - Fill in your farm details including name and location coordinates
   - Submit and wait for admin approval

2. **Manage Products** (After Approval)
   - Login with your credentials
   - Navigate to "Products" section
   - Add new products with name, price, unit, and quantity
   - Edit products inline by clicking the Edit button
   - Toggle availability status as needed

3. **Update Farm Information**
   - Access your dashboard
   - Update contact information and location as needed

### For Customers

1. **Browse Farms**
   - Visit the Farm Map page
   - Click on farm markers to view details
   - Click "View Products" to see available items

2. **View Products**
   - Browse available products from each farm
   - View pricing and availability
   - Contact farmers directly for purchases

### For Administrators

1. **Login**
   - Use the admin credentials to access the admin panel

2. **Manage Farmers**
   - Review pending farmer registrations
   - Approve legitimate farmers
   - Reject inappropriate registrations

3. **Monitor Platform**
   - View all registered farmers
   - Check approval status
   - Maintain platform quality

## 🛡️ Security Features

- **Password Hashing**: Secure password storage using Werkzeug
- **JWT Authentication**: Stateless authentication with token expiry
- **Role-Based Access**: Separate permissions for farmers and admins
- **CORS Configuration**: Controlled cross-origin resource sharing
- **SQL Injection Protection**: Parameterized queries via SQLAlchemy
- **Input Validation**: Server-side validation for all inputs

## 🧪 Testing

### Running Backend Tests
```bash
cd backend
python -m pytest tests/
```

### Running Frontend Tests
```bash
cd frontend
npm run test
```

## 🚢 Deployment

### Production Considerations

1. **Database**: Migrate from SQLite to PostgreSQL
2. **Security**: 
   - Use environment-specific secrets
   - Enable HTTPS
   - Set up proper CORS origins
3. **Performance**:
   - Add Redis for caching
   - Implement CDN for static assets
   - Use production builds

### Docker Production Build

```bash
docker-compose -f docker-compose.prod.yml up --build
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Use ESLint configuration for JavaScript
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

## 📄 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register` | Register new farmer |
| POST | `/api/auth/login` | User login |
| GET | `/api/auth/me` | Get current user |

### Farmer Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/farmers/profile` | Get farmer profile |
| PUT | `/api/farmers/profile` | Update farmer profile |

### Product Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products/` | List farmer's products |
| POST | `/api/products/` | Create new product |
| PUT | `/api/products/:id` | Update product |
| DELETE | `/api/products/:id` | Delete product |

### Public Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/public/farms` | List all approved farms |
| GET | `/api/public/farms/:id/products` | Get farm's products |

### Admin Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/admin/farmers/pending` | List pending farmers |
| POST | `/api/admin/farmers/:id/approve` | Approve farmer |
| POST | `/api/admin/farmers/:id/reject` | Reject farmer |
| GET | `/api/admin/farmers` | List all farmers |

## 🐛 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Change ports in docker-compose.yml or use different ports
   PORT=3001 npm run dev  # Frontend
   ```

2. **Database Migrations**
   ```bash
   # Reset database
   rm backend/instance/honestybox.db
   python backend/run.py
   ```

3. **Docker Build Failures**
   ```bash
   # Clean Docker cache
   docker system prune -a
   docker-compose build --no-cache
   ```

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/jgalan247/farmersbox/issues)
- **Discussions**: [GitHub Discussions](https://github.com/jgalan247/farmersbox/discussions)
- **Email**: support@honestybox.com

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape HonestyBox
- Inspired by the local farming communities and sustainable agriculture movement
- Built with open-source technologies and community support

## 🔮 Future Enhancements

- [ ] Payment integration for online transactions
- [ ] Mobile applications (iOS/Android)
- [ ] Advanced analytics for farmers
- [ ] Customer accounts and order history
- [ ] Delivery scheduling system
- [ ] Review and rating system
- [ ] Multi-language support
- [ ] SMS notifications for farmers
- [ ] Seasonal produce calendars
- [ ] Farm certification badges

---

<div align="center">
  Made with ❤️ for local farmers and sustainable agriculture
</div>
