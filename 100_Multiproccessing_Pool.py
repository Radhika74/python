from multiprocessing import Pool

def process_task(task):
    print("Task processed:", task)
    return task  # If you need to return a result

if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    with Pool(processes=4) as pool:
        results = pool.map(process_task, tasks)
    # Print results if needed
    print(results)
