import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

from dotenv import load_dotenv
load_dotenv()

from BotWeb import BotWeb
from downloadCSV import downloadCSV

# Configurar WebDriver
# necessário inserir o caminho do chromedriver.exe
path = r'c:\Users\thayr\AppData\Local\Programs\Python\Python312\chromedriver.exe' # caminho do chromedriver
service = Service(path)
web = webdriver.Chrome(service=service)

try:
    time.sleep(5)
    # dados do usuário
    
    nome = os.environ.get("NOME")
    senha = os.environ.get("SENHA")
    
    universidade = os.environ.get("UNIVERSIDADE")
    campus = os.environ.get("CAMPUS")
    curso = os.environ.get("CURSO")
    turno = os.environ.get("TURNO")
    grau = os.environ.get("GRAU")
   
        
    # Acessar a página inicial
    web.get("https://brasil.io/home/")
    web.maximize_window()

    # clicar no botão de Login
    wait = WebDriverWait(web, 3)
    web.find_element(By.CLASS_NAME, 'dropdown-trigger').click()
    web.find_element(By.XPATH, '//*[@id="desktop_unauthenticated-dropdown"]/li[2]/a').click()

    # Inserir credenciais
    username = wait.until(EC.presence_of_element_located((By.ID, "id_username")))
    password = web.find_element(By.ID, "id_password")
    username.send_keys(nome)
    password.send_keys(senha)
    password.send_keys(Keys.RETURN)

    # Navegar para o dataset
    # botão de acesso ao dataset
    dataset_link = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section[2]/div/div[2]/a/div'))) 
    dataset_link.click()
    # botão de acesso ao "Cursos e notas de corte do PROUNI 2018"
    dataset = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div[1]')))
    dataset.click()
    # botão de acesso aos cursos
    cursos = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div[2]/div[2]/div/div[2]/div/a/b')))
    cursos.click()


    # diretório do aquivo CSV
    download_dir = "./downloads"
    os.makedirs(download_dir, exist_ok=True)
    time.sleep(5)  
    for file in os.listdir(download_dir):
        if file.endswith(".csv"):
            os.rename(os.path.join(download_dir, file),
                    os.path.join(download_dir, file))
            
                   
    # classes do robô e download do arquivo CSV      
    bot = BotWeb(universidade, campus, curso, turno, grau, wait)
    download = downloadCSV(download_dir, wait)
          
    # inserir filtros        
    bot.filtros()
    
    # filtrar botão
    filtrar = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="data"]/div[1]/div/form/div[2]/input')))
    filtrar.click()   
    time.sleep(2)
    
    # download do CSV filtrado
    download.download_csv()
        
finally:
    web.quit()


# ex: 'Pontifícia Universidade Católica de Minas Gerais - PUC MINAS', 'Lourdes', 'Ciências', 'Todos', 'Licenciatura',