# SecurePass: Gerador de Senhas em Python

O **SecurePass** é um gerador de senhas desenvolvido em Python, com interface interativa construída utilizando Streamlit.

O projeto tem como objetivo permitir a criação de senhas aleatórias e personalizadas, oferecendo diferentes opções de caracteres, tamanhos e quantidades, além de uma avaliação simplificada da força das senhas geradas.

## Funcionalidades

- Geração de senhas utilizando a biblioteca `secrets` do Python.
- Personalização dos caracteres utilizados:
  - Números (0–9).
  - Letras minúsculas (a–z).
  - Letras maiúsculas (A–Z).
  - Símbolos especiais.
- Escolha do comprimento da senha entre 8 e 64 caracteres.
- Geração de 1 a 10 senhas por vez.
- Garantia de pelo menos um caractere de cada categoria selecionada.
- Avaliação simplificada da força das senhas, com pontuação de até 100 pontos.
- Interface interativa desenvolvida com Streamlit.
- Testes automatizados utilizando pytest.

## Tecnologias utilizadas

- **Python:** linguagem principal do projeto.
- **Streamlit:** desenvolvimento da interface.
- **secrets:** geração de caracteres aleatórios apropriada para uso criptográfico.
- **string:** conjuntos de caracteres utilizados na geração e avaliação.
- **pytest:** testes automatizados das funcionalidades.

## Estrutura do projeto

```text
SecurePass/
├── screenshots/
│   ├── 
│   ├── main.py
│   └── security.py
├── src/
│   ├── generator.py
│   ├── main.py
│   └── security.py
├── test/
│   ├── test_generator.py
│   └── test_security.py
├── README.md
├── requirements.txt
└── .gitignore
```

### Organização do código

- `main.py`: interface e interação com o usuário.
- `generator.py`: lógica de geração das senhas.
- `security.py`: cálculo da pontuação das senhas.
- `test_generator.py`: testes da geração de senhas.
- `test_security.py`: testes da avaliação de segurança.

## Como executar

### 1. Pré-requisitos

Tenha o Python e o pip instalados em seu computador.

### 2. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
cd SecurePass
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Inicie a aplicação

```bash
python -m streamlit run src/main.py
```

O Streamlit disponibilizará um endereço local para acessar a interface no navegador.

## Testes automatizados

O projeto utiliza pytest para verificar o funcionamento das principais funções.

Para executar todos os testes:

```bash
python -m pytest -v
```

Os testes verificam:

- Comprimento das senhas geradas.
- Presença das categorias de caracteres selecionadas.
- Comportamento diante de entradas inválidas.
- Cálculo da pontuação de segurança.
- Funcionamento das regras de avaliação.

## Avaliação de segurança

O SecurePass utiliza uma pontuação simplificada baseada no comprimento da senha e na presença de diferentes categorias de caracteres.

As classificações apresentadas são:

| Pontuação | Classificação |
|---|---|
| 0–24 | Fraca |
| 25–49 | Regular |
| 50–74 | Boa |
| 75–100 | Forte |

**Observação:** essa pontuação é uma avaliação didática e não representa uma medição criptográfica completa da resistência de uma senha.

## Possíveis melhorias futuras

- Implementação de estimativa de entropia.
- Verificação de senhas comuns ou comprometidas.
- Melhorias na interface e experiência do usuário.
- Ampliação da cobertura dos testes automatizados.
- Disponibilização da aplicação online.

## Objetivo do projeto

O SecurePass foi desenvolvido como um projeto de aprendizado e portfólio, com foco na aplicação prática de conceitos de programação Python, modularização de código, tratamento de erros, desenvolvimento de interfaces e testes automatizados.
