from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QTextEdit


# Fonctions

def charger_fichier():
    print("charger_fichier")
    try:
        nom_fichier = input_nomFichier.text()
        f = open(nom_fichier, "r")
        contenu = f.read()
        input_text.setPlainText(contenu)
    except Exception as e:
        input_text.setPlainText("Erreur : " + str(e))


def sauvegarder_fichier():
    print("sauvegarder_fichier")
    try:
        nom_fichier = input_nomFichier.text()
        f = open(nom_fichier, "w")
        contenu = input_text.toPlainText()
        f.write(contenu)
    except Exception as e:
        input_text.setPlainText("Erreur : " + str(e))

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
input_text = QTextEdit()
layout.addWidget(input_text, 2, 0, 1, 2)

fen.show()
app.exec()
