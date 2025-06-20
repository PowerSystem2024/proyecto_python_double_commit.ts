class Usuario:
    def __init__(self, nombre, apellido, email, contrasena):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasena = contrasena

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena

    def __str__(self):
        return f"""
        Usuario: {self._nombre}
        Apellido: {self._apellido}
        Email: {self._email}
        """
