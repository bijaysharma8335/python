from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label
d = Drawing(200, 100)
# mark the origin of the label
d.add(Circle(100,90, 5, fillColor=colors.green))
lab = Label()
lab.setOrigin(100,90)
lab.boxAnchor = 'ne'
lab.angle = 45
lab.dx = 0
lab.dy = -20
lab.boxStrokeColor = colors.green
lab.setText('Some
Multi-Line
Label')
d.add(lab)