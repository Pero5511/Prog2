#IME I PREZIME: PERICA TOPIC
import re
tekst="p1e2r3i 4c5XYZT"
reg1="(^P|^p).*[0-5].*(t$|T$)"
reg2=r"\s"
res1=re.findall(reg1,tekst)
res2=re.findall(reg2,tekst)
if res1 and res2:
    print(tekst,"zadovoljava kriterije")
else:
    print(tekst,"ne zadovoljava uvjete...")
