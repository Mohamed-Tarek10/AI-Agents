# Created by: Mohamed Tarek

import time
import asyncio

def sync_task(name, second):
    print(f"[SYNC] {name} started")
    time.sleep(second)
    print(f"[SYNC] {name} completed")
    return name

async def async_task(name,second):
    print(f"[ASYBC] {name} started")
    await asyncio.sleep(second)
    print(f"[ASYNC] {name} completed")
    return name


async def run_async():
    start = time.pref_counter()
    await asyncio.gather(
        async_task("Task1", 1),
        async_task("Task2", 2),
        async_task("Task3", 3)
    )
    end = asyncio.get_event_loop().time()
    print(f"Async task completed in {end - start:.2f} seconds")


def run_sync():
    start = time.perf_counter()
    sync_task("Task1", 1)
    sync_task("Task2", 2)
    sync_task("Task3", 3)
    end = time.perf_counter()
    print(f"Sync task completed in {end - start:.2f} seconds")

if __name__ == "__main__":
    run_sync()
    asyncio.run(run_async())        
