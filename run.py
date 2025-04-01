import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Error: {result.stderr}")

def initialize_git():
    commands = [
        "git init",
        "git add .",
        "git commit -m 'first commit'",
        "git branch -M main",
        "git remote add origin git@github.com:ni9gas/app.git",
        "git push -u origin main"
    ]
    
    for cmd in commands:
        print(f"Running: {cmd}")
        run_command(cmd)

if __name__ == "__main__":
    initialize_git()

