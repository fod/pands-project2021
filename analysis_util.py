# analysis_util.py
# Useful functions for analysing Fisher's Iris Dataset
# Author: Fiachra O' Donoghue

import fileinput
import re

def insert_text(filename, content):
    """A simple templating system for updating text files. Intended mainly for inserting dynamically 
       generated tables and text into Github README.md files.

       The target text file should contain labels in the form '{% LABEL %}' and '{% END %}' wherever it
       is intended that dynamically generated content will be inserted. The insert_text() function scans
       the passed file for labels and when one is encountered the passed dictionary is searched for a key
       matching the label. If the label exists the value for that label is inserted into the document. If 
       content already exists between the {% LABEL %} and {% END %} it is removed.

       The labels are not replaced but remain in the target document so that dynamically generated content
       can be updated whenever necessary. As such, it is recommended that the tags be placed in comments so
       as not to be visible in the rendered document. In the case of Github README.md files, written in Github
       Markdown, html comments are suggested, e.g.:

                            `<!-- {% TABLE_1 %} -->
                            ...
                            <!-- {% END %} -->`

    Args:
        filename (str): The full path to the file to be updated
        content (dict): A dictionary of labels matching the templating labels in the target file, and content
                        to be inserted
    """

    try:
        with fileinput.input(files=filename, inplace=True) as f:

            del_old_lines = False
            for line in f:

                if del_old_lines:
                    if re.search(r"{%\s*END\s*%}", line):
                        del_old_lines = False
                        print(line, end="")                  
                    continue

                match = re.search(r"{%(.*)%}", line)    # https://docs.python.org/3/howto/regex.html


                if match and match.group(1).strip() in content:
                    print(line)
                    print(content[match.group(1).strip()])
                    del_old_lines = True
                else:
                    print(line, end="")

    except IOError as e:
        print(f"File error: {e}")
 
#full_summary.to_markdown(tablefmt="github")