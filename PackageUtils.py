import urllib.request
import gzip
import re
from pathlib import Path

def load_package_gz(dist, rep, component):
    packages_url = f"{rep}/dists/{dist}/{component}/binary-amd64/Packages.gz"
    with urllib.request.urlopen(packages_url) as response:
        compressed_data = response.read()
    name_gz = f'{dist}_{component}_Package.gz'
    with open(name_gz, 'wb') as f:
        f.write(compressed_data)

def load_packages(package_path):
    with gzip.open(package_path, 'rb') as f:
        content = f.read().decode('utf-8')
    packages = {}
    for part in content.split('\n\n'):
        name = ''
        for line in part.split('\n'):
            if line.startswith('Package:'):
                name = line.split()[1]

                if name not in packages:
                    packages[name] = {
                        'versions': [],
                        'dependencies': set()
                    }

            if line.startswith('Version:'):
                version = re.sub(r'Version: ', '', line)
                packages[name]['versions'].append(version)

            if line.startswith('Depends:') or line.startswith('Pre-Depends:'):
                deps = re.sub(r'(Pre-)?Depends:|:any|,|\||\([^)]+\)', ' ', line)

                packages[name]['dependencies'] |= set(deps.split())

    return packages