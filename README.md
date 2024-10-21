
# 📝 Aplicação Web de Lista de Tarefas com Flask

Este projeto implementa uma aplicação web simples de lista de tarefas utilizando o framework Flask, onde o usuário pode adicionar e remover tarefas de uma lista. A interface é construída com HTML e estilizada utilizando o Bootstrap, proporcionando uma experiência de usuário agradável e responsiva.

## 🚀 Funcionalidades

- **Adicionar Tarefas**: Permite ao usuário inserir uma nova tarefa na lista através de um formulário simples.
- **Excluir Tarefas**: O usuário pode remover uma tarefa da lista ao clicar no botão de "Excluir" ao lado de cada item.
- **Listagem Dinâmica**: As tarefas adicionadas aparecem automaticamente na página inicial, utilizando renderização dinâmica com Jinja2.

## 🛠️ Tecnologias Utilizadas

- **Flask**: Framework web em Python utilizado para criar a lógica da aplicação.
- **HTML/CSS**: Estrutura e estilo da interface do usuário.
- **Bootstrap**: Framework CSS para tornar a interface mais moderna e responsiva.
- **Jinja2**: Motor de template do Flask para renderizar dinamicamente as tarefas na página HTML.

## 📁 Estrutura de Diretórios

```
.
├── app.py              # Código principal do Flask
├── templates
│   └── index.html      # Página HTML principal
└── static
    └── (Bootstrap e outros recursos estáticos)
```

## 🔧 Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Instale as dependências**:
   Certifique-se de que você tem o Python instalado em sua máquina. Em seguida, instale o Flask:
   ```bash
   pip install flask
   ```

3. **Execute o servidor**:
   Inicie o servidor Flask para rodar a aplicação:
   ```bash
   python app.py
   ```

4. **Acesse a aplicação**:
   No navegador, vá até `http://127.0.0.1:5000/` para visualizar a lista de tarefas.

## 📋 Arquivos Principais

- **app.py**: Contém as rotas e a lógica da aplicação em Flask.
- **index.html**: Página principal da aplicação, onde as tarefas são listadas e adicionadas.
  
## ✍️ Autor

**Prof. Sauer**
- Website: [www.sauer.pro.br](http://www.sauer.pro.br)
- Email: sauer@simplificatreinamentos.com.br
- [Instagram](https://www.instagram.com/prof.alesauer/)
- [Facebook](https://www.facebook.com/prof.alesauer)
- [YouTube](https://www.youtube.com/@prof.alesauer)
- [LinkedIn](https://www.linkedin.com/in/alesauer)
