import fitz

fnPdfIn, fnPdfOut = 'blank.pdf', 'out.pdf'

doc2 = fitz.open()
pdfIn = fitz.open(fnPdfIn)
doc2.insertPDF(pdfIn)

for idxPage in range(len(doc2)):
    page = doc2[idxPage]
    _, _, wid, hi = page.MediaBox

    text =  'page %i' % (idxPage+1)

    # method 1: insertText
    #~ where = fitz.Point(wid*0.5, hi-10)
    #~ page.insertText(where, text, fontsize=fontsize, )

    # method 2: insertTextbox
    rect = fitz.Rect(
        wid/2-fontsize*len(text)/2, hi/2-fontsize/2,
        wid/2+fontsize*len(text)/2, hi/2+fontsize/2
    )
    page.drawRect(rect, color = (0.5, 0.5, 0.5), overlay=True)
    page.insertTextbox(rect, text, fontsize=fontsize)

doc2.save(fnPdfOut)
doc2.close()


