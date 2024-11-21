from Mundo.Contacto import Contacto

class ListaDeContactos:
    def __init__(self):
        self.contactos = []
        
    def darTodosLosContactos(self):
        return self.contactos
        
    def buscarContactoPalabraClave(self, palabra):
        return [contacto for contacto in self.contactos if contacto.contienePalabraClave(palabra)]
        
    def buscarContacto(self, nombre, apellido):
        for contacto in self.contactos:
            if contacto.darNombre().lower() == nombre.lower() and \
                contacto.darApellido().lower() == apellido.lower():
                return contacto
        return None
        
    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos=None, palabras=None):
        if self.buscarContacto(nombre, apellido) is not None:
            raise ValueError("Ya existe un contacto con ese nombre y apellido")
            
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
