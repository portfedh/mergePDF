# Merging Odd and Even pages in a PDF

![MergePDF](https://pablocruz.io/wp-content/uploads/2022/08/Merge.png)

If you want to merge two pdf’s by alternating their pages, you can use this simple script.

## What it does

The script creates a merged pdf from two files named ‘odd.pdf’ and ‘even.pdf’, alternating the pages.

## How to Install

The script requires the fpdf2 library, which can be found here, and installed using:

`pip install fpdf2`

## How to Use

- Scan the odd pages and save the pdf file as ‘odd.pdf’.
- Do the same with the even pages and save the file as ‘even.pdf’.
- Make sure the number of pages in both files is the same.
- Move both documents to the same directory as ‘merge.py’.
- Run the python script
- A terminal prompt will ask for the name of the merged document.
- Write the filename for the merged pdf file.
- The script will combine both pdf’s, alternating the pages and saving the file with the specified name.
