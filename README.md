# 🧪 UI Testing con UAT y Selenium

## 📌 Descripción

Este proyecto demuestra la validación de una aplicación web simple mediante **User Acceptance Testing (UAT)**, pruebas manuales y pruebas automatizadas utilizando Python y Selenium.

La aplicación consiste en un formulario de registro donde el usuario debe ingresar:

* Nombre
* Correo electrónico
* Curso de interés

---

## 🎯 Objetivo

Validar que la interfaz funcione correctamente desde la perspectiva del usuario, asegurando:

* Correcta validación de datos
* Mensajes de error adecuados
* Confirmación de envío exitoso

---

## 🧩 Tecnologías utilizadas

* HTML5
* TailwindCSS
* JavaScript
* Python
* Selenium

---

## ✅ UAT implementados

### 🔹 UAT-1: Campos obligatorios

* Acción: Enviar formulario vacío
* Resultado esperado:
  `"Todos los campos son obligatorios."`

### 🔹 UAT-2: Correo inválido

* Acción: Ingresar correo incorrecto
* Resultado esperado:
  `"El correo electrónico no es válido."`

### 🔹 UAT-3: Registro exitoso

* Acción: Ingresar datos válidos
* Resultado esperado:
  `"Registro enviado correctamente."`

---

## ⚙️ Instalación y ejecución

### 1. Clonar repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd UI-Testing-Activity
```

### 2. Instalar dependencias

```bash
pip install selenium
```

### 3. Ejecutar pruebas

```bash
python test_ui.py
```

---

## 📊 Resultados esperados

En la consola se mostrarán los resultados de los UAT:

```
UAT-1: PASS
UAT-2: PASS
UAT-3: PASS
```

---

## 🧠 Aprendizaje

* Cómo convertir criterios de aceptación en pruebas
* Diferencia entre pruebas manuales y automatizadas
* Uso de Selenium para automatizar UI Testing

---

## 📁 Archivos incluidos

* `index.html` → Aplicación web
* `test_ui.py` → Pruebas automatizadas
* `README.md` → Documentación del proyecto

---

## 👨‍💻 Autor

Yeriel Mejias
