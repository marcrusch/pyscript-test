from datetime import datetime
import asyncio


async def foo():
    while True:
        await asyncio.sleep(1)
        pyscript.write("timeOutput", datetime.now().strftime('%H:%M:%S'))

pyscript.run_until_complete(foo())
