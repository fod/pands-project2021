# analysis_util.py
# Useful functions for analysing Fisher's Iris Dataset
# Author: Fiachra O' Donoghue

import fileinput
import re

def insert_text(filename, content):

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