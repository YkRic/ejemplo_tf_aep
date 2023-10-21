#Paso 1. Crear una ventana de tipo Dialog en QTDesigner:
#   - Para ingresar datos agregar el widget del tipo QLineEdit
#   - Para etiquetas, agregamos el widget del tipo QLabel
#   - Para agregar botones, agregamos el widget del tipo QPushButton
#   - Para este ejemplo se ha guardado la ventana que creamos en QTDesigner con el nombre VentanaSecundaria.ui,
#   la cual contiene 3 label (Nombre, Edad, Datos), dos LineEdit y un botón QPushButton

#Paso 2. Abrimos Pycharm y creamos un nuevo proyecto
#Paso 3. En la carpeta donde creamos el proyecto de pycharm guardamos la ventana que creamos en QTDesigner (VentanaSecundaria.ui)

#Paso 4. Vemos que en Pycharm aparece el archivo VentanaSecundaria.ui, si damos clic sobre él y presionamos shift + Enter
#   accederemos al su código xml, donde se muestra su configuración.

#Paso 5. Instalamos la librería PyQt5
#   - Ir al menú File->Settings: buscar la opción "Python Interpreter"
#   - Agregar la libreria PyQt5

#Paso 6. Importar las librerías necesarias
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QLineEdit, QPushButton

#Para la ventana principal
from PyQt5.QtWidgets import QMainWindow, QMenu, QAction

from PyQt5 import uic

#Paso 7. Crear una clase para la Ventana secundaria (recordar que el tipo de ventana creado en QTDesigner es QDialog)
class VentanaSecundaria(QDialog):
    def __init__(self, parent=None):
        super(VentanaSecundaria, self).__init__()

        #Paso 8. Utilizamos la función uic.loadUI() para asociar el archivo de QTDesigner con los Widget de PyQt5
        uic.loadUi("VentanaSecundaria.ui", self)

        #Paso 9. Asociamos los widget de PyQt5 con los del archivo de QTdesigner
        # lineEdit, lineEdit2, label y button son variables que creamos en la clase actual (self)
        #findChild es un método que permite asociar las variables con los widgets del archivo .ui que se
        # detallan en su código xml (ver paso 4).
        self.lineEdit = self.findChild(QLineEdit, "lineEdit")
        self.lineEdit2 = self.findChild(QLineEdit, "lineEdit_2")
        self.label = self.findChild(QLabel, "label_3")
        self.button = self.findChild(QPushButton, "pushButton")

        #Paso 10. Configuramos el evento al hacer clic, el cual debe llamar a una función donde ejecutaremos
        # nuestro código Python, en este ejemplo se ha creado la función "funcionesClick"
        self.button.clicked.connect(self.funcionesClick)

    def funcionesClick(self):
        print("Aquí agregamos el código que se ejecuta al hacer click en el botón")
        nombre = self.lineEdit.text()
        edad = int(self.lineEdit2.text())
        print("El nombre es: ", nombre)
        print("La edad es: ", edad)
        lista = [nombre, edad]
        print("Almacenamos los datos en una lista", lista)
        #En el tercer label de la ventana agregamos la siguiente línea:
        self.label.setText(f"El nombre es {nombre} y la edad es {edad} \nVer los datos en la consola de pycharm")


#Para este segundo ejemplo incluimos la ventana principal
class VentanaPrincipal(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Titulo de la ventana Principal")
        self.showMaximized()
        self._crearAcciones()
        self._crearBarraMenu()
        self._conectarAcciones()


    def _crearBarraMenu(self):
        barraMenu = self.menuBar()
        # Creamos el menú utilizando el widget QMenu
        Menu = QMenu("Archivo", self)
        barraMenu.addMenu(Menu)
        Menu.addAction(self.accionNuevo)
        Menu.addAction(self.accionAbrir)
        Menu.addAction(self.accionSalir)

        # Crear menu 2
        menuEditar = barraMenu.addMenu("Editar")
        menuEditar.addAction(self.accionCopiar)
        menuEditar.addAction(self.accionPegar)

        # Crear menu 3
        menuHelp = barraMenu.addMenu("Ayuda")
        menuHelp.addAction(self.accionHelp)
        menuHelp.addAction(self.accionAbout)

        #SubMenus
        menuEncontrar = menuHelp.addMenu("Sub Encontrar")
        menuEncontrar.addAction("Sub Encontrar 2")
        menuEncontrar.addAction("Sub Encontrar 3")

    #Creamos las acciones que se ejecutarán al hacer clic sobre las opciones del menú
    def _crearAcciones(self):
        # Crear acciones usando el primer constructor
        self.accionNuevo = QAction(self)
        self.accionNuevo.setText("Nuevo")
        #Crear acciones usando el segundo constructor
        self.accionAbrir = QAction("Abrir", self)
        self.accionSalir = QAction("Salir", self)

        self.accionCopiar = QAction("Copiar", self)
        self.accionPegar = QAction("Pegar", self)

        self.accionHelp = QAction("Ayuda", self)
        self.accionAbout = QAction("&Acerca de...", self)


    #Definimos las funciones que se ejecutarán al hacer clic sobre los elementos del menú
    def funcionNuevo(self):
        #Al hacer click en el menú nuevo se ejecuta esta función.
        print("Al hacer click en el menú nuevo se ejecuta esta función")

        #Aquí ensayamos el ejemplo de abrir una ventana flotante.
        #Abrir ventana flotante
        self.ventana = VentanaSecundaria()
        self.ventana.exec_()

    def funcionAbrir(self):
        print("funcion Abrir")

    def funcionCopiar(self):
        print("funcion Copiar")

    def funcionPegar(self):
        print("funcion Pegar")

    def funcionAyuda(self):
        print("funcion Ayuda")

    def funcionAbout(self):
        print("funcion About")

    def _conectarAcciones(self):
        # Connect File actions
        self.accionNuevo.triggered.connect(self.funcionNuevo)
        self.accionAbrir.triggered.connect(self.funcionAbrir)
        self.accionSalir.triggered.connect(self.close)

        # Conectar acciones de editar
        self.accionCopiar.triggered.connect(self.funcionCopiar)
        self.accionPegar.triggered.connect(self.funcionPegar)

        # Conectar las acciones de ayuda
        self.accionHelp.triggered.connect(self.funcionAyuda)
        self.accionAbout.triggered.connect(self.funcionAbout)


#En el main creamos la aplicación, creamos un nuevo objeto de la clase VentanaPrincipal y mostramos la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = VentanaPrincipal()
    win.show()
    sys.exit(app.exec_())
