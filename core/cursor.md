# Regras do módulo Core

Este módulo contém a API de **clientes** e **endereços** (rotas sob `/clients/`).

## Regras obrigatórias

1. **Documentação Swagger (OpenAPI)**  
   Todas as views e viewsets deste módulo **devem** ter documentação via `drf-spectacular`:
   - Use `@extend_schema` ou `@extend_schema_view` em todas as views/viewsets.
   - Sempre informe `tags=['Clients']` para que os endpoints apareçam no grupo correto na documentação.
   - Inclua `summary` (e opcionalmente `description`) para cada operação.

2. **Desacoplamento**  
   - A documentação do módulo fica no próprio módulo (decorators nas views), não em um arquivo central único.
   - Novos endpoints deste módulo devem ser documentados aqui, mantendo a tag `Clients`.

3. **Serializers**  
   - Os serializers são a fonte do schema OpenAPI; mantenha campos e `Meta` consistentes com o que a API expõe.

4. **Permissões**  
   - Endpoints que exigem autenticação devem declarar `permission_classes` de forma explícita.

## Estrutura esperada

- `api/viewsets.py`: viewsets com `@extend_schema_view`/`@extend_schema` e `tags=['Clients']`.
- `api/serializers.py`: serializers usados pelos endpoints (e pelo schema).

## Referência

- Documentação da API: `/api/docs/` (Swagger UI) e `/api/redoc/` (ReDoc).
- Schema bruto: `/api/schema/`.
