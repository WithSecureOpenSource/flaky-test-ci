import subprocess

for i in range(15):
    subprocess.run(["pytest", f"--junit-xml=report{i}.xml"])
