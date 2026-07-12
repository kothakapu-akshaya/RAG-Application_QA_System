import pymupdf4llm


def extract_text(pdf_path: str) -> str:
    """
    Extract text from a PDF using PyMuPDF4LLM.
    """
    markdown = pymupdf4llm.to_markdown(pdf_path)
    return markdown
