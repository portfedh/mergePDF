from PyPDF2 import PdfFileReader, PdfFileWriter


class MergePDF():

    def __init__(self):
        self.odd = 'odd.pdf'
        self.even = 'even.pdf'
        self.merged = 'merged.pdf'
        self.open_files()
        self.check_pages()
        if self.check is True:
            self.merge_files()
            print('Finished successfully.')

    def open_files(self):
        self.odd_file = PdfFileReader(open(self.odd, 'rb'))
        self.even_file = PdfFileReader(open(self.even, 'rb'))
        self.odd_pages = self.odd_file.getNumPages()
        self.even_pages = self.even_file.getNumPages()

    def check_pages(self):
        if self.odd_pages == self.even_pages:
            self.check = True
            print("Odd pages are equal to even pages: executing merge.")
        else:
            self.check = False
            print("Odd pages are not equal to even pages: aborting.")

    def merge_files(self):
        self.merge = PdfFileWriter()
        for x in range(self.odd_pages):
            self.merge.addPage(self.odd_file.getPage(x))
            self.merge.addPage(self.even_file.getPage(x))
        self.merge.write(open(self.merged, 'wb'))
        print('Documents merged successfully.')


if __name__ == '__main__':
    oMerge = MergePDF()
