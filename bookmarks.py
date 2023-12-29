import fitz  # PyMuPDF
import os


def find_bookmarks(pdf_path):
    pdf_document = fitz.open(pdf_path)
    bookmarks = []
    toc = pdf_document.get_toc()
    for page_num in range(len(toc)):
        page = toc[page_num]
        if page[0] == 2:
            bookmarks.append({"page": page[2], "bookmark": page[1]})
    pdf_document.close()
    return bookmarks


def splice_pdf(pdf_path, bookmarks):
    pdf1 = fitz.open(pdf_path)
    file_base_name = os.path.basename(pdf_path)
    outputFileName = os.path.splitext(file_base_name)[0]
    page_count = pdf1.page_count
    last_slash_index = pdf_path.rfind("/")
    outputPath = pdf_path[:last_slash_index]
    # 要创建的新文件夹的路径
    new_folder_path = outputPath + '/' + outputFileName
    # 使用os.mkdir创建新文件夹
    try:
        os.mkdir(new_folder_path)
    except OSError as error:
        print('無法建立')
    for page_num in range(len(bookmarks)):
        pdf2 = fitz.open()
        if (page_num < len(bookmarks)-1):
            start = bookmarks[page_num]['page']-1
            end = bookmarks[page_num+1]['page']-2
            # print('start:' + str(start))
            # print('end:' + str(end))
            pdf2.insert_pdf(pdf1, from_page=start, to_page=end)

        else:
            start = bookmarks[page_num]['page']-1
            end = page_count-1
            # print('start:' + str(start))
            # print('end:' + str(end))
            pdf2.insert_pdf(pdf1, from_page=start, to_page=end)
        pdf2.save(outputPath + '/' + outputFileName + '/' +
                  bookmarks[page_num]['bookmark']+'.pdf')
        pdf2.close()
    pdf1.close()


def run(pdf_path):
    bookmarks = find_bookmarks(pdf_path)
    splice_pdf(pdf_path, bookmarks)
