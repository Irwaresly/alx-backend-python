#!/usr/bin/env python3
import asyncio
from time import perf_counter
from typing import List

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random floating-point number between 0 and 10

async def async_comprehension() -> List[float]:
    return [i async for i in async_generator()]

async def measure_runtime() -> float:
    start_time = perf_counter()  # Start measuring time
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = perf_counter()  # End measuring time
    return end_time - start_time  # Return total runtime

# Example usage:
async def main():
    total_runtime = await measure_runtime()
    print("Total runtime:", total_runtime)

asyncio.run(main())

