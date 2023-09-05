from unstructured.partition.auto import partition

elements = partition("db/Print Screen CRIO_commentaires à discuter.docx")
print("start!")
for element in elements[0:100]:
    if element.category != "PageBreak":
        print(str(element))
        print(element.metadata.filetype)
        print(element.metadata.page_location)
        print(element.category)
        print("================================")
# elements = partition("db/page_6.png", skip_infer_table_types=[], pdf_infer_table_structure=True, strategy="ocr_only")
# print("start!")
# for element in elements[0:50]:
#     if element.category != "PageBreak":
#         print(str(element))
#         print(element.metadata.filetype)
#         print(element.metadata.page_location)
#         print(element.category)
#         print("================================")
