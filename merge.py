from PyPDF2 import PdfReader, PdfWriter

class MergePDF:

    def __init__(self):
        self.merged = 'merged.pdf'
        self.get_user_choice()

        if self.merge_mode == "interleave":
            self.odd = 'odd.pdf'
            self.even = 'even.pdf'
            self.open_odd_even()
            self.check_pages()
            if self.check:
                self.merge_interleave()
        elif self.merge_mode == "append":
            self.original = 'original.pdf'
            self.appendix = 'append.pdf'
            self.open_append_files()
            self.merge_append()
        else:
            print("Invalid mode selected. Exiting.")

    def get_user_choice(self):
        print("PDF Merge Tool")
        print("==============")
        print("I: Interleave odd/even pages (needs 'odd.pdf' and 'even.pdf')")
        print("M: Append one PDF to another (needs 'original.pdf' and 'append.pdf')")
        choice = input("Enter your choice (I/M): ").strip().upper()

        if choice == "I":
            self.merge_mode = "interleave"
        elif choice == "M":
            self.merge_mode = "append"
        else:
            print("Invalid selection. Please enter 'I' or 'M'.")
            exit(1)

    def open_odd_even(self):
        self.odd_file = PdfReader(self.odd)
        self.even_file = PdfReader(self.even)
        self.odd_pages = len(self.odd_file.pages)
        self.even_pages = len(self.even_file.pages)

    def open_append_files(self):
        self.original_file = PdfReader(self.original)
        self.append_file = PdfReader(self.appendix)

    def check_pages(self):
        if self.odd_pages == self.even_pages:
            self.check = True
            print("Odd and even page counts match. Proceeding with interleave.")
        else:
            self.check = False
            print("Page counts do not match. Cannot interleave.")

    def merge_interleave(self):
        merger = PdfWriter()
        for x in range(self.odd_pages):
            merger.add_page(self.odd_file.pages[x])
            merger.add_page(self.even_file.pages[x])
        with open(self.merged, 'wb') as f_out:
            merger.write(f_out)
        print("Interleaved merge completed successfully.")

    def merge_append(self):
        merger = PdfWriter()
        for page in self.original_file.pages:
            merger.add_page(page)
        for page in self.append_file.pages:
            merger.add_page(page)
        with open(self.merged, 'wb') as f_out:
            merger.write(f_out)
        print("Append merge completed successfully.")

if __name__ == '__main__':
    oMerge = MergePDF()