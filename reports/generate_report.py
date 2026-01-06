from reportlab.platypus import SimpleDocTemplate, Paragraph

def generate_report(data):
    doc = SimpleDocTemplate("credit_ai_audit.pdf")
    content = []
    content.append(Paragraph("Credit AI Compliance Report"))
    content.append(Paragraph(str(data)))
    doc.build(content)
