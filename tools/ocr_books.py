"""Local OCR of scanned PDF books -> page-delimited text file.
No network / API calls. Uses PyMuPDF (fitz) to rasterize + tesseract to OCR.
Usage: python tools/ocr_books.py "<pdf_path>" "<out_txt_path>" [dpi]
"""
import sys, os
from concurrent.futures import ProcessPoolExecutor, as_completed
import fitz
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

PDF = sys.argv[1]
OUT = sys.argv[2]
DPI = int(sys.argv[3]) if len(sys.argv) > 3 else 300


def ocr_page(args):
    pdf, i, dpi = args
    try:
        doc = fitz.open(pdf)
        page = doc.load_page(i)
        # try embedded text first (cheap); fall back to OCR
        txt = page.get_text() or ""
        if len(txt.strip()) < 40:
            pix = page.get_pixmap(dpi=dpi)
            img = Image.open(io.BytesIO(pix.tobytes("png")))
            txt = pytesseract.image_to_string(img, lang="eng")
        doc.close()
        return i, txt
    except Exception as e:
        return i, f"[OCR-ERROR pg {i}: {e}]"


def main():
    doc = fitz.open(PDF)
    n = doc.page_count
    doc.close()
    print(f"OCR {os.path.basename(PDF)} : {n} pages @ {DPI}dpi", flush=True)
    results = {}
    tasks = [(PDF, i, DPI) for i in range(n)]
    done = 0
    with ProcessPoolExecutor(max_workers=10) as ex:
        futs = [ex.submit(ocr_page, t) for t in tasks]
        for f in as_completed(futs):
            i, txt = f.result()
            results[i] = txt
            done += 1
            if done % 20 == 0:
                print(f"  ...{done}/{n}", flush=True)
    with open(OUT, "w", encoding="utf-8") as o:
        for i in range(n):
            o.write(f"\n===== PAGE {i+1} =====\n")
            o.write(results.get(i, ""))
    print(f"DONE -> {OUT} ({os.path.getsize(OUT)} bytes)", flush=True)


if __name__ == "__main__":
    main()
