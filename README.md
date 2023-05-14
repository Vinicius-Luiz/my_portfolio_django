# Meu Portfólio desenvolvido em Django

Url: **em breve**

## Preparação

### Ambiente virtual

**Criar ambiente virtual**
```bash
python -m venv .
```

**Criar arquivos para armazenar as variáveis de ambiente**
```bash
type nul > ".env"
```

### Projeto Django
**Criar projeto Django**
```bash
pip install django
```

```bash
rem comando para criar um projeto
django-admin startproject setup .
```

**Alterar interpretador do python**
`ctrl + shift + p` no vscode mostra as configurações para alterar o interpretador

**Alterar Timezone**
- Alterar `LANGUAGE_CODE` para `pt-br`
- Alterar `TIME_ZONE` para `America/Sao Paulo`

### Configurar Git e GitHub
```bash
pip install python-dotenv
```

```bash
rem comando para criar o .gitignore
type nul > ".gitignore"
```

Utilize o gitignore.io para gerar um template padrão para o Django.

```bash
rem comando para subir os arquivos para o GitHub
git init
git add .
git commit -m "First Commit"
git remote add origin https://github.com/Vinicius-Luiz/my_portfolio_django
git push origin master
```

### Criar app Portfolio

```bash
rem comando para criar novo app
python manage.py startapp portfolio
```

- Alterar `name = 'apps.portfolio'` em **apps.py**<br>

- Adicionar `'apps.portfolio.apps.PortfolioConfig'` em `INSTALLED_APPS`<br>

### Preparar Urls, Views e Templates

- Em **views.py**
```python
# Criando uma rota para carregar a página principal
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

- Em **urls.py** do app
```python
# Criar variável que contém todas as rotas do app
from django.urls import path
from apps.portfolio.views import index

urlpatterns = [
    path('', index)
]
```

- Em **urls.py** do setup
```python
# Isolando as urls do apps
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.portfolio.urls')),
]
```

- Em **templates**<br>
Criar a pasta `templates` e adicionar `[path.join(BASE_DIR, 'templates')] `em `TEMPLATES['DIRS']`

### Configurar arquivos estáticos

- Em **settings.py**
```python
# Configurar arquivos estáticos
STATIC_URL = 'static/'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'setup\static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

`python manage.py collectstatic` para coletar todos os arquivos estáticos

## Django Admin

```bash
rem comando para criar um superusuário
python manage.py createsuperuser vlsf2
```

## Configurando Imagens
```python
# A pasta "media" é criada na raiz do projeto Django e é usada para armazenar os arquivos de mídia enviados pelos usuários.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# O Django irá procurar os arquivos de mídia na pasta definida em MEDIA_ROOT usando a URL http://example.com/media/.
MEDIA_URL = "/media/"
```

- Em **urls.py** de setup
```python
# Isso indicará ao Django que ele precisa usar as referências que inserimos em settings.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.portfolio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```