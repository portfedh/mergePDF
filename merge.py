# -*- coding: UTF-8 -*-
from PyPDF2 import PdfFileReader, PdfFileWriter


def merge_odd_even(odd, even, output_file):
    """
    Return a merged pdf from two pdfs.

    Parameters:
        odd:
            - pdf filename with odd pages in descending order.
        even:
            - pdf filename with even pages in descending order.
    Returns:
        output_file:
            - pdf filename with merged pdf.
    """
    pdf_output = PdfFileWriter()
    odd_input = PdfFileReader(open(odd, 'rb'))
    even_input = PdfFileReader(open(even, 'rb'))
    odd_pages = odd_input.getNumPages()
    even_pages = even_input.getNumPages()
    num_pages = odd_pages * 2
    if odd_pages == even_pages:
        print(f'The number of pages is {num_pages}.')
        for i in range(odd_pages):
            pdf_output.addPage(odd_input.getPage(i))
            pdf_output.addPage(even_input.getPage(i))
        pdf_output.write(open(output_file, 'wb'))
        print('Documents merged successfully.')
    else:
        print('Check page number: Odd pages unequal to even pages')


if __name__ == '__main__':
    odd = 'odd.pdf'
    even = 'even.pdf'
    filename = input(
        'Input the file name for the merged document (without .pdf): ')
    output_file = filename + '.pdf'
    merge_odd_even(odd, even, output_file)
