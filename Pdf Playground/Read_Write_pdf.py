import PyPDF2
with open('twopage.pdf','rb') as file:
    reader=PyPDF2.PdfFileReader(file)
    page=reader.getPage(0)
    page.rotateCounterClockwise(90)
    print(reader.getPage(0))
    writer=PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf','wb')as newfile:
        writer.write(newfile)
