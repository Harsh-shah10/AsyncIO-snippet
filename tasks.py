# ASYNCIO -> FOR MANAGING MANY WAITING TASKS
# PROCESSES -> FOR MAXIMIZING PERFORMANCE ON CPU INTENSIVE TASKS
# THREADS -> FOR PARALLEL TASKS THAT SHARE DATA WITH MINIMAL CPU USE

import asyncio

# ------- Tasks --------------------> Run concurrently

# Example 1 : create_task

import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    # Create tasks for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data(1, 2)) 
    task2 = asyncio.create_task (fetch_data(2, 10)) 
    task3 = asyncio.create_task(fetch_data(3, 1))

    result1 = await task1 
    result2 = await task2
    result3 = await task3
    print(result1, result2, result3)

# asyncio.run(main())


# Example 2 : To avoid creating multiple create_task we can use gather
# But gather is not good at error handline !!

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    # Run coroutines concurrently and gather their return values
    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))

    # Process the results
    for result in results:
        print(f"Received result: {result}")

# asyncio.run(main())


# Example 3 : Using Task Group

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time) # Simulate a network request or 10 operation 
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    tasks = []
    for i, sleep_time in enumerate([2, 1, 3], start=1): 
        task = asyncio.create_task(fetch_data(i, sleep_time))
        tasks.append(task)
    
    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)
    
    # Process results
    for result in results:
        print(f"Received result: {result}")

asyncio.run(main())