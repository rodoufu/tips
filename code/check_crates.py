#!/usr/bin/env python3
import requests
import asyncio


async def get_version(crate_name):
    url = f"https://crates.io/api/v1/crates/{crate_name}/versions"
    response = requests.get(url)
    if response:
        data = response.json()['versions']
        data = [x for x in data if not x['yanked']]
        last_version = data[0]["num"].strip()
        return last_version,
    else:
        return None, f"Problem finding the crate {crate_name}"


async def print_version(get_version, crate_name, crate_version):
    last_version = await get_version
    if last_version[0] is None:
        print(last_version[1])

        return False
    else:
        last_version = last_version[0]
        if crate_version.count('.') == 1 and last_version.count('.') >= 2 and last_version.startswith(crate_version):
            crate_version = last_version

        if crate_version < last_version:
            print(f"The crate {crate_name} in version {crate_version} "
                  f"can be updated to {last_version}")
            return True
    return False


async def can_update(crate_version_check):
    can_update = False
    for crate_check in crate_version_check:
        if await crate_check:
            can_update = True

    return can_update


async def check_file(file_lines):
    can_update = False
    dependencies_started = False
    dependencies = ["[dependencies]", "[dev-dependencies]"]
    for line in file_lines:
        if dependencies_started:
            if len(line.strip()) > 0:
                if line.startswith("["):
                    dependencies_started = any(x in line for x in dependencies)
                else:
                    line = line.replace(' ', '').replace('\n', '').replace('"', '')
                    crate = line.split('=')
                    if len(crate) == 2:
                        crate_name, crate_version = crate
                        crate_version = crate_version.strip()
                        # print(f"Checking crate: {crate_name}")
                        if await print_version(get_version(crate_name), crate_name, crate_version):
                            can_update = True
        else:
            dependencies_started = any(x in line for x in dependencies)
    return can_update


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("You need to provide the Cargo.toml path")
        exit(1)

    file_name = sys.argv[1]
    with open(file_name) as file_lines:
        if not asyncio.run(check_file(file_lines)):
            print("All the dependencies are update")
        else:
            exit(2)
