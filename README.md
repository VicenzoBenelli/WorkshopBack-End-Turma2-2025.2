# 📚 Workshop Back-End Turma 2 - 2025.2

Este repositório contém os exercícios e desafios desenvolvidos durante o **Workshop de Back-End**, abordando desde conceitos básicos de Python até a criação de APIs REST com Django e Django REST Framework.

---

## 🚀 Visão Geral

O projeto é dividido em **módulos diários (DIA 1 a DIA 6)**, cada um com um conjunto de tarefas e desafios práticos.  
O objetivo é evoluir gradualmente do ambiente de desenvolvimento local até a implementação de aplicações web completas e APIs.

---

## 🛠️ Como Executar

### Pré-requisitos
- Python 3.x instalado
- Virtualenv (recomendado)
- Banco de dados configurado (ex: SQLite, PostgreSQL)

### 1. Criar e Ativar Ambiente Virtual
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # macOS/Linux
```

### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com as configurações necessárias (ex: chaves secretas, credenciais do banco).

### 4. Executar Migrações
Antes de rodar o servidor, é necessário criar as tabelas no banco de dados:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Rodar Servidor
Após instalar as dependências e executar as migrações, inicie o servidor local:
```bash
python manage.py runserver
```
Acesse: http://localhost:8000

---

## 📅 Conteúdo por Dia

### **DIA 1 – Configuração do Ambiente e Git**
- **Objetivo:** Preparar o ambiente Python e configurar o Git.
- **Arquivos principais:**
  - `Main.py` → Arquivo inicial do projeto.
  - `.gitignore` → Lista de arquivos/pastas a serem ignorados pelo Git (ex.: `venv`).
- **Tarefas:**
  - Criar ambiente virtual (`venv`).
  - Configurar Git (`user.name` e `user.email`).
  - Subir projeto no GitHub com o nome **WorkshopBack-End-Turma2-2025.2**.
- **Aplicação:** Apenas configuração inicial, sem lógica de negócio.

---

### **DIA 2 – Funções, Classes e Polimorfismo**
- **Objetivo:** Praticar funções, retorno de valores, classes, herança e polimorfismo.
- **Desafios:**
  1. **Raiz Quadrada Simples** → Uso de `math.sqrt()`.
  2. **Arredondamento Inteligente** → Uso de `math.floor()`, `math.ceil()` e `round()`.
  3. **Calculadora Geométrica Avançada** → Classe `FiguraGeometrica` com métodos para área de círculo, área de triângulo e hipotenusa.
  4. **Animais Simples** → Classe `Animal` e subclasses `Gato` e `Cachorro` com polimorfismo.
  5. **Animais com Atributos** → Inclusão de `nome` e `idade` com `super().__init__()`.
  6. **Zoológico Inteligente** → Classe `Zoologico` com métodos para adicionar, listar e filtrar animais.

---

### **DIA 3 – Depuração de Código**
- **Objetivo:** Treinar resolução de problemas e debugging.
- **Aplicação:** Exercícios de análise e correção de código.

---

### **DIA 4 – Consulta de CEP com Django**
- **Objetivo:** Criar aplicação Django que consulta a API ViaCEP e salva no banco.
- **Arquivos principais:**
  - `models.py` → Modelo `Endereco` com campos `rua`, `bairro`, `cidade`, `estado`, `cep`.
  - `forms.py` → Formulário para entrada de CEP.
  - `views.py` → Funções `home` e `consulta_cep`.
  - `urls.py` (app e projeto) → Rotas para as views.
  - Templates:
    - `home.html` → Formulário de entrada.
    - `consulta_cep.html` → Exibição dos dados retornados.
- **Aplicação:** Recebe CEP, consulta API ViaCEP, salva no banco e exibe resultado.

---

### **DIA 5 – CRUD com Django Class-Based Views**
- **Objetivo:** Criar CRUD para CEP usando `FormView`, `ListView`, `DeleteView` e `DetailView`.
- **Arquivos principais:**
  - `models.py` → Modelo de CEP.
  - `forms.py` → Formulário de CEP.
  - `views.py` → Classes baseadas em view para CRUD.
  - `urls.py` → Rotas usando `.as_view()`.
  - Templates → Um para cada funcionalidade, herdando de `base.html`.
- **Aplicação:** Permite cadastrar, listar, visualizar e excluir registros de CEP.

---

### **DIA 6 – API REST com Django REST Framework**
- **Objetivo:** Criar API REST que consome uma API pública.
- **Arquivos principais:**
  - `models.py` → Modelo da API.
  - `serializers.py` → Serializador `ModelSerializer`.
  - `viewsets.py` → `ModelViewSet` para CRUD via API.
  - `urls.py` (projeto) → Registro de rotas com `DefaultRouter`.
- **Aplicação:** API REST completa, integrando dados externos e expondo endpoints.

---

## 📂 Estrutura Lógica dos Arquivos

```
projeto/
├── main.py               # Script inicial do projeto (DIA 1)
├── models.py             # Modelos de dados para Django
├── forms.py              # Formulários para entrada de dados
├── views.py              # Lógica de controle (funções e classes)
├── urls.py               # Rotas da aplicação
├── serializers.py        # Conversão de modelos para JSON (API REST)
└── templates/            # Interface para interação com usuário
    ├── base.html
    └── ...
```

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Django**
- **Django REST Framework**
- **Requests**
- **Biblioteca Math (Python)**

---

## 👨‍💻 Desenvolvimento
Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---


