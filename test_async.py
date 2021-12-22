import asyncio

async def main():
    #Corutina
    print("Hola")
    await foo()
    print("Fin")

async def foo():
    #corutina
    print("Adios")
    await asyncio.sleep(2)

asyncio.run(main())