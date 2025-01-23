"""
Python script that merges Word documents.
"""

import os
from docx import Document

DIRECTORY = "tmp"


def main():
    """
    Main function.
    """
    if not os.path.exists(DIRECTORY):
        print("Directory does not exist.")
        return
    docs = [
        Document(os.path.join(DIRECTORY, f))
        for f in os.listdir(DIRECTORY)
        if f.endswith(".docx")
    ]
    if not docs:
        print("No documents found.")
        return
    merged = docs[0]
    for doc in docs[1:]:
        merged.add_paragraph("\n")
        for element in doc.element.body:
            merged.element.body.append(element)
    merged.save(os.path.join(DIRECTORY, "merged.docx"))
    print("Documents merged.")


if __name__ == "__main__":
    main()
