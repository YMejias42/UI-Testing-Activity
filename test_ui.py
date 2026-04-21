from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time

ruta_archivo = "file://" + os.path.abspath("index.html")

driver = webdriver.Chrome()
driver.get(ruta_archivo)
driver.maximize_window()

def registrar_resultado(nombre_prueba, esperado, obtenido):
    estado = "PASS" if esperado == obtenido else "FAIL"
    print(f"{nombre_prueba}: {estado}")
    print(f"Esperado: {esperado}")
    print(f"Obtenido: {obtenido}")
    print("-" * 50)

def uat_1_campos_vacios():
    driver.refresh()
    time.sleep(5)
    driver.find_element(By.ID, "btnEnviar").click()
    time.sleep(5)
    mensaje = driver.find_element(By.ID, "mensaje").text
    registrar_resultado(
        "UAT-1",
        "Todos los campos son obligatorios.",
        mensaje
    )

def uat_2_correo_invalido():
    driver.refresh()
    time.sleep(5)
    driver.find_element(By.ID, "nombre").send_keys("Ana Torres")
    driver.find_element(By.ID, "correo").send_keys("ana@")
    Select(driver.find_element(By.ID, "curso")).select_by_value("ui")
    driver.find_element(By.ID, "btnEnviar").click()
    time.sleep(5)
    mensaje = driver.find_element(By.ID, "mensaje").text
    registrar_resultado(
        "UAT-2",
        "El correo electrónico no es válido.",
        mensaje
    )

def uat_3_registro_exitoso():
    driver.refresh()
    time.sleep(5)
    driver.find_element(By.ID, "nombre").send_keys("Ana Torres")
    driver.find_element(By.ID, "correo").send_keys("ana@email.com")
    Select(driver.find_element(By.ID, "curso")).select_by_value("ui")
    driver.find_element(By.ID, "btnEnviar").click()
    time.sleep(5)
    mensaje = driver.find_element(By.ID, "mensaje").text
    registrar_resultado(
        "UAT-3",
        "Registro enviado correctamente.",
        mensaje
    )

uat_1_campos_vacios()
uat_2_correo_invalido()
uat_3_registro_exitoso()

driver.quit()