def calcular_imc(peso, altura):
    # Fórmula del IMC: peso / (altura^2)
    imc = peso / (altura ** 2)
    return imc

def clasificar_imc(imc, rangos):
    if rangos[0] <= imc <= rangos[1]:
        return "NORMAL"
    elif rangos[2] <= imc <= rangos[3]:
        return "SOBREPESO"
    elif rangos[4] <= imc <= rangos[5]:
        return "OBESIDAD 1"
    elif rangos[6] <= imc <= rangos[7]:
        return "OBESIDAD 2"
    elif imc >= rangos[8]:
        return "OBESIDAD 3"

if __name__ == "__main__":
    # Datos específicos según las tablas proporcionadas
    datos_personas = [
        {"nombre": "Persona1", "estatura": 1.44, "peso": 50},
        {"nombre": "Persona2", "estatura": 1.46, "peso": 60},
        # Agrega más datos según sea necesario
    ]

    # Definición de los rangos según las tablas proporcionadas
    rangos_persona1 = [38.4, 51.6, 51.8, 62, 62.2, 72.4, 72.6, 82.7, 82.9]
    rangos_persona2 = [39.4, 53, 53.3, 63.7, 63.9, 74.4, 74.6, 85.1, 85.3]
    # Agrega más rangos según sea necesario

    # Iteración sobre los datos de las personas
    for i, persona in enumerate(datos_personas):
        try:
            nombre = input("Ingrese nombre: ")
            apellido_paterno = input("Ingrese su apellido paterno: ")
            apellido_materno = input("Ingrese su apellido materno: ")
            edad = input("Ingrese su edad: ")
            estatura = float(input("Ingrese su estatura en metros: "))
            peso = float(input("Ingrese su peso en kilogramos: "))

            # Validar datos del usuario
            if peso <= 0 or estatura <= 0:
                print(f"{nombre}: Por favor, ingrese valores válidos para peso y altura.")
            else:
                # Calcular IMC 
                imc = calcular_imc(peso, estatura)

                # Mostrar resultados
                print("\nInformación del usuario:")
                print(f"Nombre: {nombre} {apellido_paterno} {apellido_materno}")
                print(f"Edad: {edad} años")
                print(f"Peso: {peso} kg")
                print(f"Estatura: {estatura} m")
                print(f"Índice de Masa Corporal (IMC): {imc:.2f}")

                # Selecciona los rangos adecuados según la persona
                if i == 0:
                    rangos = rangos_persona1
                elif i == 1:
                    rangos = rangos_persona2
                # Agrega más condiciones según sea necesario

                clasificacion = clasificar_imc(imc, rangos)
                print(f"{nombre}: Clasificación: {clasificacion}")

        except ValueError:
            print(f"{nombre}: Por favor, ingrese valores numéricos para peso y altura.")
