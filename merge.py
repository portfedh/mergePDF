from PyPDF2 import PdfReader, PdfWriter

class MergePDF:

    def __init__(self):
        self.odd = 'odd.pdf'
        self.even = 'even.pdf'
        self.merged = 'merged.pdf'
        self.open_files()
        self.check_pages()
        if self.check:
            self.merge_files()
            print('Finished successfully.')

    def open_files(self):
        self.odd_file = PdfReader(self.odd)
        self.even_file = PdfReader(self.even)
        self.odd_pages = len(self.odd_file.pages)
        self.even_pages = len(self.even_file.pages)

    def check_pages(self):
        if self.odd_pages == self.even_pages:
            self.check = True
            print("Odd pages are equal to even pages: executing merge.")
        else:
            self.check = False
            print("Odd pages are not equal to even pages: aborting.")

    def merge_files(self):
        self.merge = PdfWriter()
        for x in range(self.odd_pages):
            self.merge.add_page(self.odd_file.pages[x])
            self.merge.add_page(self.even_file.pages[x])
        with open(self.merged, 'wb') as f_out:
            self.merge.write(f_out)
        print('Documents merged successfully.')

if __name__ == '__main__':
    oMerge = MergePDF()