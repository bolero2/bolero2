import os


prefix = os.getenv("BOLERO2_GITHUB_IO_INDEX_HTML_PREFIX")
repo = os.getenv("BOLERO2_REPOSITORY")


print(prefix)
print(repo)


string = """
---
title: bolero2.log
subtitle: AI Engineer's Archives
layout: page
callouts: home_callouts
show_sidebar: true
---
"""
print(string)
