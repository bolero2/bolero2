import os


prefix = os.getenv("BOLERO2_GITHUB_IO_INDEX_HTML_PREFIX")
repo = os.getenv("BOLERO2_REPOSITORY")


print("PREFIX :", prefix)
print("REPOSITORY :", repo)

pwd = os.getcwd()

with open(os.path.join(pwd, "prefix.md"), 'w') as f:
    f.write(prefix)
