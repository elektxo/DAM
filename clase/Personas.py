# clase Persona , la cual será el Padre de la clase Jugador.

class Personas:
#Constructor.
    def __init__(self,nombre,apellido,psudonimo,edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__psudonimo = psudonimo
        self.__edad = edad
        self.__categoria = None
        self.__nro_partidas_ganadas = 0
        self.__nro_partidas_totales = 0
        self.__nro_torneos_ganados = 0
        self.__nro_torneos_participados = 0
    #getter/setter nombre.
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    #getter/setter apellido.
    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
    #getter/setter edad.
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        while True:
            if edad >= 12:
                self.__edad = edad
                break
            else:
                edad = input("Introduce una edad mayor o igual a 12 años: ")
    #getter/setter psudonimo.
    @property
    def psudonimo(self):
        return self.__psudonimo
    @psudonimo.setter
    def psudonimo(self, psudonimo):
        self.__psudonimo = psudonimo
    #getter/setter categoria.
    @property
    def categoria(self):
        return self.__categoria
    @categoria.setter
    def categoria(self, categoria):
        if categoria in ("Juvenil","Amateur","Master","Senior"):
            self.__categoria = categoria
        else:
            print("Esa categoria no existe.")
    #getter/setter nro_partidas_ganadas.
    @property
    def nro_partidas_ganadas(self):
        return self.__nro_partidas_ganadas
    @nro_partidas_ganadas.setter
    def nro_partidas_ganadas(self, nro_partidas_ganadas):
        self.__nro_partidas_ganadas = nro_partidas_ganadas
    #getter/setter nro_partidas_totales.
    @property
    def nro_partidas_totales(self):
        return self.__nro_partidas_totales
    @nro_partidas_totales.setter
    def nro_partidas_totales(self, nro_partidas_totales):
        self.__nro_partidas_totales = nro_partidas_totales
    #getter/setter nro_torneos_ganados.
    @property
    def nro_torneos_ganados(self):
        return self.__nro_torneos_ganados
    @nro_torneos_ganados.setter
    def nro_torneos_ganados(self, nro_torneos_ganados):
        self.__nro_torneos_ganados = nro_torneos_ganados
    #getter/setter nro_torneos_ganados.
    @property
    def nro_torneos_participados(self):
        return self.__nro_torneos_participados
    @nro_torneos_participados.setter
    def nro_torneos_participados(self, nro_torneos_participados):
        self.__nro_torneos_participados = nro_torneos_participados
    #metodos

    def modificarEdad(self,edad):
        self.edad = edad
        self.__actualizarCategoria(edad)

    def  incrementarNroPartidasGanadas(self):
        self.nro_partidas_ganadas += 1

    def  incrementarNroPartidasTotales(self):
        self.nro_partidas_totales += 1

    def incrementarNroTorneosGanados(self):
        self.nro_torneos_ganados += 1

    def incrementarNroTorneosParticipados(self):
        self.nro_torneos_participados +1
    def __actualizarCategoria(self,edad):
        if edad >= 12 and  edad <= 17:
            self.categoria = "Juvenil"
        elif  edad >= 18 and edad <= 24:
            self.categoria = "Amateur"
        elif  edad >= 25 and edad <= 60:
            self.categoria = "Master"
        elif  edad > 60:
            self.categoria = "Senior"
    def mostrarDatosPersona(self):
        return f'''\n----Datos----\n
        Nombre : {self.nombre}
        Apellido: {self.apellido}
        Psudonimo: {self.psudonimo}
        Edad: {self.edad}
        Categoria: {self.categoria}
        Partidas ganadas: {self.nro_partidas_ganadas}
        Partidas totales: {self.nro_partidas_totales}
        Torneo ganados: {self.nro_torneos_ganados}
        Torneo participados: {self.nro_torneos_participados}
        -----------------------
        '''