import asyncio

async def obtener_datos():
    print("Solicitud de datos")
    await asyncio.sleep(2)
    print("Tengo los datos")
    return {"datos":25}

async def contar_cosas():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def main():
    tarea1 = asyncio.create_task(obtener_datos())
    tarea2 = asyncio.create_task(contar_cosas())
    print("Esperamos a que terminen")
    datos = await tarea1
    print("Datos obtenidos: ", datos)
    await tarea2
    print ("Todas las tareas completadas")

asyncio.run(main())
