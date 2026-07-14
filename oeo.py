def check_status(status):
    if status == "server_down":
        return "Warning: Server is offline!"
    else:
        return "Warning: Server is online!"
check_status("server_up")
server_message = check_status("server_down")
print(f"server_message: {server_message}")