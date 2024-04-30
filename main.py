from categoria import Categoria
from desktop import Desktop
from notebook import Notebook

categoria = Categoria(1, "Eletrônicos")
desktop = Desktop("Modelo A", "Preto", 1500.00, categoria, "500W")
notebook = Notebook("Modelo B", "Prata", 2000.00, categoria, "8 horas")

print(desktop.getInformacoes())
print(notebook.getInformacoes())
