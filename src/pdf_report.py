from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(results):
    doc = SimpleDocTemplate(
        "reports/credit_ai_compliance_report.pdf",
        pagesize=LETTER
    )
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("Credit AI Compliance Report", styles["Title"]))

    for k, v in results.items():
        content.append(Paragraph(f"<b>{k}</b>: {v}", styles["Normal"]))

    doc.build(content)
