# EJERCICIO 1
nombre = ""
# Validar que el nombre solo tenga letras y no esté vacío
while not nombre.isalpha():
    nombre = input("Nombre del cliente: ")

cantidad = ""
# Validar que sea número y mayor a 0
while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Cantidad de productos a comprar: ")
cantidad = int(cantidad)

total_sin_desc = 0
total_con_desc = 0

# Iterar por cada producto
for i in range(cantidad):
    precio = ""
    while not precio.isdigit() or int(precio) <= 0:
        precio = input(f"Producto {i+1} - Precio: ")
    precio = int(precio)
    
    desc = ""
    # Validar S o N (mayúscula o minúscula)
    while desc.upper() not in ["S", "N"]:
        desc = input("¿Tiene descuento? (S/N): ").upper()
        
    total_sin_desc += precio
    if desc == "S":
        total_con_desc += precio * 0.90 # 10% de descuento
    else:
        total_con_desc += precio

ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cantidad

print(f"\nCliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

# EJERCICIO 2
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
acceso_concedido = False

while intentos < 3:
    intentos += 1
    print(f"Intento {intentos}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso_concedido = True
        break
    else:
        print("Error: credenciales inválidas.\n")

if not acceso_concedido:
    print("Cuenta bloqueada.")
else:
    opcion = ""
    while opcion != "4":
        print("\n1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ")
        
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
        elif int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
        else:
            if opcion == "1":
                print("Estado: Inscripto")
            elif opcion == "2":
                nueva_clave = input("Nueva clave: ")
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                else:
                    confirmacion = input("Confirmar clave: ")
                    if nueva_clave == confirmacion:
                        clave_correcta = nueva_clave
                        print("Clave cambiada exitosamente.")
                    else:
                        print("Error: Las claves no coinciden.")
            elif opcion == "3":
                print("¡La persistencia es la clave del éxito!")

# EJERCICIO 3
# Lunes: 4 cupos. Martes: 3 cupos.
l1, l2, l3, l4 = "", "", "", ""
m1, m2, m3 = "", "" , ""

operador = ""
while not operador.isalpha():
    operador = input("Nombre del operador: ")

opcion = ""
while opcion != "5":
    print("\n1. Reservar\n2. Cancelar\n3. Ver agenda\n4. Ver resumen\n5. Salir")
    opcion = input("Elegir opción: ")
    
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: Opción inválida.")
        continue
        
    if opcion == "1": # Reservar
        dia = ""
        while dia not in ["1", "2"]:
            dia = input("Día (1=Lunes, 2=Martes): ")
        
        paciente = ""
        while not paciente.isalpha():
            paciente = input("Nombre del paciente: ")
            
        if dia == "1":
            if paciente in [l1, l2, l3, l4] and paciente != "":
                print("Error: Paciente ya tiene turno el Lunes.")
            elif l1 == "": l1 = paciente
            elif l2 == "": l2 = paciente
            elif l3 == "": l3 = paciente
            elif l4 == "": l4 = paciente
            else: print("Error: No hay cupos para el Lunes.")
        elif dia == "2":
            if paciente in [m1, m2, m3] and paciente != "":
                print("Error: Paciente ya tiene turno el Martes.")
            elif m1 == "": m1 = paciente
            elif m2 == "": m2 = paciente
            elif m3 == "": m3 = paciente
            else: print("Error: No hay cupos para el Martes.")
            
    elif opcion == "2": # Cancelar
        dia = ""
        while dia not in ["1", "2"]:
            dia = input("Día (1=Lunes, 2=Martes): ")
        paciente = input("Nombre a cancelar: ")
        
        cancelado = False
        if dia == "1":
            if l1 == paciente: l1 = ""; cancelado = True
            elif l2 == paciente: l2 = ""; cancelado = True
            elif l3 == paciente: l3 = ""; cancelado = True
            elif l4 == paciente: l4 = ""; cancelado = True
        elif dia == "2":
            if m1 == paciente: m1 = ""; cancelado = True
            elif m2 == paciente: m2 = ""; cancelado = True
            elif m3 == paciente: m3 = ""; cancelado = True
            
        if cancelado:
            print("Turno cancelado con éxito.")
        else:
            print("No se encontró el paciente en ese día.")
            
    elif opcion == "3": # Ver agenda
        dia = ""
        while dia not in ["1", "2"]:
            dia = input("Día (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"Lunes -> T1: {l1 if l1 else '(libre)'}, T2: {l2 if l2 else '(libre)'}, T3: {l3 if l3 else '(libre)'}, T4: {l4 if l4 else '(libre)'}")
        elif dia == "2":
            print(f"Martes -> T1: {m1 if m1 else '(libre)'}, T2: {m2 if m2 else '(libre)'}, T3: {m3 if m3 else '(libre)'}")
            
    elif opcion == "4": # Resumen
        ocu_lun = (1 if l1 else 0) + (1 if l2 else 0) + (1 if l3 else 0) + (1 if l4 else 0)
        ocu_mar = (1 if m1 else 0) + (1 if m2 else 0) + (1 if m3 else 0)
        print(f"Lunes: {ocu_lun} ocupados, {4-ocu_lun} disponibles.")
        print(f"Martes: {ocu_mar} ocupados, {3-ocu_mar} disponibles.")
        if ocu_lun > ocu_mar: print("Día con más turnos: Lunes")
        elif ocu_mar > ocu_lun: print("Día con más turnos: Martes")
        else: print("Empate de turnos.")

# EJERCICIO 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzados_seguidos = 0 # Variable para la regla anti-spam

agente = ""
while not agente.isalpha():
    agente = input("Nombre del agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma and tiempo <= 3:
        print("SISTEMA BLOQUEADO. LA ALARMA HA SELLADO LA BÓVEDA.")
        break
        
    print(f"\nEstado: Energía={energia}, Tiempo={tiempo}, Cerraduras={cerraduras_abiertas}, Alarma={alarma}")
    print("1. Forzar cerradura (-20e, -2t)")
    print("2. Hackear panel (-10e, -3t)")
    print("3. Descansar (+15e, -1t)")
    
    opcion = input("Acción: ")
    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        opcion = input("Error. Ingrese 1, 2 o 3: ")
    opcion = int(opcion)
    
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzados_seguidos += 1
        
        if forzados_seguidos >= 3:
            print("Cerradura trabada por forzar demasiado. ¡Alarma activada!")
            alarma = True
        else:
            riesgo = False
            if energia < 40:
                print("Riesgo de alarma por baja energía.")
                num = ""
                while not num.isdigit() or int(num) not in [1, 2, 3]:
                    num = input("Elija un número del 1 al 3: ")
                if int(num) == 3:
                    alarma = True
                    riesgo = True
                    print("¡Alarma activada!")
            if not riesgo:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")
                
    elif opcion == 2:
        forzados_seguidos = 0 # Corta el spam
        energia -= 10
        tiempo -= 3
        print("Hackeando...")
        for paso in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completado! 1 Cerradura abierta.")
            
    elif opcion == 3:
        forzados_seguidos = 0 # Corta el spam
        tiempo -= 1
        energia += 15
        if energia > 100: energia = 100
        if alarma:
            energia -= 10
        print("Descansando...")

if cerraduras_abiertas == 3:
    print(f"¡VICTORIA, {agente}! Bóveda abierta.")
else:
    print(f"DERROTA, {agente}. Misión fallida.")

# EJERCICIO 5
vida_jugador = 100 # int
vida_enemigo = 100 # int
pociones = 3 # int
dano_pesado = 15 # int
dano_enemigo = 12 # int
turno_gladiador = True # boolean

nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del Gladiador: ")
    if not nombre.isalpha():
        print("Error: Solo se permiten letras.")

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")
    
    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        opcion = input("Error: Ingrese un número válido (1, 2 o 3): ")
    opcion = int(opcion)
    
    # TURNO DEL JUGADOR
    if opcion == 1:
        if vida_enemigo < 20:
            dano_final = float(dano_pesado * 1.5) # Float requerido para el crítico
            print("¡GOLPE CRÍTICO!")
        else:
            dano_final = dano_pesado
        vida_enemigo -= dano_final
        print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")
        
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
            
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Te has curado 30 puntos de vida.")
        else:
            print("¡No quedan pociones!")
            
    # TURNO DEL ENEMIGO 
    if vida_enemigo > 0:
        vida_jugador -= dano_enemigo
        print(f">> ¡El enemigo contraataca por {dano_enemigo} puntos!")

# FIN DEL JUEGO
print("\n=== RESULTADO ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")