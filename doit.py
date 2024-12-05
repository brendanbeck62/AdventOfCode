import os
import shutil
from datetime import datetime
import argparse
import requests
import ssl



def get_args():
    parser = argparse.ArgumentParser(
                    prog='doig',
                    description='generates folder structure for AoC and pulls down input file if it exists')
    parser.add_argument('-s', '--session_id', required=True, help='session token from advent of code. (sign in, application > cookies)')
    parser.add_argument('-y', '--year', help='format: 2024. create year [default = this year]')
    parser.add_argument('-d', '--day', help='format: 01. create day [default = today]')
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    # create folder for year
    year = args.year if args.year else datetime.today().strftime('%Y')
    if not os.path.isdir(year):
        os.makedirs(year)

    # create folder for day
    day = f"{int(args.day):02d}" if args.day else datetime.today().strftime('%d')
    day_path = f"{year}/{day}"
    if not os.path.isdir(day_path):
        os.makedirs(day_path)

    # create python script from template
    shutil.copy2('./template.py', f"{day_path}/day-{day}.py")
    open(f"{day_path}/example1.txt", 'a').close()

    # download input
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {
		"cookie": f"session={args.session_id}"
	}
    res = requests.get(f"https://adventofcode.com/{year}/day/{day.lstrip("0")}/input", headers=headers)
    with open(f"{day_path}/in.txt", 'w+') as f:
        f.write(res.text.removesuffix("\n"))
