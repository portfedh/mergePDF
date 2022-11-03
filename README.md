# Merging Odd and Even pages in a PDF

![MergePDF](https://pablocruz.io/wp-content/uploads/2022/08/Merge.png)

If you want to merge two pdf’s by alternating their pages, you can use this python script to automate the process.

You can find a more in depth explanation of the script in [this](https://pablocruz.io/merge-pdf-alternating-pages/) blog post.

## What the script does

The script creates a merged pdf from two files named ‘odd.pdf’ and ‘even.pdf’, alternating the pages.

## Requirements

The script requires the PyPDF2 library, which can be found here, and installed using:

`pip install PyPDF2`

## How to use

- Scan the odd pages and save the pdf file as ‘odd.pdf’.
- Do the same with the even pages and save the file as ‘even.pdf’.
- Make sure the number of pages in both files is the same.
- Move both documents to the same directory as ‘merge.py’.
- Run the python script
- The script will combine both pdf’s, alternating the pages and save the file as ‘merged.pdf’.
