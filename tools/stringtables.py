#!/usr/bin/env python3
"""
Author: DartRuffian

Various stringtable related functions
"""

# import sys
import os
import xml.dom
import xml.dom.minidom


class Stringtables:
    @staticmethod
    def supported_languages() -> list[str]:
        # https://community.bistudio.com/wiki/Stringtable.xml#Supported_Languages
        return [
            "English",
            "Czech",
            "French",
            "Spanish",
            "Italian",
            "Polish",
            "Portuguese",
            "Russian",
            "German",
            "Korean",
            "Japanese",
            "Chinese",
            "Chinesesimp",
            "Turkish",
            "Slovak",
            "Ukrainian",
            "Latin",
            "Bulgarian",
            "Hungarian"
        ]

    @staticmethod
    def is_language_supported(language: str) -> bool:
        """Determines if a given language is supported by Arma 3"""
        return language in Stringtables.supported_languages()

    @staticmethod
    def get_all_languages(project_path: str) -> list[str]:
        """Checks what languages exist in the repo."""
        languages: list[str] = []

        for addon in os.listdir(project_path):
            if addon[0] == ".":
                continue

            stringtable_path = os.path.join(
                project_path, addon, "stringtable.xml")
            try:
                xml_doc: xml.dom.minidom.Document = xml.dom.minidom.parse(
                    stringtable_path)
            except:
                continue

            keys = xml_doc.getElementsByTagName("Key")
            for key in keys:
                for child in key.childNodes:
                    try:
                        if not child.tagName in languages:  # type: ignore
                            languages.append(child.tagName)  # type: ignore
                    except:
                        continue

        return languages


def main() -> None:
    print(
        f"All supported languages:\n{Stringtables.supported_languages()}")
    print(f"All present languages:\n{Stringtables.get_all_languages(".")}")


if __name__ == "__main__":
    main()
