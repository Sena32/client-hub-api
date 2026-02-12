# Regras do módulo Users (Auth)

Este módulo contém a API de **autenticação**: login, registro, refresh e verificação de token JWT (rotas `/token/`, `/register/`, `/token/refresh`, `/token/verify`).

## Regras obrigatórias

1. **Documentação Swagger (OpenAPI)**  
   Todas as views deste módulo **devem** ter documentação via `drf-spectacular`:
   - Use `@extend_schema` em todas as views (incluindo as que envolvem `TokenRefreshView` e `TokenVerifyView`).
   - Sempre informe `tags=['Auth']` para que os endpoints apareçam no grupo "Auth" na documentação.
   - Inclua `summary` (e opcionalmente `description`) para cada operação.

2. **Desacoplamento**  
   - A documentação do módulo fica no próprio módulo (decorators nas views), não em um arquivo central único.
   - Novos endpoints de auth devem ser documentados aqui, mantendo a tag `Auth`.

3. **Serializers**  
   - Mantenha os serializers de token e registro alinhados com o que a API expõe; eles definem o schema na documentação.

4. **Permissões**  
   - Endpoints públicos (login, registro, refresh, verify) devem usar `AllowAny` de forma explícita onde aplicável.

## Estrutura esperada

- `api/viewsets.py`: views com `@extend_schema` e `tags=['Auth']`.
- `api/serializers.py`: serializers de token e registro.

## Referência

- Documentação da API: `/api/docs/` (Swagger UI) e `/api/redoc/` (ReDoc).
- Schema bruto: `/api/schema/`.
