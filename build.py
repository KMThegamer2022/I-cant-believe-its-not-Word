#!/usr/bin/env python3
"""
Build the single-file HTML from modules.
Usage:
  python3 build.py          # builds latest version to root
  python3 build.py v2.0     # builds specific version to root
  python3 build.py --list   # lists all versions
"""
import os, sys, glob, shutil

BASE = os.path.dirname(os.path.abspath(__file__))
VERSIONS_DIR = os.path.join(BASE, 'versions')
OUTPUT = os.path.join(BASE, "I cant believe its not Word.html")

def list_versions():
    if not os.path.isdir(VERSIONS_DIR):
        print("No versions directory found.")
        return []
    versions = sorted([d for d in os.listdir(VERSIONS_DIR) if os.path.isdir(os.path.join(VERSIONS_DIR, d))])
    for v in versions:
        readme = os.path.join(VERSIONS_DIR, v, 'README.md')
        status = ""
        if os.path.isfile(readme):
            with open(readme) as f:
                for line in f:
                    if line.startswith('**Status:**'):
                        status = line.split(':',1)[1].strip()
                        break
        print(f"  {v:10s}  {status}")
    return versions

def get_latest_version():
    versions = sorted([d for d in os.listdir(VERSIONS_DIR) if os.path.isdir(os.path.join(VERSIONS_DIR, d))])
    return versions[-1] if versions else None

def build(version=None):
    if version is None:
        version = get_latest_version()
        if version is None:
            print("No versions found. Run with a version name.")
            return
        print(f"Building latest version: {version}")
    else:
        print(f"Building version: {version}")

    modules_dir = os.path.join(VERSIONS_DIR, version, 'modules')
    if not os.path.isdir(modules_dir):
        print(f"Error: {modules_dir} not found.")
        return

    parts = []
    for path in sorted(glob.glob(os.path.join(modules_dir, '*.html'))):
        with open(path, 'r', encoding='utf-8') as f:
            parts.append(f.read())

    combined = '\n'.join(parts)

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(combined)

    size_kb = os.path.getsize(OUTPUT) / 1024
    print(f"Built: {OUTPUT}")
    print(f"Version: {version}")
    print(f"Size: {size_kb:.1f} KB")
    print(f"Modules combined: {len(parts)}")

if __name__ == '__main__':
    if '--list' in sys.argv or '-l' in sys.argv:
        print("Available versions:")
        list_versions()
    elif len(sys.argv) > 1 and not sys.argv[1].startswith('-'):
        build(sys.argv[1])
    else:
        build()
