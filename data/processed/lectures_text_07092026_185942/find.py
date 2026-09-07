import re,sys,pathlib
pat=re.compile(sys.argv[1], re.I)
maxn=int(sys.argv[2]) if len(sys.argv)>2 else 40
for p in sorted(pathlib.Path('.').glob('*.txt')):
    txt=p.read_text(encoding='utf-8',errors='replace')
    blocks=re.split(r'=== FILE: (.+?) \| PDFPAGE: (\d+) ===\n', txt)
    for i in range(1,len(blocks),3):
        f,pg,body=blocks[i],blocks[i+1],blocks[i+2]
        if pat.search(body):
            m=re.search(r'(\d+)\s*/\s*(\d+)\s*$', body.strip())
            sl=f"{m.group(1)}/{m.group(2)}" if m else '-'
            first=[l.strip() for l in body.strip().split('\n') if l.strip()][:1]
            print(f"{f} p{pg} slajd {sl} :: {first[0][:70] if first else ''}")
            maxn-=1
            if maxn<=0: sys.exit()
