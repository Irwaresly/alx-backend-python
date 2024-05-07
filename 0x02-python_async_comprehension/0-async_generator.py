#!/usr/bin/env python3
'''coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10'''
import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random floating-point number between 0 and 10

# Example usage:
async def print_yielded_values():
    async for i in async_generator():
        print(i)

asyncio.run(print_yielded_values())

