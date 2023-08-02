from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/files_open/")
def files_open():
    fd_directory = "/proc/self/fd"
    fds = os.listdir(fd_directory)
    fd_info = {fd: os.readlink(os.path.join(fd_directory, fd)) for fd in fds}
    return fd_info
