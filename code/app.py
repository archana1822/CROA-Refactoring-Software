import streamlit as st
import ast
import astor  # To convert AST back to source code

# Code Smell Detector and Optimizer Class
class CodeSmellDetector(ast.NodeTransformer):
    def __init__(self, max_method_length=10, max_conditionals=3, max_params=5):
        self.max_method_length = max_method_length  # Threshold for method length
        self.max_conditionals = max_conditionals    # Threshold for number of conditionals
        self.max_params = max_params                # Threshold for the number of parameters in a function
        self.smells = []                            # List to store identified code smells

    def visit_FunctionDef(self, node):
        """Check function definition for long methods and long parameter lists."""
        method_length = len(node.body)
        if method_length > self.max_method_length:
            self.smells.append(f"Long method: {node.name} is {method_length} lines long. Consider breaking it into smaller functions.")

            # Refactor long method: Break into smaller methods (if possible, for this demo, just suggest)
            if method_length > self.max_method_length:
                node = self.split_long_function(node)

        num_params = len(node.args.args)
        if num_params > self.max_params:
            self.smells.append(f"Long parameter list: {node.name} has {num_params} parameters. Consider reducing the number of parameters.")

            # Refactor long parameter list: Use *args or **kwargs or pass an object instead of multiple params
            node.args.args = node.args.args[:self.max_params]  # For simplicity, trim down to max_params

        return self.generic_visit(node)

    def visit_If(self, node):
        """Check if statements for complex conditionals."""
        num_conditionals = len([n for n in ast.walk(node) if isinstance(n, ast.If)])
        if num_conditionals > self.max_conditionals:
            line_number = node.lineno
            self.smells.append(f"Complex conditional at line {line_number} with {num_conditionals} nested conditions. Consider simplifying the conditions.")
            
            # Refactor nested conditionals (for demo, flatten one level)
            if num_conditionals > self.max_conditionals:
                node = self.flatten_conditionals(node)
        
        return self.generic_visit(node)

    def report_smells(self):
        """Return the list of code smells identified."""
        if not self.smells:
            return "No significant code smells detected."
        return "\n".join(self.smells)

    def split_long_function(self, node):
        """For demo purposes, break long functions into smaller stubs."""
        # For simplicity, we just split after the max method length
        split_point = self.max_method_length // 2
        new_node = ast.FunctionDef(
            name=node.name + "_part2",
            args=node.args,
            body=node.body[split_point:],
            decorator_list=node.decorator_list,
            lineno=node.lineno
        )
        node.body = node.body[:split_point]
        return node

    def flatten_conditionals(self, node):
        """For demo, flatten one level of nested if-statements."""
        # If nested, we'll merge simple branches into a single-level structure
        if isinstance(node, ast.If) and isinstance(node.body[0], ast.If):
            # Merge conditions
            new_test = ast.BoolOp(op=ast.And(), values=[node.test, node.body[0].test])
            new_body = node.body[0].body
            return ast.If(test=new_test, body=new_body, orelse=node.orelse)
        return node

def analyze_code_for_refactoring(source_code):
    """
    Analyze the provided Python source code for common code smells and suggest refactoring.
    :param source_code: A string representing the source code to analyze.
    :return: A string with suggestions for refactoring and the refactored code.
    """
    # Parse the source code into an AST
    try:
        tree = ast.parse(source_code)
    except SyntaxError as e:
        return f"Syntax Error: {e}", None

    # Create an instance of the CodeSmellDetector
    detector = CodeSmellDetector()

    # Visit the AST nodes to check for code smells and apply optimizations
    optimized_tree = detector.visit(tree)

    # Get the refactored code (if any changes were made)
    refactored_code = astor.to_source(optimized_tree)

    # Return the detected code smells and refactored code
    return detector.report_smells(), refactored_code

# Streamlit Interface
st.title("Code Refactoring Analysis and Optimization Tool")

st.write("This tool analyzes your Python code for common code smells, suggests refactoring, and provides an optimized version of the code.")

# Code input from the user
user_code = st.text_area("Enter your Python code here:", height=300)

if st.button("Analyze Code"):
    if user_code.strip():
        # Analyze the code for refactoring needs
        refactoring_report, optimized_code = analyze_code_for_refactoring(user_code)

        # Display the results
        if "No significant code smells detected." in refactoring_report:
            st.success("No significant code smells detected. Refactoring may not be required.")
        else:
            st.warning("Code smells detected. Refactoring is recommended.")
            st.text(refactoring_report)

            # Display the refactored code
            if optimized_code:
                st.subheader("Optimized Code Version:")
                st.code(optimized_code, language='python')
    else:
        st.error("Please enter valid Python code.")
