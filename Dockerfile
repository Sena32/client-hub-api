# Use Alpine Linux LTS como imagem base
FROM python:3.11-alpine AS builder

# Instalar dependências de build necessárias
RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev \
    libffi-dev \
    && rm -rf /var/cache/apk/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar requirements e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Estágio final - imagem de produção otimizada
FROM python:3.11-alpine

# Instalar apenas runtime dependencies
RUN apk add --no-cache \
    postgresql-libs \
    && rm -rf /var/cache/apk/*

# Criar usuário não-root para segurança
RUN addgroup -g 1000 appuser && \
    adduser -D -u 1000 -G appuser appuser

# Definir diretório de trabalho
WORKDIR /app

# Copiar dependências instaladas do estágio builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copiar código da aplicação
COPY --chown=appuser:appuser . .

# Mudar para usuário não-root
USER appuser

# Expor porta
EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import socket; s = socket.socket(); s.connect(('localhost', 8000)); s.close()" || exit 1

# Comando padrão (pode ser sobrescrito no docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

