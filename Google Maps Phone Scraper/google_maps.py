import re
import pandas as pd
import pyperclip
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def obter_telefone_empresa(nome_empresa, driver):

    nome_empresa_formatado = nome_empresa.replace(' ', '+')
    url = f"https://www.google.com/maps/search/{nome_empresa_formatado}"
    driver.get(url)

    try:
        try:
            # Tenta pegar o telefone direto da listagem pelo span
            telefone_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.Usd1K"))
            )
            telefone = telefone_element.text.strip()
            if telefone:
                print(f"Telefone encontrado na listagem: {telefone}")
                return telefone
        except:
            pass

        copiar_telefone_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//button[@aria-label='Copiar número de telefone']")))
        copiar_telefone_element.click()
        print("Clicou no botão de copiar")

        telefone_texto = pyperclip.paste()
        return telefone_texto.strip()
    except Exception as e:
        print(f"Erro ao obter telefone: {e}")
        return None
def main():
    df = pd.read_excel('empresas.xlsx')
    driver = webdriver.Chrome()
    if 'Empresa' not in df.columns:
        print("A coluna 'Empresa' não foi encontrada no arquivo Excel.")
        return

    df['Telefone'] = None
    for i, row in df.iterrows():
        nome_empresa = row['Empresa']
        print(f"Buscando telefone para: {nome_empresa}")
        telefone = obter_telefone_empresa(nome_empresa, driver)
        if telefone:
            df.at[i, 'Telefone'] = telefone
        else:
            print(f"Telefone não encontrado para: {nome_empresa}")

    output_file = 'empresas_com_telefone.xlsx'
    df.to_excel(output_file, index=False)
    print(f"Resultados salvos em {output_file}")



if __name__ == '__main__':
    main()
