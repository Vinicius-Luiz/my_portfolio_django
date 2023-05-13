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