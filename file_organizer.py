#!/usr/bin/env python3
"""
file_organizer.py
A simple script to organize files in a directory into subfolders by file type.
Usage:
    python file_organizer.py /path/to/target_folder
Options:
    --dry-run    : Show what would be moved without changing files
    --verbose    : Print each action
"""

import sys
import shutil
import os
from pathlib import Path
import argparse

# Mapping of folder name -> extensions
EXT_MAP = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".heic"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv", ".webm"},
    "Documents": {".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".txt", ".md"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg"},
    "Archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
    "Code": {".py", ".js", ".java", ".c", ".cpp", ".cs", ".html", ".css", ".json", ".sql"},
}

def detect_category(suffix: str) -> str:
    suffix = suffix.lower()
    for category, exts in EXT_MAP.items():
        if suffix in exts:
            return category
    return "Others"

def ensure_folder(base: Path, folder_name: str, dry_run: bool):
    target = base / folder_name
    if not target.exists():
        if dry_run:
            print(f"[DRY-RUN] Would create folder: {target}")
        else:
            target.mkdir(parents=True, exist_ok=True)
    return target

def unique_target_path(target: Path) -> Path:
    """If target exists, append (1), (2) ... before extension."""
    if not target.exists():
        return target
    parent = target.parent
    stem = target.stem
    suffix = target.suffix
    counter = 1
    while True:
        new_name = f"{stem}({counter}){suffix}"
        candidate = parent / new_name
        if not candidate.exists():
            return candidate
        counter += 1

def organize_folder(folder: Path, dry_run: bool=False, verbose: bool=False):
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Invalid folder: {folder}")

    # Avoid organizing inside the destination folders themselves
    ignore_dirs = set(EXT_MAP.keys()) | {"Others"}

    moved = 0
    for item in folder.iterdir():
        if item.is_dir():
            # skip known category dirs
            if item.name in ignore_dirs:
                if verbose:
                    print(f"Skipping folder: {item.name}")
                continue
            # Optionally, skip hidden dirs
            if item.name.startswith('.'):
                continue
            # For nested folders, you might want to optionally organize recursively.
            continue

        # it's a file
        dest_category = detect_category(item.suffix)
        dest_folder = ensure_folder(folder, dest_category, dry_run)
        dest_path = dest_folder / item.name

        # handle duplicates
        dest_path = unique_target_path(dest_path)

        if dry_run:
            print(f"[DRY-RUN] Would move: {item.name} -> {dest_category}/{dest_path.name}")
        else:
            if verbose:
                print(f"Moving: {item.name} -> {dest_category}/{dest_path.name}")
            try:
                shutil.move(str(item), str(dest_path))
                moved += 1
            except Exception as e:
                print(f"Error moving {item}: {e}")

    print(f"Done. Files moved: {moved}")

def parse_args():
    ap = argparse.ArgumentParser(description="Organize files in a folder by file type.")
    ap.add_argument("folder", type=str, help="Target folder path to organize")
    ap.add_argument("--dry-run", action="store_true", help="Show what would happen without moving files")
    ap.add_argument("--verbose", action="store_true", help="Print detailed actions")
    return ap.parse_args()

def main():
    args = parse_args()
    folder = Path(args.folder).expanduser().resolve()
    organize_folder(folder, dry_run=args.dry_run, verbose=args.verbose)

if __name__ == "__main__":
    main()

