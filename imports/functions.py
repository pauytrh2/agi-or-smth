from os import system as run_command

def write_file(path, content):
    run_command(f"echo '{content}' > {path}")

def open_url(url):
    run_command(f"zen-browser {url}")