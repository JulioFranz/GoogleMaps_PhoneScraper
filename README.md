<div align="center">

<br/>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=30&pause=1000&color=34A853&center=true&vCenter=true&width=600&lines=GoogleMaps+PhoneScraper;Search.+Extract.+Export." alt="Typing SVG" />
</a>

<br/>

<p>
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square"/>
</p>

</div>

<br/>

---

## `~/about`

```python
googlemaps_phone_scraper = {
    "type":    "Web Scraping · Automation",
    "stack":   ["Python", "Selenium", "Pandas", "OpenPyXL", "Pyperclip"],
    "input":   "empresas.xlsx  —  column: Empresa",
    "output":  "empresas_com_telefone.xlsx",
    "purpose": "Educational — extract business phone numbers from Google Maps",
    "author":  "JulioFranz · github.com/JulioFranz",
}
```

**GoogleMaps PhoneScraper** automates the extraction of business phone numbers directly from Google Maps. It reads a list of company names from an Excel spreadsheet, searches each one on Maps, extracts the phone number, and exports all results to a new spreadsheet.

```
GoogleMaps_PhoneScraper/
├── Google Maps Phone Scraper/
│   └── main.py                     # Main script
├── empresas.xlsx                   # Input spreadsheet (you create)
├── empresas_com_telefone.xlsx      # Output spreadsheet (auto-generated)
└── requirements.txt
```

---

## `~/how-it-works`

<table>
  <tr>
    <td valign="top" width="50%">
      <b>📋 Flow</b><br/><br/>
      <ol>
        <li>Reads <code>empresas.xlsx</code> — column <strong>Empresa</strong></li>
        <li>Opens Google Maps and searches each company</li>
        <li>Extracts phone number via one of two strategies</li>
        <li>Saves results to <code>empresas_com_telefone.xlsx</code></li>
      </ol>
    </td>
    <td valign="top" width="50%">
      <b>⚙️ Extraction Strategies</b><br/><br/>
      <ul>
        <li><strong>Strategy 1</strong> — Direct extraction from search results via <code>span.Usd1K</code></li>
        <li><strong>Strategy 2</strong> — Fallback: clicks "Copy phone number" button and reads clipboard via <code>pyperclip</code></li>
      </ul>
    </td>
  </tr>
</table>

---

## `~/getting-started`

### Input format

Create `empresas.xlsx` with a column named **Empresa**:

| Empresa |
|---|
| FACEBOOK |
| GOOGLE |
| GITHUB |

### Run

```bash
git clone https://github.com/JulioFranz/GoogleMaps_PhoneScraper.git
cd GoogleMaps_PhoneScraper

pip install -r requirements.txt

python main.py
```

> ChromeDriver is managed automatically by Selenium 4.6+. For older versions, download manually from [chromedriver.chromium.org](https://chromedriver.chromium.org/) and add to PATH.

---

## `~/stack`

<div align="center">

| Package | Purpose |
|---|---|
| ![Selenium](https://img.shields.io/badge/selenium-43B02A?style=flat-square&logo=selenium&logoColor=white) | Chrome browser automation |
| ![Pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white) | Read and write Excel spreadsheets |
| ![OpenPyXL](https://img.shields.io/badge/openpyxl-217346?style=flat-square&logo=microsoftexcel&logoColor=white) | `.xlsx` file engine |
| ![Pyperclip](https://img.shields.io/badge/pyperclip-3776AB?style=flat-square&logo=python&logoColor=white) | Clipboard access for fallback strategy |

</div>

---

## `~/notes`

> **Google Maps HTML changes** — Google may update page structure at any time, breaking the selectors. If that happens, inspect the page and update the selectors in `main.py`.

> **Rate limiting** — Avoid running the script at high frequency to prevent being blocked by Google.

> **Pyperclip on Linux** — requires `xclip` or `xsel`. On macOS, `pbcopy` is used. Windows is natively supported.

> **Missing phones** — Some companies may not have a phone number listed on Google Maps. Those rows will be empty in the output file.

---

<div align="center">
  <br/>
  <sub>
    Built by <a href="https://github.com/JulioFranz"><strong>Julio Franz</strong></a> and
    <a href="https://github.com/mj01px"><strong> Mauro Junior</strong></a>
  </sub>
   
  <br/><br/>
</div>
