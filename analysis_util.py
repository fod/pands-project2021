# analysis_util.py
# Useful functions for analysing Fisher's Iris Dataset
# Author: Fiachra O' Donoghue

import fileinput
import re
import pandas as pd
import sys


"""
This file contains some functions that are both reusable in other projects
and tangential to the main business of anlysing the Fisher's iris data set.
"""

def insert_text(filename, content):
    """A simple templating system for updating text files. Intended mainly for inserting 
    dynamically generated tables and text into Github README.md files.

       The target text file should contain labels in the form '{% LABEL %}' and '{% END %}' 
       wherever it is intended that dynamically generated content will be inserted. 
       The insert_text() function scans the passed file for labels and when one is encountered 
       the passed dictionary is searched for a key matching the label. If the label exists the 
       value for that label is inserted into the document. If content already exists between the 
       {% LABEL %} and {% END %} it is removed.

       The labels are not replaced but remain in the target document so that dynamically 
       generated content can be updated whenever necessary. As such, it is recommended that the 
       tags be placed in comments so as not to be visible in the rendered document. In the case 
       of Github README.md files, written in Github Markdown, html comments are suggested, e.g.:

                            `<!-- {% TABLE_1 %} -->
                            ...
                            <!-- {% END %} -->`

    Args:
        filename (str): The full path to the file to be updated
        content (dict): A dictionary of labels matching the templating labels in the target file, 
        and content to be inserted
    """

    try:
        # fileinput.input(inplace=True) creates a line by line copy of the original then uses it 
        # to replace the original. As the new file is being built up lines can be omitted or added
        with fileinput.input(files=filename, inplace=True) as f:

            # Flag indicating that we are between a LABEL tag and an END tag
            del_old_lines = False
            for line in f:

                # If we are between a LABEL and an END tag, see if we've reached the END tag and if not 
                # carry on to the next line discarding the current one
                if del_old_lines:
                    if re.search(r"{%\s*END\s*%}", line):
                        del_old_lines = False
                        print("\n" + line, end="")                  
                    continue

                # Match the LABEL markers ('{%' and '%}') and capture the text inside them
                match = re.search(r"{%(.*)%}", line)    # https://docs.python.org/3/howto/regex.html

                # If a LABEL is found and that label exists in the content dict then keep the LABEL line
                # and insert the relevant text from the content dict
                if match and match.group(1).strip() in content:
                    print(line)
                    print(content[match.group(1).strip()])

                    # All lines from here to the END tag are old content and should be removed 
                    # so del_old_lines flag is activated
                    del_old_lines = True

                # If no LABEL is found or a LABEL is found but there is not content for it in the content dict
                # keep the current line and carry on    
                else:
                    print(line, end="")

    except IOError as e:
        print(f"File error: {e}: README.md must exist in the project root.")
        sys.exit()


def csv_to_df(filename, colnames):
# Load csv data into pandas dataframe and name the columns; return the dataframe
# Really just a call to pandas.read_csv with exception catching but placed in a 
# function to make future changes easier

    try:
        df = pd.read_csv(filename, names=colnames)

    except IOError as e:
        print(f"File error: {e}")
        sys.exit()

    return df


def df_to_csv(filename, df):
# Write out a csv representation of a dataframe -- convenience function

    try:
        with open(filename, "w+") as f:
            f.write(df.to_csv())

    except IOError as e:
        print(f"File error: {e}")
        

