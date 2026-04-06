# 📞 Google Maps Phone Scraper

Automação para extração de telefones comerciais diretamente do Google Maps. O script lê uma planilha Excel com nomes de empresas, pesquisa cada uma no Maps e extrai o número de telefone automaticamente, exportando os resultados em uma nova planilha.

---

##  Como funciona

1. O script lê o arquivo `empresas.xlsx` contendo uma coluna chamada **Empresa**
2. Para cada empresa, abre o Google Maps e realiza a busca pelo nome
3. Tenta extrair o telefone diretamente da listagem de resultados (via elemento da página)
4. Caso não encontre, tenta clicar no botão "Copiar número de telefone" como fallback
5. Salva todos os resultados em `empresas_com_telefone.xlsx`

---

##  Pré-requisitos

- **Python 3.8+**
- **Google Chrome** instalado
- **ChromeDriver** compatível com a versão do seu Chrome

---

##  Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/google-maps-phone-scraper.git
cd google-maps-phone-scraper
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install selenium pandas openpyxl pyperclip
```

### 3. Configure o ChromeDriver

O Selenium precisa do ChromeDriver para controlar o navegador. A partir do Selenium 4.6+, o **Selenium Manager** já baixa o driver automaticamente. Caso esteja usando uma versão anterior, baixe manualmente em [chromedriver.chromium.org](https://chromedriver.chromium.org/) e adicione ao PATH do sistema.

---

##  Estrutura do projeto

```
google-maps-phone-scraper/
├── main.py                     # Script principal
├── empresas.xlsx               # Planilha de entrada (você cria)
├── empresas_com_telefone.xlsx  # Planilha de saída (gerada automaticamente)
├── requirements.txt            # Dependências do projeto
```

---

## 📊 Formato da planilha de entrada

O arquivo `empresas.xlsx` deve conter uma coluna chamada **Empresa** com os nomes das empresas:

| Empresa |
|---------|
| SUSTENTA ALIMENTOS LTDA |
| VALE GRANDE INDUSTRIA E COMERCIO DE ALIMENTOS S/A |
| NUTRIX ALIMENTOS |

---

##  Como usar

1. Crie ou edite o arquivo `empresas.xlsx` com os nomes das empresas
2. Execute o script:

```bash
python main.py
```

3. Aguarde o processo — o navegador abrirá e fará as buscas automaticamente
4. Ao finalizar, o arquivo `empresas_com_telefone.xlsx` será gerado com os telefones encontrados

---

##  Como funciona internamente

O script utiliza duas estratégias para encontrar o telefone:

**Estratégia 1 — Extração direta da listagem:**
Quando o Google Maps retorna resultados, o telefone já aparece visível na lista. O script localiza o elemento `span.Usd1K` que contém o número e extrai o texto diretamente — sem precisar clicar em nada.

**Estratégia 2 — Fallback via botão de copiar:**
Caso o telefone não esteja visível na listagem (quando a busca redireciona direto para o perfil da empresa, por exemplo), o script procura pelo botão "Copiar número de telefone" (`aria-label='Copiar número de telefone'`), clica nele e lê o conteúdo da área de transferência.

---

## ⚠️ Observações importantes

- O Google Maps pode alterar a estrutura HTML a qualquer momento, o que pode quebrar os seletores utilizados. Caso isso aconteça, inspecione a página e atualize os seletores no código.
- Evite executar o script em alta frequência para não ser bloqueado pelo Google.
- O script depende do `pyperclip` para a estratégia de fallback, que por sua vez depende de ferramentas de clipboard do sistema (`xclip`/`xsel` no Linux, `pbcopy` no macOS, nativo no Windows).
- Algumas empresas podem não ter telefone cadastrado no Google Maps — nesses casos, o campo ficará vazio na planilha de saída.

---

##  Dependências

| Pacote | Função |
|--------|--------|
| `selenium` | Automação do navegador Chrome |
| `pandas` | Leitura e escrita de planilhas Excel |
| `openpyxl` | Engine para manipulação de arquivos `.xlsx` |
| `pyperclip` | Acesso à área de transferência do sistema |

---

##  requirements.txt

```
selenium
pandas
openpyxl
pyperclip
```

---



