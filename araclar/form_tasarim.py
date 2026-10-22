import sys,copy,re
import openpyxl
from openpyxl.styles import PatternFill,Font,Alignment,Border,Side
from openpyxl.drawing.image import Image
from openpyxl.drawing.spreadsheet_drawing import TwoCellAnchor,AnchorMarker
G='006600'; LG='EBF1DE'
GF=PatternFill('solid',fgColor=G); LF=PatternFill('solid',fgColor=LG)
def rgb(c):
    try:
        if c is not None and c.type=='rgb' and isinstance(c.rgb,str): return c.rgb[-6:].upper()
    except Exception: pass
    return None
def fnt(cell,sz=None,bold=None,color=None):
    f=copy.copy(cell.font)
    cell.font=Font(name='Calibri',sz=sz if sz else f.sz,b=f.b if bold is None else bold,i=f.i,color=color if color else f.color)
def anchor(c0,o0,r0,ro0,c1,o1,r1,ro1):
    a=TwoCellAnchor(editAs='oneCell');a._from=AnchorMarker(col=c0,colOff=o0,row=r0,rowOff=ro0);a.to=AnchorMarker(col=c1,colOff=o1,row=r1,rowOff=ro1);return a
def restyle(src,dst,gots=True):
    wb=openpyxl.load_workbook(src);ws=wb.worksheets[0]
    ws._images=[]
    maxc=ws.max_column;maxr=ws.max_row
    # find title cell (row1 merged big block) and meta block (R..T rows1-4)
    title=None
    for r in list(ws.merged_cells.ranges):
        if r.min_row==1 and r.max_row>=4 and r.max_col>=8 and r.min_col>=2: title=r
    TE=title.max_col if title else 17
    tv=None
    if title:
        tv=ws.cell(1,title.min_col).value
    for m in list(ws.merged_cells.ranges):
        if m.min_row<=4 and m.min_col<=TE:
            ws.merged_cells.remove(m)
            for rr in range(m.min_row,m.max_row+1):
                for cc in range(m.min_col,m.max_col+1):
                    if (rr,cc)!=(m.min_row,m.min_col): ws._cells.pop((rr,cc),None)
    else:
        for c in range(1,maxc+1):
            if ws.cell(1,c).value and len(str(ws.cell(1,c).value))>15: tv=ws.cell(1,c).value;break
    # clear row1..4 cols A..Q then rebuild
    for r in range(1,5):
        for c in range(1,TE+1):
            cell=ws.cell(r,c);cell.value=None
    thin=Side(style='thin');med=Side(style='medium')
    ws.merge_cells('D1:%s4'%openpyxl.utils.get_column_letter(TE-2))
    a1=ws['D1'];a1.value=tv
    import math
    dflt=ws.sheet_format.defaultColWidth or 9
    def cw(i):
        d=ws.column_dimensions.get(openpyxl.utils.get_column_letter(i))
        return (d.width if d is not None and d.width else dflt)
    avail=sum(cw(i)*7+5 for i in range(4,TE-1))*0.75*0.97
    lines=str(tv).split('\n') if tv else ['']
    sz=14
    for cand in range(28,13,-1):
        need=sum(max(1,math.ceil(len(x)*0.62*cand/avail)) for x in lines)
        if need*cand*1.25<=90: sz=cand;break
    a1.font=Font(name='Calibri',sz=sz,b=True,color='FFFFFF');a1.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
    for r in range(1,5):
        for c in range(1,maxc+1):
            cell=ws.cell(r,c);cell.fill=GF
            if c<=TE:
                cell.border=Border(left=med if c==1 else None,top=med if r==1 else None)
    for r in range(1,5):
        for c in range(TE+1,maxc+1):
            cell=ws.cell(r,c)
            if cell.value is not None:
                lab=(c<maxc);cell.font=Font(name='Calibri',sz=9 if lab else 10,b=True if (lab or 'FORM' in str(ws.cell(r,TE+1).value)) else False,color='FFFFFF')
                cell.alignment=Alignment(horizontal='left',vertical='center',wrap_text=True)
            cell.fill=GF;cell.border=Border(left=thin,right=thin,top=thin,bottom=thin)
    # rest of sheet
    for r in range(5,maxr+1):
        for c in range(1,maxc+1):
            cell=ws.cell(r,c);fl=rgb(cell.fill.fgColor) if cell.fill.fill_type=='solid' else None
            v=cell.value
            if fl in ('2E3135','2F3237','1F2933','212529') or (fl and fl<'404040' and fl!='FFFFFF'):
                cell.fill=GF;cell.font=Font(name='Calibri',sz=11,b=True,color='FFFFFF');cell.alignment=Alignment(horizontal='left',vertical='center',wrap_text=True)
            elif fl in ('E8EBF0','F6F7F9','EEF0F4','F1F3F6','F3F4F6','E5E7EB','EDEFF3'):
                cell.fill=LF;b=cell.font.b
                cell.font=Font(name='Calibri',sz=11 if (b or v) else cell.font.sz,b=True if b else False,color='000000')
                if v is not None and cell.alignment.horizontal is None: cell.alignment=Alignment(horizontal='left',vertical='top',wrap_text=True)
    # imza başlıkları (altındaki satırda 'Name - Signature' yazan hücreler) yeşil / signature headers green
    for r in range(5,maxr):
        for c in range(1,maxc+1):
            nv=ws.cell(r+1,c).value
            if isinstance(nv,str) and nv.startswith('Name - Signature') and ws.cell(r,c).value:
                cell=ws.cell(r,c);cell.fill=GF;cell.font=Font(name='Calibri',sz=11,b=True,color='FFFFFF');cell.alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
                for m in ws.merged_cells.ranges:
                    if m.min_row==r and m.min_col==c:
                        for cc in range(m.min_col,m.max_col+1): ws.cell(r,cc).fill=GF
    # retention / last text rows: green bar
    last=maxr
    for r in range(maxr,maxr-4,-1):
        v=ws.cell(r,1).value
        if isinstance(v,str) and v.startswith('Retention'): last=r;break
    rng=[m for m in ws.merged_cells.ranges if m.min_row==last and m.min_col==1]
    if rng:
        c=ws.cell(last,1);c.fill=GF;c.font=Font(name='Calibri',sz=11,b=True,color='FFFFFF');c.alignment=Alignment(horizontal='left',vertical='center',wrap_text=True)
        for cc in range(1,maxc+1): ws.cell(last,cc).fill=GF
        ws.row_dimensions[last].height=32
    # data rows font 10
    # logos
    for path,anc in (('araclar/ems_white.png',anchor(0,238124,0,198193,2,171449,3,205802)),):
        im=Image(path);im.anchor=anc;ws.add_image(im)
    if gots:
        im=Image('araclar/gots.png');im.anchor=anchor(TE-2,66676,0,28575,TE-1,609600,3,283176);ws.add_image(im)
    ws.page_setup.orientation='landscape';ws.page_setup.paperSize=9;ws.sheet_properties.pageSetUpPr.fitToPage=True;ws.page_setup.fitToHeight=0
    wb.save(dst)
if __name__=='__main__': restyle(sys.argv[1],sys.argv[2])
