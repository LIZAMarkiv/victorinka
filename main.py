from PyQt6.QtWidgets import*
app = QApplication([])
window = QWidget()
window.show()

quest_lbl = QLabel("Яка столиця УкраЇни")
put_lbl = QLabel("Хто є президент України")
ans1_btn = QRadioButton("Київ")
ans = QRadioButton("Харків")
ads = QRadioButton("Одеса")
aps = QRadioButton("Львів")
vot = QRadioButton("Порошенко")
vov = QRadioButton("Дорошенко")
var = QRadioButton("Зеленський")
ton = QRadioButton("Кучма")



main_lain = QVBoxLayout()
main_lain.addWidget(quest_lbl)

h2 = QHBoxLayout()
h2.addWidget(ans1_btn)
h2.addWidget(ans)
h1 = QHBoxLayout()
h1.addWidget(ads)
h1.addWidget(aps)
h3 = QHBoxLayout()
h3.addWidget(vot)
h3.addWidget(vov)
h4 = QHBoxLayout()
h4.addWidget(var)
h4.addWidget(ton)
main_lain.addLayout(h1)
main_lain.addLayout(h2)
main_lain.addWidget(put_lbl)
main_lain.addLayout(h3)
main_lain.addLayout(h4)


window.setLayout(main_lain)
def win_funk():
    msg = QMessageBox()
    msg.setText("ЦЕ ПРАВЛЬНА ВІДПОВІДЬ")
    msg.setWindowTitle("ПЕРЕМОГА")
    msg.exec()
ans1_btn.clicked.connect(win_funk)
def loze_funk():
    msg = QMessageBox()
    msg.setText("ЦЕ НЕПРАВИЛЬНА ВІДПОВІДЬ")
    msg.setWindowTitle("ПОМИЛКА")
    msg.exec()


ans.clicked.connect(loze_funk)
ads.clicked.connect(loze_funk)
aps.clicked.connect(loze_funk)
var.clicked.connect(win_funk)
ton.clicked.connect(loze_funk)
vov.clicked.connect(loze_funk)
vot.clicked.connect(loze_funk)
app.exec()

