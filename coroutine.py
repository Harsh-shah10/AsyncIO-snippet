# ASYNCIO -> FOR MANAGING MANY WAITING TASKS
# PROCESSES -> FOR MAXIMIZING PERFORMANCE ON CPU INTENSIVE TASKS
# THREADS -> FOR PARALLEL TASKS THAT SHARE DATA WITH MINIMAL CPU USE

import asyncio

# ------- Co-routines -------------------->

# Example 1 :

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
	print("Fetching data...")
	await asyncio.sleep(delay) # Simulate an I/O operation with a sleep print("Data fetched")
	return {"data": "Some data"} # Return some data 

# Define another coroutine that calls the first coroutine
async def main():
	print("Start of main coroutine")
	task = fetch_data(2)
	print("End of main coroutine")
	result = await task
	print(f"Received result: {result}")

# Run the main coroutine
# asyncio.run(main())


# Example 2 : 

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
	print("Fetching data... id:", id)
	await asyncio.sleep(delay) # Simulate an I/O operation with a sleep print("Data fetched, id:", id)
	return {"data": "Some data", "id": id} # Return some data

# Define another coroutine that calls the first coroutine 
async def main():
	task1= fetch_data(2, 1)
	task2= fetch_data(2, 2)
	result1 = await task1
	print(f"Received result: {result1}")

	result2 = await task2
	print (f"Received result: {result2}")

# Run the main coroutine
asyncio.run(main())
