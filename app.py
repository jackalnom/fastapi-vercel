from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/files_open/")
def files_open():
    fd_directory = "/proc/self/fd"
    fds = os.listdir(fd_directory)
    fd_info = {}
    for fd in fds:
        try:
            fd_info[fd] = os.readlink(os.path.join(fd_directory, fd))
        except FileNotFoundError:
            fd_info[fd] = "File descriptor closed before it could be read"
    return fd_info
