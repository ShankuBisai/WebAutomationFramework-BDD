import subprocess

if __name__ == '__main__':
    rs = subprocess.run('behave ./feature/loginpage.feature --no-capture',shell=True)
