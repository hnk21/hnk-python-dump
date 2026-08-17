import asyncio

async def func_1():
    task = asyncio.create_task(func_2())
    print(">> func_1 > task 1")
    print(">> func_1 > task 4")
    await asyncio.sleep(1)
    print(">> func_1 > task 5")
    await asyncio.sleep(1)

async def func_2():
    print(">> func_2 > task 2")
    await asyncio.sleep(1)
    print(">> func_2 > task 3")
    
asyncio.run(func_2())