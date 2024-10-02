from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton


# Fonctions

def charger_fichier():
    print("charger_fichier")
    nomFichier = input_nomFichier.text()
    f = open(nomFichier, "r")
    contenu = f.read()
    input_text.setText(contenu)


def sauvegarder_fichier():
    print("sauvegarder_fichier")
    nomFichier = input_nomFichier.text()
    f = open(nomFichier, "w")
    contenu = input_text.text()
    f.write(contenu)

# application
app = QApplication([])
fen = QWidget()

# layout
layout = QGridLayout()
fen.setLayout(layout)

# Ligne 1 : nom fichier --- QlineEdit ...
lbl_nomFichier = QLabel("Nom : ")
layout.addWidget(lbl_nomFichier, 0, 0)
input_nomFichier = QLineEdit()
layout.addWidget(input_nomFichier, 0, 1)

# Ligne 2 : btn charger -- sauvegarder
btn_charger = QPushButton("Charger")
btn_charger.clicked.connect(charger_fichier)
layout.addWidget(btn_charger, 1, 0)

btn_sauvegarder = QPushButton("Sauvegarder")
layout.addWidget(btn_sauvegarder, 1, 1)
btn_sauvegarder.clicked.connect(sauvegarder_fichier)

# ligne 3
input_text = QLineEdit()
layout.addWidget(input_text, 2, 0, 1, 2)





fen.show()
app.exec()
