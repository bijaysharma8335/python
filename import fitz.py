import fitz
doc=fitz.open()
page=doc.new_page()
r = fitz.Rect(100, 100, 300, 200)
shape=page.new_shape()
shape.draw_squiggle(r.tl, r.tr)
shape.draw_squiggle(r.tr, r.br)
shape.draw_squiggle(r.br, r.tl)
shape.finish(color=(0, 0, 1), fill=(1, 1, 0))
shape.commit()
doc.save("x.pdf")