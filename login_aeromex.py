from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_email = "ramiro.andino@viajaclick.com"
user_pw = "Clodi2001"
rfc = "GVI201216LX6"
razonsocial = "GRUPO VIAJACLICK"
codigo_postal = 77509
regimen = "601"

def loginto_aeromexico(driver):
    driver.get("https://amfacturacion.aeromexico.com/Inicio.aspx")
    wait = WebDriverWait(driver, 15)

    # Botón de iniciar sesión
    wait.until(EC.element_to_be_clickable((By.ID, "IdIniciar"))).click()

    # Campos de login
    wait.until(EC.presence_of_element_located((By.ID, "txtCorreo"))).send_keys(user_email)
    driver.find_element(By.ID, "txtClave").send_keys(user_pw)
    driver.find_element(By.ID, "btnEntrar").click()

    # Aceptar términos después de login
    wait.until(EC.element_to_be_clickable((By.ID, "chbLeido"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "btnAceptoLeido"))).click()
