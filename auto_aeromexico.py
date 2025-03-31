from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 

user_email = "ramiro.andino@viajaclick.com"
user_pw = "Clodi2001"
rfc = "GVI201216LX6"
razonsocial = "GRUPO VIAJACLICK"
codigo_postal = 77509
regimen = "601"
# reserva = ""

driver = webdriver.Chrome()




def aeromexico (reserva):
    driver = webdriver.Chrome()
    driver.get("https://amfacturacion.aeromexico.com/Inicio.aspx")

    """before login"""
    loginbutton = driver.find_element(By.XPATH,'//*[@id="IdIniciar"]')
    loginbutton.click()
    time.sleep(2)

    email =  driver.find_element(By.XPATH,'//*[@id="txtCorreo"]')
    email.send_keys(user_email)

    password = driver.find_element(By.XPATH,'//*[@id="txtClave"]')
    password.send_keys(user_pw)

    start_login_button = driver.find_element(By.XPATH,'//*[@id="btnEntrar"]')
    start_login_button.click()

    time.sleep(2)

    """after login"""
    check_btn_afterlogin = driver.find_element(By.XPATH,'//*[@id="chbLeido"]')
    check_btn_afterlogin.click()

    accept_btn = driver.find_element(By.XPATH,'//*[@id="btnAceptoLeido"]')
    accept_btn.click()

    reservationcheck_btn = driver.find_element(By.XPATH,'//*[@id="CheckClave"]')
    reservationcheck_btn.click()

    time.sleep(2)

    numero_boleto = driver.find_element(By.XPATH,'//*[@id="claveResTourCode"]')
    numero_boleto.send_keys(reserva)

    buscar_reserva_btn = driver.find_element(By.XPATH,'//*[@id="btnAgregar"]')
    buscar_reserva_btn.click()

    time.sleep(3)

    continuar_btn = driver.find_element(By.XPATH,'//*[@id="MainContent_ctlBoletos_btnContinuar"]')
    continuar_btn.click()

    time.sleep(2)

    aviso_ok_btn = driver.find_element(By.XPATH,'//*[@id="btnAviso"]')
    aviso_ok_btn.click()


    rfc_input = driver.find_element(By.XPATH,'//*[@id="rfc"]')
    rfc_input.send_keys(rfc)

    razonsocial_input = driver.find_element(By.XPATH,'//*[@id="nombre"]')
    razonsocial_input.send_keys(razonsocial)

    codigoposta_input = driver.find_element(By.XPATH,'//*[@id="codigoPostal"]')
    codigoposta_input.send_keys(codigo_postal)
    time.sleep(1.5)

    validardatos_btn = driver.find_element(By.XPATH,'//*[@id="btnValidarDatoFiscal"]')
    validardatos_btn.click()

    time.sleep(5)

    select_tdc = driver.find_element(By.NAME,"ctl00$MainContent$ctlDatosFis$CmbTipoFOP")
    select = Select(select_tdc)
    select.select_by_value("4")

    time.sleep(1)

    select_regimen = driver.find_element(By.NAME,"ctl00$MainContent$ctlDatosFis$ddRegimenFiscal")
    selectregi = Select(select_regimen)
    selectregi.select_by_value(regimen)

    time.sleep(1)

    cfdi = driver.find_element(By.NAME,"ctl00$MainContent$ctlDatosFis$ddUsoCFDI")
    selectcfdi = Select(cfdi)
    selectcfdi.select_by_value("G03")

    time.sleep(1)

    email_input = driver.find_element(By.NAME,"ctl00$MainContent$ctlDatosFis$email")
    email_input.send_keys(user_email)

    time.sleep(1)

    continuar_btn = driver.find_element(By.XPATH,'//*[@id="btnContinuar"]')
    continuar_btn.click()

    time.sleep(3)

    confirmar_factura = driver.find_element(By.CLASS_NAME,'confirm')
    confirmar_factura.click()

    descargar_factura = driver.find_element(By.XPATH,'//*[@id="MainContent_ctlDescarga_btnDescarga"]')
    descargar_factura.click()

    time.sleep(5)




    """OTRA FUNC"""

    # cargar_constancia_selection = driver.find_element(By.XPATH,'//*[@id="profile-tab2"]')
    # cargar_constancia_selection.click()

    # file_input = driver.find_element(By.ID, "cif")
    # file_input.send_keys(upload_file)

    # validate_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnUploadFile")))
    # driver.execute_script("arguments[0].removeAttribute('disabled')", validate_button)

    # validate_button.click()

    # time.sleep(2)

    # driver.find_element(By.ID, "cif")

    # cargar_confirmar = driver.find_element(By.XPATH,'//*[@id="btnUploadFile"]')
    # time.sleep(2)
    # cargar_confirmar.click()










    """LO QUE VA A PASAR ES QUE LE DAREMOS A CAPTURAR RFC ENVES DE SUBIR EL ARCHIVO"""




















