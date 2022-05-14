name: Readme Updater 
on:
  push:
    branches:
      - "main"

jobs:
  build:
    env:
      NEURALWORKS_MODEL_STORAGE: /home/runner/work/bolero2/bolero2
      AUTHOR: bolero2 README.md main branch
      PROJECT: bolero2 README.md update
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - name: Set up Python 3.7
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python }}
      - name: "git clone bolero2.github.io"
        run: |
          git clone https://github.com/bolero2/bolero2.github.io.git
     
      - name: "Copy bolero2/README.md > bolero2.github.io/docs/index.md"
        env: 
          PREFIX: ${{ secrets.BOLERO2_GITHUB_IO_INDEX_HTML_PREFIX }}
        run: |
          pwd
     