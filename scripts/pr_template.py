#!/usr/bin/env python3
"""CLI: pr-template"""
import sys, json, argparse
from datetime import datetime
def main():
    parser = argparse.ArgumentParser(description="Pr Template")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    r = {"tool": "pr-template", "v": "1.0.0", "author": "Jose Zuma"}
    print(json.dumps(r, indent=2) if args.json else f"{name} v1.0.0")
if __name__ == "__main__": main()
