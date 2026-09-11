import subprocess
import time

CONTAINER = "restreamer"

while True:
    result = subprocess.run(
        ["docker", "inspect", "-f", "{{.State.Running}}", CONTAINER],
        capture_output=True,
        text=True
    )

    if result.returncode != 0 or result.stdout.strip() != "true":
        print("Restreamer stopped. Starting it...")

        subprocess.run([
            "docker", "start", CONTAINER
        ])

    else:
        print("Restreamer is running.")

    time.sleep(30)
