# Screening Eagle Downloads.
Code to compile and format raw GPR data as downloaded from <a href="https://www.screeningeagle.com/">Screening Eagle</a>. 
Data is downloaded in .zip files, with structure:

. <br>
├── ZIPFILE_Name <br>
│  ├── Sub Folder<br>
│  │   ├── Data<br>
│  │   └── Data<br>
│  ├── Sub Folder<br>
│  │   ├── Data<br>
│  │   └── Data<br>
│  ├── Sub Folder<br>
│  │   ├── Data<br>
│  │   └── Data<br>
└──<br>

This code compiles multiple .zipfiles and extracts only the Sub Folders, and corresponding Data, into a seperate folder.


To install a virtual environment for the code:
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    python -m venv unzipper
</head>

To activate the virtual environment:
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    .\unzipper\Scripts\activate
</head>

Most of the modules needed to run this are in-built with Python, however <a href="https://github.com/tqdm/tqdm">tqdm</a> provides a nice progress bar.

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    pip install tqdm
</head>
