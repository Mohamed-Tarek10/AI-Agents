#   Created by: Mohamed Tarek

import time
import asyncio

def sync_task(name, seconds):
    print(f"[SYNC] {name} started")
    time.sleep(seconds)
    print(f"[SYNC] {name} completed")
    return name

async def async_task(name, seconds):
    print(f"[ASYNC] {name} started")
    await asyncio.sleep(seconds)
    print(f"[ASYNC] {name} completed")
    return name

async def run_async():
    start = time.perf_counter()
    results = await asyncio.gather(
        async_task("Task 1", 2),
        async_task("Task 2", 2),
        async_task("Task 3", 2)
    )
    print(results)
    end = time.perf_counter()
    print(f"Async tasks completed in {end - start:.2f} seconds")

def run_sync():
    start = time.perf_counter()
    sync_task("Task 1", 2)
    sync_task("Task 2", 2)
    sync_task("Task 3", 2)
    end = time.perf_counter()
    print(f"Sync tasks completed in {end - start:.2f} seconds")


if __name__ == "__main__":
    run_sync()
    asyncio.run(run_async())