#
from pdf2docx import Converter, parse

pdf_file="y.pdf"
word_File="Bank.docx"
try:
    parse(pdf_file, word_File, start=0, end=None)
    print("File converted successfully");
except:
    print("Not oppening file");

#
# import requests
# import threading
#
# # Number of threads to use for the stress test
# thread_count = 100
#
# # URL of the website to stress test
# url = "https://openai.com/blog/chatgpt/"
#
# def stress_test():
#     while True:
#         # Send a GET request to the website
#         response = requests.get(url)
#         # Print the status code of the response
#         print(response.status_code)
#
# # Create and start the specified number of threads
# for i in range(thread_count):
#     t = threading.Thread(target=stress_test)
#     t.start()
