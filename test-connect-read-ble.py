import asyncio
from bleak import BleakClient

address = "C1:86:98:EB:60:4F"
MODEL_NBR_UUID = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"

async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, loop))