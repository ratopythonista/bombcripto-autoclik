import subprocess


def page_focus(page_name: str):
    windown_id = subprocess.Popen(f'xdotool search --name "{page_name}"', shell=True, stdout=subprocess.PIPE).stdout.read().decode().strip()
    subprocess.Popen(f'xdotool windowactivate {windown_id}', shell=True, stdout=subprocess.PIPE)