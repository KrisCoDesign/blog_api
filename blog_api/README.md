# Blog API Platform

A robust RESTful API for a modern blog application built with Django and Django REST Framework. This platform facilitates user engagement through blog posting, commenting, and real-time news integration.

## 🚀 Features

- **Automated Content Integration**: Seamless integration with The News API for global news aggregation
- **User-Generated Content**: Complete CRUD operations for blog posts and comments
- **User Authentication**: JWT-based authentication with registration, login, and profile management
- **Content Categorization**: Organized content management with category system
- **Admin Dashboard**: Comprehensive administrative tools for content and user management
- **RESTful Architecture**: Clean, standardized API endpoints following REST principles

## 📋 API Endpoints
The ModelViewSet works hand‑in‑hand with routers to generate standard CRUD URLs automatically.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/posts/` | GET, POST | List and create blog posts |
| `/api/posts/<pk>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete specific post |
| `/api/comments/` | GET, POST | List and create comments |
| `/api/comments/<pk>/` | GET, PUT, PATCH, DELETE | Manage specific comments |
| `/api/category/` | GET, POST | List and create categories |
| `/api/category/<pk>/` | GET, PUT, PATCH, DELETE | Manage specific categories |
| `/api/externalnews/` | GET | Fetch curated news from external API |
| `/api/profile/` | GET, PUT, PATCH | User profile management |
| `/api/register/` | POST | User registration |
| `/api/login/` | POST | User authentication |
| `/api/logout/` | POST | User logout |

## 🛠️ Technology Stack

- **Backend Framework**: Django 3.2+
- **API Framework**: Django REST Framework 3.12+
- **Database**: SQLite (Development), PostgreSQL (Production-ready)
- **Authentication**: Token Authentication
- **Python Version**: 3.8+

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/blog-api-platform.git
   cd blog-api-platform
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

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
NEWS_API_KEY=your-newsapi-key
```

### External API Integration

The platform integrates with [The News API](https://www.thenewsapi.com/) for real-time news content. Obtain an API key and configure it in your environment variables.

## 🎯 Usage

### Authentication

```bash
# Register new user
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "user", "password": "pass", "email": "user@example.com"}'

# Login
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "user", "password": "pass"}'

# Use token in subsequent requests
curl -H "Authorization: Token <your-token>" http://localhost:8000/api/posts/
```

### Creating a Post

```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Token <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"title": "My First Post", "content": "Post content", "category": 1}'
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

