"""
In-memory PDF certificate generator using ReportLab.
"""
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_esg_pdf(company_name: str, impact_metrics: dict) -> bytes:
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    c.setFont("Helvetica-Bold", 18)
    c.drawString(80, 720, "ESG Environmental & Social Impact Certificate")
    
    c.setFont("Helvetica", 12)
    c.drawString(80, 680, f"Issued to: {company_name}")
    c.drawString(80, 650, f"• E-Waste Diverted: {impact_metrics['ewaste_kg']} kg")
    c.drawString(80, 630, f"• Scope 3 Carbon Offset: {impact_metrics['co2_saved_kg']} kg CO2e")
    c.drawString(80, 610, f"• Refurbished Devices Donated: {impact_metrics['digital_access_units']} units")
    
    c.showPage()
    c.save()
    
    buffer.seek(0)
    return buffer.getvalue()