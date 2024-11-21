class Contacto:

    def __init__(self, nombre, apellido, direccion, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.correo = correo
        self.telefonos = []
        self.palabrasClaves = []
        
    def darNombre(self):
        return self.nombre
        
    def darApellido(self):
        return self.apellido
        
    def darDireccion(self):
        return self.direccion
        
    def darCorreo(self):
        return self.correo
        
    def darTelefonos(self):
        return self.telefonos
        
    def darPalabras(self):
        return self.palabrasClaves
        
    def cambiarDireccion(self, direccion):
        self.direccion = direccion
        
    def cambiarCorreo(self, correo):
        self.correo = correo
        
    def agregarTelefono(self, telefono):
        self.telefonos.append(telefono)
        
    def eliminarTelefono(self, telefonoEliminar):
        if telefonoEliminar in self.telefonos:
            self.telefonos.remove(telefonoEliminar)
            
    def agregarPalabra(self, palabra):
        self.palabrasClaves.append(palabra)
        
    def eliminarPalabra(self, palabraEliminar):
        if palabraEliminar in self.palabrasClaves:
            self.palabrasClaves.remove(palabraEliminar)
            
    def contienePalabraClave(self, palabra):
        return palabra in self.palabrasClaves