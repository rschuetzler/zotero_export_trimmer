# Zotero Export Trimmer

A simple utility to take the most useful columns from a Zotero library and trim them down to simpler format. 
All it really does is select a subset of the columns and rename some of them.
I created it to help make a database in Notion mirroring my Zotero database so I can better track my reading, but the same output can be used for anything.

## Usage instructions

1. Put this file into a directory
2. Export your library from Zotero as a CSV, UTF-8 format with BOM, and name it `library.csv`
3. Check the `convert.py` file to make sure the fields selected are the ones you want. I picked the ones I like
4. Run the `convert.py` script. Your trimmed file will be output into `zot.csv`.
5. The time you last ran the script will be saved in `lastrun.txt`. Leave that file there, so that next time you run it, only the new files will be added.

## LICENSE

Copyright 2020 Ryan Schuetzler

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
