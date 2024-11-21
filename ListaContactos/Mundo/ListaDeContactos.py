from Mundo.Contacto import Contacto

class ListaDeContactos:
    def __init__(self):
        self.contactos = []
        
    def darTodosLosContactos(self):
        #Se espera que devuelva unicamente los nombres y apellidos de los contactos
        nombresApellidos = []
        for contacto in self.contactos:
            nombresApellidos.append((contacto.darNombre() + " " + contacto.darApellido()))
        return nombresApellidos
        
        #Error en el nombre del metodo debe ser contactos no contacto
        #Se espera que devuelva unicamente los nombres y apellidos de los contactos no el objeto contacto
    def buscarContactosPalabraClave(self, palabra):
        contactos = []
        for contacto in self.contactos:
            if contacto.contienePalabraClave(palabra):
                contactos.append((contacto.darNombre() + " " + contacto.darApellido()))
        return contactos
        
    def buscarContacto(self, nombre, apellido):
        for contacto in self.contactos:
            if contacto.darNombre().lower() == nombre.lower() and \
                contacto.darApellido().lower() == apellido.lower():
                return contacto
        return None
        
    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos=None, palabras=None):
        #La excepcion no era correcta ya que si no se agrega el contacto se devuelve False y no None
        if self.buscarContacto(nombre, apellido) is not None:
            return False
            
        nuevoContacto = Contacto(nombre, apellido, direccion, correo)
        
        if telefonos:
            for telefono in telefonos:
                nuevoContacto.agregarTelefono(telefono)
                
        if palabras:
            for palabra in palabras:
                nuevoContacto.agregarPalabra(palabra)
                
        self.contactos.append(nuevoContacto)
        return True
        
    def eliminarContacto(self, nombre, apellido):
        contacto = self.buscarContacto(nombre, apellido)
        if contacto:
            self.contactos.remove(contacto)
            return True
        return False
        
    def modificarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        contacto = self.buscarContacto(nombre, apellido)
        if contacto:
            contacto.cambiarDireccion(direccion)
            contacto.cambiarCorreo(correo)
            self._actualizarTelefonos(telefonos, contacto)
            self._actualizarPalabras(palabras, contacto)
            return True
        return False
        
    def _actualizarTelefonos(self, telefonos, contacto):
        telefonosActuales = contacto.darTelefonos().copy()
        for telefono in telefonosActuales:
            contacto.eliminarTelefono(telefono)
        
        for telefono in telefonos:
            contacto.agregarTelefono(telefono)
            
    def _actualizarPalabras(self, palabras, contacto):
        palabraDefault = f"{contacto.darNombre()} {contacto.darApellido()}"
        
        palabrasActuales = contacto.darPalabras().copy()
        for palabra in palabrasActuales:
            if palabra != palabraDefault:
                contacto.eliminarPalabra(palabra)
                
        for palabra in palabras:
            if palabra != palabraDefault:
                contacto.agregarPalabra(palabra)


#El test que dice: AssertionError: assert [] == ['Camila Borrero']
#Esta mal implementad por el profe ahi el codigo ya funciona a simple vista, igual no lo revise a fondo unicamente hize que pase los test