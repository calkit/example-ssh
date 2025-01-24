"""Prototyping running in an SSH environment."""

import subprocess
import os

env = {
    "host": "172.20.32.185",
    "user": "pete",
    "wdir": "/home/pete/calkit/example-ssh",
}
host = env["host"]
user = env["user"]
wdir = env["wdir"]
send_files = [
    "script.sh"
]
get_files = ["lol.txt"]
key = os.path.expanduser("~/.ssh/id_ed25519")

cmd = "bash script.sh"

remote_cmd = f"cd '{wdir}' && {cmd}"

# First ensure the working directory exists on the host
subprocess.call(["ssh", "-i", key, f"{user}@{host}", f"mkdir -p {wdir}"])
# First send files
subprocess.call(["scp", "-i", key] + send_files + [f"{user}@{host}:{wdir}/"])
# Now run the command
subprocess.call(["ssh", "-i", key, f"{user}@{host}", remote_cmd])
# Now sync the files back
src_paths = ", ".join([wdir + "/" + p for p in get_files])
src = f"{user}@{host}:'{src_paths}'"
subprocess.call(["scp", "-i", key, src, "."])
