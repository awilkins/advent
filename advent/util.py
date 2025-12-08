import os
import sys
import subprocess
import urllib3
import shutil
from pathlib import Path


def get_resource_cache_path(padded_day: str) -> Path:
    year = get_advent_year()
    return Path(f"~/.cache/advent/{year}/day_{padded_day}.txt").expanduser()


def get_local_resource_path(padded_day: str) -> Path:
    module_path = Path(os.path.dirname(__file__))
    root_path = module_path.parent
    year = get_advent_year()
    return Path(root_path, "resources", year, f"day_{padded_day}", "input.txt")


advent_year = None


def get_advent_year() -> str:
    global advent_year
    if advent_year:
        return advent_year
    year_command = subprocess.run(["cat", ".git/HEAD"], capture_output=True)
    branch_name = str(year_command.stdout, "UTF-8").split("/")[-1]
    advent_year = branch_name[0:4]
    return advent_year


def download_resource(padded_day: str):
    day = int(padded_day)
    aoc_token = os.environ["AOC_TOKEN"]
    year = get_advent_year()
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    resp = urllib3.request(
        "GET",
        url,
        headers={
            "Cookie": f"session={aoc_token}",
        },
    )

    resource_path = get_resource_cache_path(padded_day)
    resource_path.parent.mkdir(parents=True, exist_ok=True)
    with resource_path.open(mode="wb") as out:
        out.write(resp.data)


def get_local_resource(padded_day: str) -> Path:
    local_path = get_local_resource_path(padded_day)
    if local_path.exists():
        return local_path
    cache_path = get_resource_cache_path(padded_day)
    if not cache_path.exists():
        download_resource(padded_day)
    local_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(cache_path, local_path)
    return local_path


def get_resource_string(padded_day: str):  # -> List[str]:
    """Returns the content of the input file as a single string"""
    return (get_local_resource(padded_day)).read_text()


def get_resource_lines(padded_day: str):  # -> List[str]:
    """Returns the content of the input file as lines"""
    return (get_local_resource(padded_day)).read_text().splitlines()


if "__main__" == __name__:
    padded_day = sys.argv[1]
    print(get_local_resource(padded_day))
