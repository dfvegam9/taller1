# En un centro de Nutrición y Cuidado se requiere modelar una aplicación
# que permita llevar los datos y hacer los cálculos correspondientes para sus afiliados,
# para ello se han definido los siguientes requerimientos:

# De una persona es necesario conocer su:
# -> nombre,
# -> edad,
# -> estatura (en centímetros),
# -> peso (en kilogramos),
# -> el nivel de actividad física (un entero de 1 a 10) y
# -> el tipo de trabajo que realiza (sedentario o no sedentario).

# Al llegar al centro, se calcula el índice de masa corporal de la persona
# como el peso dividido sobre el cuadrado de la estatura. (peso (kg) / estatura (cm)^2)

# Con el indice de Masa Corporal se establece el estado de la persona, de acuerdo a la siguiente tabla:

# Estado              |       Indice de Masa Corporal
# -------------------------------------------------------
# Sedentaria          |       <= 18.49
# -------------------------------------------------------
# Delgadez            |       > 18.49 y <= 24.99
# -------------------------------------------------------
# Sobrepeso           |       > 24.99
# -------------------------------------------------------
# Normal              |       > 25.00

# Finalmente se establece el plan de trabajo así:
# si la persona es sedentaria, se le aplica el plan de Trabajo INTENSIVO,
# si la persona no es sedentaria pero su estado es Delgadez, se aplica también el plan de Trabajo INTENSIVO,
# si la persona tiene sobrepeso se la aplica el plan REDUCCIÓN,
# en cualquier otro caso, se aplica el plan NORMAL.


def obtener_tipo_trabajo(tipo_trabajo: str) -> str:
    if tipo_trabajo == "s":
        tipo_trabajo = "Sedentario"
    else:
        tipo_trabajo = "No sedentario"

    return tipo_trabajo


def calcular_indice_masa_corporal(peso: float, estatura: float) -> float:
    return peso / (estatura / 100) ** 2


def calcular_estado(indice_masa_corporal: float) -> str:
    if indice_masa_corporal <= 18.49:
        return "Delgadez"
    elif indice_masa_corporal <= 24.99:
        return "Normal"
    elif indice_masa_corporal > 24.99:
        return "Sobrepeso"


def calcular_plan_de_trabajo(estado: str, tipo_trabajo: str) -> str:
    tipo_trabajo = obtener_tipo_trabajo(tipo_trabajo)
    if tipo_trabajo == "Sedentario":
        return "Plan de Trabajo INTENSIVO"
    elif estado == "Delgadez":
        return "Plan de Trabajo INTENSIVO"
    elif estado == "Sobrepeso":
        return "Plan REDUCCIÓN"
    else:
        return "Plan NORMAL"


def validar_nombre(nombre) -> None:
    if len(nombre.strip()) < 2:
        print("El nombre debe tener al menos 2 caracteres.")
        exit()


def principal() -> None:
    # Se solicita la info al usuario:

    print()
    print(
        "--------------------------------------------------------------------------------"
    )
    print("INFORMACIÓN DEL USUARIO")
    print(
        "--------------------------------------------------------------------------------"
    )
    print()

    # -> Nombre
    nombre = input("Ingrese su nombre: ")

    # -> Apellido
    apellido = input("Ingrese su apellido: ")

    # -> Edad
    edad = int(input("Ingrese su edad: "))

    # -> Estatura
    estatura = float(input("Ingrese su estatura en centímetros: "))

    # -> Peso
    peso = float(input("Ingrese su peso en kilogramos: "))

    # -> Nivel de actividad física
    nivel_actividad = int(
        input(
            "Ingrese su nivel de actividad física donde 1 es muy inactiva y 10 es muy activa (1 a 10): "
        )
    )

    # -> Tipo de trabajo
    tipo_trabajo = input("¿Su trabajo es sedentario (S) o no sedentario (N)?: ")

    # Se validan los datos
    if nivel_actividad < 1 or nivel_actividad > 10:
        print("El nivel de actividad física debe ser un número entre 1 y 10")
        exit()

    if tipo_trabajo != "s" and tipo_trabajo != "n":
        print("El tipo de trabajo debe ser S (sedentario) o N (no sedentario)")
        exit()

    if edad < 18:
        print("La edad debe ser mayor a 18")
        exit()

    if nombre == "":
        print("El nombre no puede estar vacío")
        exit()

    if apellido == "":
        print("El apellido no puede estar vacío")
        exit()

    # Se realiza el proceso
    validar_nombre(nombre)
    indice_masa_corporal = round(
        calcular_indice_masa_corporal(peso, estatura), 2)
    estado = calcular_estado(indice_masa_corporal)
    tipo_trabajo = obtener_tipo_trabajo(tipo_trabajo)
    plan_de_trabajo = calcular_plan_de_trabajo(estado, tipo_trabajo)

    # Se muestra al usuario el resultado con un mensaje claro
    print()
    print()
    print(
        "--------------------------------------------------------------------------------"
    )
    print("RESULTADOS DEL CALCULO")
    print(
        "--------------------------------------------------------------------------------"
    )
    print()
    print()
    print("Nombre completo del usuario:", nombre, apellido)
    print("Edad del usuario:", edad, "años")
    print("Estatura del usuario en centímetros:", estatura, "cm")
    print("Peso del usuario en kilogramos:", peso, "kg")
    print(
        "Nivel de actividad física según la escala de 1 a 10",
        "-> Nivel:",
        nivel_actividad,
        "<-"
    )
    print("Tipo de trabajo:", tipo_trabajo)
    print("Indice de masa corporal:", indice_masa_corporal, "I.M.C.")
    print("Estado del usuario:", estado)
    print("Plan de trabajo sugerido:", plan_de_trabajo)
    print()
    print(
        "--------------------------------------------------------------------------------"
    )
    print("Fin del programa")
    input("Pulse cualquier tecla para salir...")
    exit()


principal()
