import os


prefix = os.getenv("BOLERO2_GITHUB_IO_INDEX_HTML_PREFIX")
repo = os.getenv("BOLERO2_REPOSITORY")

string = """---
title: bolero2.log
subtitle: AI Engineer's Archives
layout: page
callouts: home_callouts
show_sidebar: true
---
"""

print("PREFIX :", prefix)
print("REPOSITORY :", repo)
print("String :", string)

pwd = os.getcwd()

with open(os.path.join(pwd, "prefix.md"), 'w') as f:
    f.write(string)
