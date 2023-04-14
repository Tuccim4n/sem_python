nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David', 'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge', 'JOSE', 'Javier', 'Joaquín', 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

lista_nombres = nombres.split()
for i in range(len(lista_nombres)):
    lista_nombres[i] = lista_nombres[i].replace("'", "")
    lista_nombres[i] = lista_nombres[i].replace(",", "")

def inciso_a(nombres, notas_1, notas_2):
    notas_total = list(zip(notas_1, notas_2))
    dic = dict(zip(nombres, notas_total))
    return dic

def inciso_b(estudiantes):
    f = lambda b: (b[0] + b[1])/2
    promedio_individual = {a: f(b) for a, b in estudiantes.items()}
    return promedio_individual

def inciso_c(prom_est):
    return (sum(prom_est.values())/len(prom_est.values()))

def inciso_d(prom_est):
    max = -1
    max_est = ""
    for nom in prom_est:
        if (prom_est.get(nom) > max):
            max = prom_est.get(nom)
            max_est = nom
    print("Estudiante con la nota promedio mas alta: ", max_est, " ", max)
    
def inciso_e(estudiantes):
    min = 9999
    min_est = ""
    for nom in estudiantes:
        for nota in estudiantes.get(nom):
            if (nota < min):
                min = nota
                min_est = nom
    print("El estudiante con la nota mas baja: ", min_est, " ", min)

nombres_notas = inciso_a(lista_nombres, notas_1, notas_2)
promedios_individuales = inciso_b(nombres_notas)
print('Promedio general del curso: ', round(inciso_c(promedios_individuales), 3))
inciso_d(promedios_individuales)
inciso_e(nombres_notas)

