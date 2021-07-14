import requests
import sys
import shutil
import glob
import os


ARTIFACTS_URL = sys.argv[1]
GITHUB_TOKEN = sys.argv[2]
ARTIFACT_NAME = sys.argv[3]

response = requests.get(ARTIFACTS_URL)
data = response.json()
i = 0
for artifact in data["artifacts"]:
    download_url = artifact["archive_download_url"]
    artifact_name = artifact["name"]
    if artifact_name != ARTIFACT_NAME:
        continue
    print("Artifact download url:", download_url)
    artifact_response = requests.get(
        download_url,
        headers={"Authorization": f"token {GITHUB_TOKEN}"},
    )
    print("Artifact download status code:", artifact_response.status_code)
    if artifact_response.status_code == 200:
        filepath = f"report{i}.zip"
        with open(filepath, "wb") as f:
            f.write(artifact_response.content)
        i += 1
        print(f"wrote file {filepath}")

i = 0
for archive_path in glob.iglob("./*.zip"):
    shutil.unpack_archive(archive_path, "./")
    os.rename("./test_results.xml", f"./report{i}.xml")
    i += 1

print(f"unpacked {i} artifacts")
