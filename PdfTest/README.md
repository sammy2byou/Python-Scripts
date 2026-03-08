# PDF Directory

This Read Me is to explain each script and how to use it.

## ZipperPdfs.py

The purpose of this is to "zipper" 2 pdf files together. Reason for this is to cut down on tedious reparative tasks at work. For instance 2 reports are run, and I need to have invoice, then corresponding timesheet, then next invoice and so on. This can be done manually with Adobe Pro, and the "combine" feature, but you have to drag and drop each page to the correct location. That can take about 1-10min depending on how many pages I need to do.

Downside of this at the moment. A timesheet is not always generated. So I'd have to check the 2nd pdf to make sure that there is a blank page, where the timesheet would be, otherwise the order would be incorrect.

#### How to Run:

Have [python](https://www.python.org/downloads/) and [PyPDF2](https://pypi.org/project/PyPDF2/) installed.

Using CMDB, path to the script's location.

Then using the following code to run:

```

py ZipperPdfs.py

```

It will ask for the first file (my invoice file), then the 2nd file (my timesheet file), then where and what you would like to name the merged file.

If there are odd pages, it will add the remaining pages to the end of the merged pdf file.

