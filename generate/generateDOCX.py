import docx
from system import utils as u

def makeDoc(name,txt):
    doc = docx.Document()
    doc.add_paragraph(txt)
    doc.save(u.dt_string+"/docs_chunks/"f'{name}.docx')    