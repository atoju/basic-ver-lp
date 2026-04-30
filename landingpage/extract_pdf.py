import sys
sys.stdout.reconfigure(encoding='utf-8')
from PyPDF2 import PdfReader

r = PdfReader(r'c:\Users\ysweb\OneDrive\Desktop\landingpage\資料\01_ベーシック版企画書_役員向け初稿.pdf')
for i, p in enumerate(r.pages):
    text = p.extract_text()
    print(f'--- Page {i+1} ---')
    print(text)
    print()
