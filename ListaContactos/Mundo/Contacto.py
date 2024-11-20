class Contacto:

    def __init__(self, nombre, apellido, direccion, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.correo = correo
        self.telefonos = set()
        self.palabrasClaves = {f"{nombre} {apellido}"}  
        
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
        self.telefonos.add(telefono)
        
    def eliminarTelefono(self, telefonoEliminar):
        if telefonoEliminar in self.telefonos:
            self.telefonos.remove(telefonoEliminar)
            
    def agregarPalabra(self, palabra):
        self.palabrasClaves.add(palabra)
        
    def eliminarPalabra(self, palabraEliminar):
        if palabraEliminar in self.palabrasClaves and palabraEliminar != f"{self.nombre} {self.apellido}":
            self.palabrasClaves.remove(palabraEliminar)
            
    def contienePalabraClave(self, palabra):
        return palabra.lower() in {p.lower() for p in self.palabrasClaves}