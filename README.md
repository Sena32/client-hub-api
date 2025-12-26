<div align="center">
  Client Hub API

RESTful API built with **Django** and **Django REST Framework**, designed for learning and experimentation purposes.  
It provides authentication and client management endpoints that integrate with the **Client Hub** frontend application.

[![Status](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)]()
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Django](https://img.shields.io/badge/Django-4.0+-092E20?style=for-the-badge&logo=django)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-336791?style=for-the-badge&logo=postgresql&logoColor=white)]()
[![GitHub](https://img.shields.io/badge/GitHub-Ailton_Sena-000?style=for-the-badge&logo=github)](https://github.com/Sena32)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ailton_Sena-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/ailtonsenap/)

</div>

---
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

Configure suas credenciais PostgreSQL através do arquivo `.env` (baseado no `.env.sample`):

```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=db
DB_USER=postgres
DB_PASSWORD=root
DB_HOST=127.0.0.1
DB_PORT=5432
```

---

## 🐳 Executando com Docker Compose

### Pré-requisitos

- Docker instalado
- Docker Compose instalado

### Configuração Inicial

1. **Clone o repositório:**
   ```bash
   git clone <repository-url>
   cd client-hub-api
   ```

2. **Configure as variáveis de ambiente:**
   ```bash
   cp .env.sample .env
   ```
   
   Edite o arquivo `.env` com suas configurações:
   ```bash
   nano .env  # ou use seu editor preferido
   ```

3. **Execute com Docker Compose:**
   ```bash
   # Desenvolvimento
   docker-compose up -d
   
   # Ou para ver os logs em tempo real
   docker-compose up
   ```

4. **Execute as migrações (se necessário):**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Crie um superusuário (opcional):**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

### Comandos Úteis

```bash
# Parar os containers
docker-compose down

# Parar e remover volumes (⚠️ apaga dados do banco)
docker-compose down -v

# Ver logs
docker-compose logs -f web
docker-compose logs -f db

# Executar comandos Django
docker-compose exec web python manage.py <comando>

# Reconstruir as imagens
docker-compose build --no-cache

# Acessar o shell do container
docker-compose exec web sh
```

### Acessar a Aplicação

- **API:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin
- **PostgreSQL:** localhost:5432

### Produção

Para executar em produção, use o arquivo `docker-compose.prod.yml`:

```bash
# Configure o arquivo .env.production primeiro
cp .env.sample .env.production
# Edite .env.production com valores de produção

# Execute em produção
docker-compose -f docker-compose.prod.yml up -d
```

**⚠️ Importante para Produção:**
- Gere uma nova `SECRET_KEY` segura
- Configure `DEBUG=False`
- Configure `ALLOWED_HOSTS` com seu domínio
- Configure `CORS_ALLOWED_ORIGINS` adequadamente
- Use senhas fortes para o banco de dados
- Configure backups regulares do PostgreSQL

<br />
<div align="center">
  <small>Developed by Ailton de Sena Pinheiro - 09/2021</small>

  [![GitHub Badge](https://img.shields.io/badge/Ailton_Sena-000?style=for-the-badge&logo=github&logoColor=white&link=https://www.linkedin.com/in/ailtonsenap)](https://github.com/Sena32/)
    [![Linkedin Badge](https://img.shields.io/badge/Ailton_Sena-000?style=for-the-badge&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/ailtonsenap)](https://www.linkedin.com/in/ailtonsenap/) 
</div>
