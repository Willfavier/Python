import pytest
from src.citations_motivantes.utils import choisir_phrase_depuis_fichier

def test_choisir_phrase_depuis_fichier(tmp_path):
    fichier_test = tmp_path / "test.txt"
    contenu = "Phrase 1\nPhrase 2\nPhrase 3"
    fichier_test.write_text(contenu, encoding="utf-8")

    phrase = choisir_phrase_depuis_fichier(fichier_test)
    assert phrase in contenu.split("\n")
