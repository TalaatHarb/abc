FROM python:3.12-slim AS build

WORKDIR /site
COPY requirements-docs.txt ./
RUN python -m pip install --no-cache-dir -r requirements-docs.txt
COPY mkdocs.yml site_hooks.py README.md Research-project-plan.md ./
COPY guide/ ./guide/
COPY docs/javascripts/mathjax.js ./docs/javascripts/mathjax.js
RUN python -m mkdocs build --strict

FROM nginxinc/nginx-unprivileged:stable-alpine
COPY --from=build /site/site/ /usr/share/nginx/html/
EXPOSE 8080
