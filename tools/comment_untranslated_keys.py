#!/usr/bin/env python3
"""
Author: DartRuffian

Comments on a GitHub PR for missing translations
"""

import os
import sys
import traceback
import subprocess as sp
from github import Github, Auth


def update_translations(repo,pr_number):
    diag = sp.check_output(
        ["python3", "tools/translation_progress.py", "--markdown"])
    diag = str(diag, "utf-8")
    pr = repo.get_pull(pr_number)
    pr.create_issue_comment(body=diag)


def main():
    print("Obtaining environment variables ...")
    try:
        token = os.environ["GITHUB_TOKEN"]
        repository = os.environ["REPOSITORY"]
        pr_number = os.environ["PR_NUMBER"]
        auth = Auth.Token(token)
        repo = Github(auth=auth).get_repo(repository)
    except:
        print("Could not obtain vars.")
        print(traceback.format_exc())
        return 1
    else:
        print("Sucessfully obtained environment variables.")

    print("\nUpdating translation issue ...")
    try:
        update_translations(repo,pr_number)
    except:
        print("Failed to update translation issue.")
        print(traceback.format_exc())
        return 1
    else:
        print("Successfull commented on pull request.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
