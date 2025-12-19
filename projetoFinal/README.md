# 🏥 Sistema de Saúde – CRUD com Django

Este projeto é um **sistema web de saúde** desenvolvido com o **framework Django**, com o objetivo de aplicar conceitos de **CRUD**, **autenticação**, **controle de acesso por perfil**, **priorização de atendimento** e **relatórios**, simulando um sistema real utilizado em unidades de saúde.

O sistema foi desenvolvido com fins **educacionais**, sendo ideal para disciplinas de **Desenvolvimento Web**, **Banco de Dados** e **Engenharia de Software**.

---

## 🎯 Objetivo do Sistema

Permitir o gerenciamento de pacientes em uma unidade de saúde, oferecendo:

* Cadastro, edição, listagem e exclusão de pacientes
* Controle de acesso por login
* Diferentes perfis de usuário (médico, enfermeiro, recepção)
* Confirmação de atendimento pelo médico
* Relatório de pacientes atendidos
* Dashboard com informações gerais

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**
* **Django 5+**
* **SQLite** (banco de dados padrão)
* **Bootstrap 5** (layout responsivo)
* **HTML5 / CSS3**

---

## 📁 Estrutura do Projeto

```
django_saude/
│
├── sistema_saude/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── saude/
│   ├── migrations/
│   ├── templates/
│   │   └── saude/
│   │       ├── base.html
│   │       ├── listar.html
│   │       ├── cadastrar.html
│   │       ├── editar.html
│   │       ├── dashboard.html
│   │       └── relatorio.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── templates/
│   └── registration/
│       └── login.html
│
├── manage.py
└── README.md
```

---

## 🔐 Controle de Acesso

O sistema utiliza o sistema de autenticação padrão do Django.

* Usuários **não autenticados** são redirecionados automaticamente para o login
* Cada funcionalidade respeita permissões do usuário

### 👥 Perfis de Usuário

* **Recepção**: cadastra e edita pacientes
* **Enfermeiro(a)**: visualiza pacientes e prioridades
* **Médico(a)**:

  * Confirma atendimento
  * Visualiza relatório de atendidos

---

## 🚦 Prioridade de Atendimento

Os pacientes possuem níveis de prioridade:

* 🟢 Baixa
* 🟡 Média
* 🟠 Alta
* 🔴 Urgente

As cores ajudam na **triagem visual** e organização do atendimento.

---

## 📊 Funcionalidades Principais

### ✔ CRUD de Pacientes

* Cadastrar paciente
* Editar paciente
* Excluir paciente
* Listar pacientes

### ✔ Confirmação de Atendimento

* Apenas médicos podem confirmar se um paciente foi atendido

### ✔ Relatório

* Lista todos os pacientes atendidos
* Ordenado por data e hora

### ✔ Dashboard

* Visão geral do sistema
* Quantidade de pacientes cadastrados
* Quantidade de atendimentos realizados

---

## ▶️ Como Executar o Projeto

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate
```

### 2️⃣ Instalar dependências

```bash
pip install django
```

### 3️⃣ Executar migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Criar superusuário

```bash
python manage.py createsuperuser
```

### 5️⃣ Rodar o servidor

```bash
python manage.py runserver
```

Acesse:

```
http://127.0.0.1:8000/
```

---

## 🧪 Testes Manuais Sugeridos

* Acessar o sistema sem login (verificar redirecionamento)
* Login com perfis diferentes
* Confirmar atendimento como médico
* Gerar relatório de atendimentos

## SENHAS DOS PERFIS

* ADMIN
    * login: everton
    * senha: everton12

* ENFERMEIRO – editar 
    * login: everton
    * senha: everton12

* RECEPÇÃO - cadastrar e listar
    * login: jose
    * senha: everton12

* MEDICO - TUDO
    * login: ricardo
    * senha:everton12

---

## 📚 Conceitos Aplicados

* MVC / MTV (Django)
* CRUD
* Autenticação e autorização
* Templates base e herança
* Boas práticas de organização de projeto

---

## 👨‍💻 Autor

**[Everton Espedito Silva Santos](https://www.linkedin.com/in/everton-espedito-3062071a3/)**

---

## 📌 Observação

Este projeto é de caráter **educacional**, podendo ser expandido com:

* Exportação de relatórios em PDF
* Gráficos estatísticos
* API REST
* Integração com IoT

---

🚀 *Projeto desenvolvido para fins acadêmicos e aprendizado prático com Dja
