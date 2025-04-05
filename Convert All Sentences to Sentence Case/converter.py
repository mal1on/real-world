"""Convert all sentences in a text file to sentence case."""

import os


def converter(input_file, output_file):
    """Convert all sentences in a text file to sentence case.

    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output text file.
    """
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Split sentences and capitalize
        fixed = '. '.join([s.strip().capitalize() for s in text.split('.')])

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(fixed)

        print(f"Converted text has been saved to '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    input_path = r'tmp\snowwhite.txt'
    output_path = r'tmp\snowwhite_edited.txt'

    # Confirm before overwriting the output file
    if os.path.exists(output_path):
        confirm = input(f"The file '{output_path}' already exists. Overwrite? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Operation canceled.")
        else:
            converter(input_path, output_path)
    else:
        converter(input_path, output_path)
