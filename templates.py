from jinja2 import Template
from .templatesObj import formTemp,baseTemp,pTemp,blockquoteTemp,tableTemp


def form(entity,entityStyle,method,action="",id="",submitValue="Submit",btnColor="blue"):
    return Template(formTemp).render(entity=entity,entityStyle=entityStyle,method=method,action=action,id=id,submitValue=submitValue,\
            btnColor=btnColor)
def base(body,title="title",headplus=None):
    return Template(baseTemp).render(body=body,title=title,headplus=headplus)
def paragraph(content):
    return Template(pTemp).render(content=content)
def quote(content):
    return Template(blockquoteTemp).render(content=content)
def table(entities,classIs='bordered',attrFilter=None):
    """
    params:
        ----classIs:
            bordered,
            striped,
            highlight,
            centered,
            responsive-table
            ----statements:
                Add class="bordered" to the table tag for a bordered table.
                Add class="striped" to the table tag for a striped table.
                Add class="highlight" to the table tag for a highlight table.
                Add class="centered" to the table tag to center align all the text in the table.
                Add class="responsive-table" to the table tag to make the table 
                    horizontally scrollable on smaller screen widths.
        ----attrFilter: a set contains all the attributes which
                    you do not want to be shown in the tables on pages.
    """
    return Template(tableTemp).render(entities=entities,classIs=classIs,attrFilter=attrFilter)

    
#,color='%s %s'%(color,degree),color='red',degree='accent-2'