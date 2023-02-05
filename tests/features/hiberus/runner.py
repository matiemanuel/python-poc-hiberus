import subprocess

if __name__ == '__main__':
    # command line args along with error capture on failure with check true
    s = subprocess.run('behave --dry-run --tags=smoke', shell=True, check=True)
