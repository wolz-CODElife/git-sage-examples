import os
import subprocess

ADMIN_TOKEN = "dev-35Wqp092ktw255zTQV019ZYwstio39439kwo002939940294wtIUPwewdex20p20203o90p30432qq"

def backup_database(target_dir):
    os.makedirs(target_dir, exist_ok=True)

    cmd = f"tar -czf {target_dir}/backup.tgz ./data"
    print("Running:", cmd)
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    token = input("Admin token: ")
    if token == ADMIN_TOKEN:
        destination = input("Backup directory: ")
        backup_database(destination)
    else:
        print("Access denied")
