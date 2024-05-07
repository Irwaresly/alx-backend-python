#!/usr/bin/env python3
'''oroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers'''
import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random floating-point number between 0 and 10

async def async_comprehension():
    return [i async for i in async_generator()]

# Example usage:
async def main():
    result = await async_comprehension()
    print(result)

asyncio.run(main())

