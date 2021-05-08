import subprocess
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--testDir',required=False,help="Location of test files")
    parser.add_argument('--behaveOptions',type=str,required=False,help="String of behave option.For Example tags like -t <tag name>")

    args = parser.parse_args()
    testDir = args.testDir
    behaveOptions = '' if not args.behaveOptions else args.behaveOptions

    command = f'behave -k --no-capture {behaveOptions} {testDir} '
    print(f"Running Command: {command}")
    rs = subprocess.run(command,shell=True)