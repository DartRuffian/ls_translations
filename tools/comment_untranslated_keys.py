#!/usr/bin/env python3
"""
Author: DartRuffian

Comments on a GitHub PR for missing translations
"""

# import os
import sys
# import traceback
# import subprocess
# import github
from stringtables import Stringtables


# def update_translations(repository: github.Repository.Repository, pr_number: int):
#     pass
# diag = subprocess.check_output(
#     ["python3", "tools/translation_progress.py", "--markdown"])
# diag = str(diag, "utf-8")
# pr = repository.get_pull(pr_number)
# pr.create_issue_comment(body=diag)


def extract_added_languages(git_diff: str) -> list[str]:
    """Takes a git diff and then extracts out newly added languages in the stringtables"""
    diff_lines = git_diff.split("\n")
    added_languages: list[str] = []

    languages = Stringtables.supported_languages()

    for line in diff_lines:
        # Filter out any changes that aren't lines being added (+++ = file additions)
        if not (line.startswith("+ ") and not line.startswith("+++")):
            continue
        line = line[1:].strip()  # Remove "+" and whitespace

        # Extract language name from line, e.g. <Language>Text</Language>
        language = line.split(">")[0][1:]
        if not language in languages:
            continue

        added_languages.append(language)

    return added_languages


def main():
    git_diff: str = sys.stdin.read()
    languages = extract_added_languages(git_diff)
    missing = Stringtables.check_missing_translations(
        ".", "activeCamo", languages)
    print(missing)
    # print("Obtaining environment variables ...")
    # try:
    #     token = os.environ["GITHUB_TOKEN"]
    #     pr_number = int(os.environ["PR_NUMBER"])
    #     auth = github.Auth.Token(token)
    #     repository = github.Github(auth=auth).get_repo(
    #         os.environ["REPOSITORY"])
    # except:
    #     print("Could not obtain vars.")
    #     print(traceback.format_exc())
    #     return 1
    # else:
    #     print("Sucessfully obtained environment variables.")

    # print("\nUpdating translation issue ...")
    # try:
    #     update_translations(repository, pr_number)
    # except:
    #     print("Failed to update translation issue.")
    #     print(traceback.format_exc())
    #     return 1
    # else:
    #     print("Successfull commented on pull request.")

    # return 0


if __name__ == "__main__":
    sys.exit(main())
