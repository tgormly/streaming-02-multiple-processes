"""
about.py: 

A utility script to display essential debugging information. 
It provides system information, Python details, file paths, and more. 

This provides an overview of the system and configuration.

To use, simply execute this script: `python about.py`
It will print this information to a new file named `about.txt`.

This script does NOT require a virtual environment.
It uses ONLY modules found in the Python standard library.

Author: Denise Case
"""

# Import from Python Standard Library

import datetime
import os
import platform
import sys

# Declare program constants

DIVIDER = "=" * 70  # A string divider for cleaner output formatting
OUTPUT_FILENAME = "about.txt"  # File name for saving the debug information

# Retrieve additional system information using platform and os modules

build_date, compiler = platform.python_build()
implementation = platform.python_implementation()
architecture = platform.architecture()[0]
user_home = os.path.expanduser("~")

# Define program functions (bits of reusable code)


def get_source_directory_path():
    """
    Returns the absolute path to the directory containing this script.
    """
    dir = os.path.dirname(os.path.abspath(__file__))
    return dir


def print_info_to_file(filename, content):
    """
    Print the provided content to a specified file.

    Args:
    - filename (str): Name of the file to save the content in.
    - content (str): The content to save.
    """
    with open(filename, "w") as f:
        f.write(content)


def get_header(fn):
    """
    Constructs a formatted string that provides helpful information.

    Args:
    - fn (str): Path to the file for which the information should be generated.

    Returns:
    - str: Formatted debug information.
    """
    return f"""
{DIVIDER}
{DIVIDER}
 Welcome to the Python Debugging Information Utility for NW 44-671!
 Date and Time: {datetime.date.today()} at {datetime.datetime.now().strftime("%I:%M %p")}
 Operating System: {os.name} {platform.system()} {platform.release()}
 System Architecture: {architecture}
 Number of CPUs: {os.cpu_count()}
 Machine Type: {platform.machine()}
 Python Version: {platform.python_version()}
 Python Build Date and Compiler: {build_date} with {compiler}
 Python Implementation: {implementation}
 Active pip environment: {os.environ.get('PIP_DEFAULT_ENV', 'None')}
 Path to Interpreter:         {sys.executable}
 Path to virtual environment: {sys.prefix}
 Current Working Directory:   {os.getcwd()}
 Path to source directory:    {get_source_directory_path()}
 Path to script file:         {fn}
 User's Home Directory:       {user_home}
{DIVIDER}
{DIVIDER}
"""


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # We are using the get_header function and providing it with the path to this script.
    # This will generate the debug information for the current script.
    debug_info = get_header(__file__)

    # Print the debug information to the console.
    print(debug_info)

    # Print the debug information to a file named by the value in OUTPUT_FILENAME.
    print_info_to_file(OUTPUT_FILENAME, debug_info)
