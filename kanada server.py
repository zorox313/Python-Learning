server_status = {
    "ip": "192.168.1.1",
    "location": "Toronto",
    "status": "active",
    "active_users": 150
}
print(f"The server in {server_status['location']},It has {server_status['active_users']} users")
server_status["Backup"] = True
server_status["status"] = "maintenance"
print(server_status)