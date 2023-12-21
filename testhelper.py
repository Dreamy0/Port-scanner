from subprocess import PIPE, Popen


def capture(command: str) -> str:
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()
    return out, err, process.returncode
