# ==============================================================================
# SCRIPT TO BUILD COMPLETE CONSOLIDATED REPORT IN MICROSOFT WORD (.DOCX)
# RAMAIAH INSTITUTE OF TECHNOLOGY - CSE (AI & ML) - BIG DATA SYSTEMS (24CI51)
# STUDENT: JOEL B JOHN | USN: 1MS24CI060
# ==============================================================================

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

SS_DIR = r"c:\Users\JOEL\OneDrive\Desktop\big_data\ss"
CHART_IMG = r"c:\Users\JOEL\OneDrive\Desktop\big_data\activity_5_cloud_real\cloud_log_analytics_060.png"
OUTPUT_DOCX = r"c:\Users\JOEL\OneDrive\Desktop\big_data\final_report\FINAL_BIG_DATA_REPORT_1MS24CI060.docx"

def set_cell_background(cell, fill_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_styled_heading(doc, text, level):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.bold = True
    
    if level == 1:
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        run.font.size = Pt(16)
        run.font.color.rgb = RGBColor(0, 32, 96) # Deep Navy
    elif level == 2:
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        run.font.size = Pt(13)
        run.font.color.rgb = RGBColor(31, 78, 121) # Slate Blue
    elif level == 3:
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(60, 60, 60) # Charcoal
    return p

def add_body_p(doc, text, bold_prefix=None, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.size = Pt(10)
        r_pre.font.name = "Calibri"
    r = p.add_run(text)
    r.font.size = Pt(10)
    r.font.name = "Calibri"
    return p

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F2F2F2")
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(code_text)
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(30, 30, 30)

def add_figure_image(doc, img_name, fig_num, caption, width=Inches(6.0)):
    img_path = os.path.join(SS_DIR, img_name)
    if not os.path.exists(img_path):
        if img_name == "cloud_log_analytics_060.png" and os.path.exists(CHART_IMG):
            img_path = CHART_IMG
        else:
            print(f"Warning: image {img_name} not found at {img_path}")
            return
    
    # Add image
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(8)
    p_img.paragraph_format.space_after = Pt(2)
    run_img = p_img.add_run()
    run_img.add_picture(img_path, width=width)
    
    # Add caption
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(10)
    
    r_lbl = p_cap.add_run(f"Figure {fig_num}: ")
    r_lbl.bold = True
    r_lbl.font.size = Pt(9)
    r_lbl.font.color.rgb = RGBColor(0, 32, 96)
    
    r_cap = p_cap.add_run(caption)
    r_cap.italic = True
    r_cap.font.size = Pt(9)
    r_cap.font.color.rgb = RGBColor(50, 50, 50)

print("Base setup ready.")
