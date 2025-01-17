# classe do robô web
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class BotWeb:
    def __init__(self, universidade, campus, curso, turno, grau, wait):
        self.universidade = universidade
        self.campus = campus
        self.curso = curso
        self.turno = turno
        self.grau = grau
        self.wait = wait
        
    def filtros(self):
        # Esperar e clicar no menu "Universidade"
        botao_universidade = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="data"]/div[1]/div/form/div[1]/div[4]/div/input')))
        botao_universidade.click()
        # Localizar todas as opções do dropdown
        opcoes_universidade = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.dropdown-content li span')))
        for opcao in opcoes_universidade:
            if opcao.text.strip() == self.universidade:
                opcao.click()
                break

        # Filtrar pelo nome do campus
        botao_campus = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_campus_nome"]')))
        botao_campus.send_keys(self.campus)

        # Esperar e clicar no menu "Curso"
        botao_curso = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="data"]/div[1]/div/form/div[1]/div[6]/div/input')))
        botao_curso.click()
        opcoes_curso = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.dropdown-content li span')))
        for opcao in opcoes_curso:
            if opcao.text.strip() == self.curso:
                opcao.click()
                break

        # Esperar e clicar no menu "Turno"
        botao_turno = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="data"]/div[1]/div/form/div[1]/div[8]/div/input')))
        botao_turno.click()
        opcoes_turno = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.dropdown-content li span')))
        for opcao in opcoes_turno:
            if opcao.text.strip() == self.turno:
                opcao.click()
                break

        # Esperar e clicar no menu "Grau"
        botao_grau = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="data"]/div[1]/div/form/div[1]/div[7]/div/input')))
        botao_grau.click()
        opcoes_grau = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.dropdown-content li span')))
        for opcao in opcoes_grau:
            if opcao.text.strip() == self.grau:
                opcao.click()
                break

        print('Filtros aplicados com sucesso!')