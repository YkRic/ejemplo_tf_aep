#Paso 1. Crear una ventana de tipo Dialog en QTDesigner:
#   - Para ingresar datos agregar el widget del tipo QLineEdit
#   - Para etiquetas, agregamos el widget del tipo QLabel
#   - Para agregar botones, agregamos el widget del tipo QPushButton
#   - Para este ejemplo se ha guardado la ventana que creamos en QTDesigner con el nombre ventana01.ui,
#   la cual contiene 3 label (Nombre, Edad, Datos), dos LineEdit y un botón QPushButton

#Paso 2. Abrimos Pycharm y creamos un nuevo proyecto
#Paso 3. En la carpeta donde creamos el proyecto de pycharm guardamos la ventana que creamos en QTDesigner (ventana01.ui)

#Paso 4. Vemos que en Pycharm aparece el archivo ventana01.ui, si hacemos clic sobre él y presionamos shift + Enter
#   accederemos al su código xml, donde se muestra su configuración.

#Paso 5. Instalamos la libreria PyQt5
#   - Ir al menú File->Settings: buscar la opción "Python Interpreter"
#   - Agregar la librería PyQt5

#Paso 6. Importar las librerías necesarias
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QLineEdit, QPushButton

from PyQt5 import uic

#Paso 7. Crear una clase para la Ventana secundaria (recordar que el tipo de ventana creado en QTDesigner es QDialog)
class VentanaSecundaria(QDialog):
    def __init__(self, parent=None):
        super(VentanaSecundaria, self).__init__()

        #Paso 8. Utilizamos la función uic.loadUI() para asociar el archivo de QTDesigner con los Widget de PyQt5
        uic.loadUi("ventana01.ui", self)

        #Paso 9. Asociamos los widget de PyQt5 con los del archivo de QTdesigner
        # lineEdit, lineEdit2, label y button son variables que creamos en la clase actual (self)
        #findChild es un método que permite asociar las variables con los widgets del archivo .ui que se
        # detallan en su codigo xml (ver paso 4).
        self.lineEdit = self.findChild(QLineEdit, "lineEdit")
        self.lineEdit2 = self.findChild(QLineEdit, "lineEdit_2")
        self.label = self.findChild(QLabel, "label_3")
        self.button = self.findChild(QPushButton, "pushButton")

        #Paso 10. Configuramos el evento al hacer clic, el cual debe llamar a una función donde ejecutaremos
        # nuestro código Python, en este ejemplo se ha creado la función "funcionesClick"
        self.button.clicked.connect(self.funcionesClick)

    def funcionesClick(self):
        print("Aquí agregamos el código que se ejecuta al hacer click en el boton")
        nombre = self.lineEdit.text()
        edad = int(self.lineEdit2.text())
        print("El nombre es: ", nombre)
        print("La edad es: ", edad)
        lista = [nombre, edad]
        print("Almacenamos los datos en una lista", lista)
        #En el tercer label de la ventana agregamos la siguiente línea:
        self.label.setText(f"El nombre es {nombre} y la edad es {edad}")

#En el main creamos la aplicación, creamos un nuevo objeto de la clase VentanaSecundaria y mostramos la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = VentanaSecundaria()
    win.show()
    sys.exit(app.exec_())

