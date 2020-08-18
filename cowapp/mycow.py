import subprocess


def cow_say(string):
    strcmd = ['cowsay', f'{str(string)}']
    result = subprocess.run(strcmd, text=True)
    return result
