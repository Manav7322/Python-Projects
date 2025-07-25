import PyPDF2
import sys

def add_waterMarker(input_pdf,watermark_pdf,output_pdf):
    with open(input_pdf,'rb') as file:
        reader=PyPDF2.PdfFileReader(file)
        with open(watermark_pdf,'rb') as watermark_file:
            watermark_reader=PyPDF2.PdfFileReader(watermark_file)
            watermark_page=watermark_reader.getPage(0)

            writer=PyPDF2.PdfFileWriter()

            for page_num in range(reader.getNumPages()):
                page=reader.getPage(page_num)
                page.mergePage(watermark_page)
                writer.addPage(page)

            with open(output_pdf,'wb') as output_file:
                writer.write(output_file)
add_waterMarker("super.pdf","wtr.pdf","output _watermarked.pdf")
