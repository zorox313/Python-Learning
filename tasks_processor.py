tasks = ["connection_error", "out_of_memory", "file_not_found"]
while len(tasks) > 0:
    current_task = tasks.pop(0)
    print(f"processing:{current_task}")
    if current_task == "out_of_memory":
        print("Alert: This task needs immediate maintenance!")
    print(f"Remaining tasks in queue:{tasks}")
    print("-----task completed-----")


