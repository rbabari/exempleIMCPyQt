# Construire une application PyQt
# demandant à l'utilisateur de saisir son poid et taille
# l'application affichera l'imc = poid / taille**2
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QGridLayout, QLineEdit

# fonction pour calculer
def calculIMC():
    try:
        poids = float(input_Poids.text())
        taille = float(input_Taille.text())
        if taille == 0:
            lbl_Resultat.setText("taille==0")
            return
        imc = poids / ( taille ** 2)
        print(imc)
       # lbl_Resultat.setText(str(imc))
        lbl_Resultat.setText(f"imc = {imc:.2f}")
    except ValueError:
        lbl_Resultat.setText('Error')

# 1- construire l'interface
app = QApplication([])
fen = QWidget()
fen.setWindowTitle('Calculateur IMC')

# utiliser un layout : gridlayout
layout = QGridLayout()
# champs pour saisr le poid
lbl_Poids = QLabel('Poids')
layout.addWidget(lbl_Poids, 0, 0)

input_Poids = QLineEdit()
layout.addWidget(input_Poids, 0, 1)

# champs pour saisr la taille
lbl_Taille = QLabel('Taille')
layout.addWidget(lbl_Taille, 1, 0)

input_Taille = QLineEdit()
layout.addWidget(input_Taille, 1, 1)

# champs pour afficher le resultat
btn_Calcule = QPushButton('Calcule IMC')
layout.addWidget(btn_Calcule, 2, 0)
btn_Calcule.clicked.connect(calculIMC)

lbl_Resultat = QLabel('___')
layout.addWidget(lbl_Resultat, 2, 1)
# champs pour le bouton calculer

fen.setLayout(layout)
fen.show()
app.exec()
