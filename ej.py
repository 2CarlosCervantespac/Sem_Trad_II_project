import ast

class SemanticAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.symbol_table = {}

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Name):
            variable_name = node.targets[0].id
            self.symbol_table[variable_name] = None  # Puedes agregar más información sobre la variable según sea necesario
            self.visit(node.value)
        else:
            raise Exception("Error: Solo se admiten asignaciones a variables simples.")

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_Name(self, node):
        variable_name = node.id
        if variable_name not in self.symbol_table:
            raise Exception(f"Error: Variable '{variable_name}' no declarada.")

    # Agrega más métodos visit para otros nodos del AST según sea necesario

def analyze_semantics(source_code):
    try:
        parsed_code = ast.parse(source_code)
        semantic_analyzer = SemanticAnalyzer()
        semantic_analyzer.visit(parsed_code)
        print("Análisis semántico exitoso.")
    except Exception as e:
        print(f"Error durante el análisis semántico: {e}")

# Ejemplo de uso
codigo_fuente = """
5
y = x + 3
z = y * 2
"""

analyze_semantics(codigo_fuente)
