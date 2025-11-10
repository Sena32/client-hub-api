<h1 align="center">
  Client Hub API
</h1>

### 🧠 **Sobre o projeto**

**API RESTful desenvolvida com Django e Django REST Framework**, criada para fins de aprendizado e desafio.
Esta API fornece endpoints de autenticação e gerenciamento de clientes que se integram diretamente com o frontend do **Client Hub**.

---

## ⚙️ Endpoints Overview

| Method | Endpoint           | Description |
|---------|--------------------|-------------|
| `POST`  | `/token/`          | Obtain JWT access and refresh tokens |
| `POST`  | `/token/refresh`   | Refresh JWT token |
| `POST`  | `/token/verify`    | Verify JWT token validity |
| `POST`  | `/register/`       | Register a new user |
| `GET`   | `/clients/`        | List all clients |
| `POST`  | `/clients/`        | Create a new client |
| `GET`   | `/clients/{id}/`   | Retrieve a specific client |
| `PUT`   | `/clients/{id}/`   | Update client information |
| `DELETE`| `/clients/{id}/`   | Delete a client |

---

## :hammer_and_wrench: Features 

- [x] JWT Authentication (access, refresh, verify)
- [x] User registration
- [x] CRUD operations for clients
- [x] Django Admin Panel
- [x] Token-based security
- [x] CORS enabled for frontend integration

---

## ✨ Technologies

- [x] Django
- [x] Django REST Framework
- [x] Django REST Framework SimpleJWT
- [x] PostgreSQL
- [x] Django CORS Headers

---

## 🛠️ Database Configuration

configure suas credentials PostgreSQL em `settings.py` ou via environment variables:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
<br />
<div align="center">
  <small>Developed by Ailton de Sena Pinheiro - 09/2021</small>

  [![GitHub Badge](https://img.shields.io/badge/Ailton_Sena-000?style=for-the-badge&logo=github&logoColor=white&link=https://www.linkedin.com/in/ailtonsenap)](https://github.com/Sena32/)
    [![Linkedin Badge](https://img.shields.io/badge/Ailton_Sena-000?style=for-the-badge&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/ailtonsenap)](https://www.linkedin.com/in/ailtonsenap/) 
</div>
