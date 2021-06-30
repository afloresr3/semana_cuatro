class Cargo:
    secuencia=0
    def __init__(self,des="Sin Cargo"):
        Cargo.secuencia= Cargo.secuencia+1
        self.codigo=Cargo.secuencia
        self.descripcion= des

if __name__ == "__main__":
    cargo1= Cargo("Docente")
    print("Cargo1: ", cargo1.secuencia)
    print(cargo1.codigo, cargo1.descripcion)

    cargo2= Cargo("Analista")
    print("Cargo2: ",cargo2.secuencia)
    print(cargo2.codigo, cargo2.descripcion)

    cargo3= Cargo("Conserje")
    print("Cargo3: ",cargo3.secuencia)
    print(cargo3.codigo, cargo3.descripcion)


    print(Cargo.secuencia)
    print(cargo1.secuencia)
    print(cargo2.secuencia)
    print(cargo2.codigo)