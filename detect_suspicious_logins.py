#!/usr/bin/env python3
"""Basic defensive detector for suspicious SSH authentication activity."""

import argparse
import re
from collections import Counter

FAILED = re.compile(
    r"Failed password for (?:invalid user )?\S+ from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)
SUCCESS = re.compile(
    r"Accepted (?:password|publickey) for \S+ from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)

def analyse(path):
    failed, successful = Counter(), Counter()
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            m = FAILED.search(line)
            if m:
                failed[m.group("ip")] += 1
                continue
            m = SUCCESS.search(line)
            if m:
                successful[m.group("ip")] += 1
    return failed, successful

def main():
    parser = argparse.ArgumentParser(description="Detect repeated SSH login failures.")
    parser.add_argument("logfile")
    parser.add_argument("--threshold", type=int, default=5)
    args = parser.parse_args()

    failed, successful = analyse(args.logfile)

    print("=== Suspicious Login Log Analysis ===")
    print(f"Total failed login attempts: {sum(failed.values())}")
    print(f"Total successful login attempts: {sum(successful.values())}")
    print("\nFailed attempts by source:")
    for ip, count in failed.most_common():
        status = "HIGH ALERT" if count >= args.threshold else "Review"
        print(f"  {ip}: {count} -> {status}")

    print("\nSuccessful logins by source:")
    for ip, count in successful.most_common():
        print(f"  {ip}: {count}")

if __name__ == "__main__":
    main()
