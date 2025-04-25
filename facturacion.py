from login_aeromex import loginto_aeromexico
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

user_email = "ramiro.andino@viajaclick.com"
user_pw = "Clodi2001"
rfc = "GVI201216LX6"
razonsocial = "GRUPO VIAJACLICK"
codigo_postal = 77509
regimen = "601"
reservas = ["AKABXS","kkkkkk"]

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

def completacion_de_factura(reserva):
    # Esperar y hacer clic en la clave
    wait.until(EC.element_to_be_clickable((By.ID, "CheckClave"))).click()
    
    # Esperar que el campo claveResTourCode sea visible y escribir la reserva
    wait.until(EC.visibility_of_element_located((By.ID, "claveResTourCode"))).send_keys(reserva)
    wait.until(EC.element_to_be_clickable((By.ID, "btnAgregar"))).click()

    # Continuar y hacer clic en el botón correspondiente
    wait.until(EC.element_to_be_clickable((By.ID, "MainContent_ctlBoletos_btnContinuar"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "btnAviso"))).click()

    # Espera crítica para cargar la página de datos fiscales
    time.sleep(4)
     
    rfccom = driver.find_element(By.ID, "rfc")
    rfccom.send_keys(rfc)

    razoncom = driver.find_element(By.ID, "nombre")
    razoncom.send_keys(razonsocial)

    codigocom = driver.find_element(By.ID, "codigoPostal")
    codigocom.send_keys(codigo_postal)

    time.sleep(3)  # Esperar a que procese la validación

    # Validar datos fiscales
    driver.find_element(By.ID, "btnValidarDatoFiscal").click()
    time.sleep(3)  # Esperar a que procese la validación

    fop_dropdown = driver.find_element(By.NAME, "ctl00$MainContent$ctlDatosFis$CmbTipoFOP")
    Select(fop_dropdown).select_by_value("4")
    time.sleep(1)

    regimen_dropdown = driver.find_element(By.NAME, "ctl00$MainContent$ctlDatosFis$ddRegimenFiscal")
    Select(regimen_dropdown).select_by_value("601")
    time.sleep(1)

    cfdi_dropdown = driver.find_element(By.NAME, "ctl00$MainContent$ctlDatosFis$ddUsoCFDI")
    Select(cfdi_dropdown).select_by_value("G03")
    time.sleep(1)

    driver.find_element(By.NAME, "ctl00$MainContent$ctlDatosFis$email").send_keys(user_email)
    time.sleep(1)
    driver.find_element(By.ID, "btnContinuar").click()
    time.sleep(2)

    # Aceptar el mensaje de confirmación
    driver.find_element(By.CLASS_NAME, "confirm").click()
    time.sleep(2)

    # Descargar la factura y finalizar
    driver.find_element(By.ID, "MainContent_ctlDescarga_btnDescarga").click()

    time.sleep(2)

    driver.find_element(By.ID, "ainic").click()

    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.ID, "chbLeido"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "btnAceptoLeido"))).click()


def inicio_de_facturacion():
    loginto_aeromexico(driver)
    time.sleep(2)  # Asegurar que se completó el login

    for reserva in reservas:
        completacion_de_factura(reserva)
        time.sleep(2)  # Pausa entre procesamiento de reservas

inicio_de_facturacion()