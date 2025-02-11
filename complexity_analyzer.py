import re
import ast
import time

def analyze_complexity(code):
    
    try:
        tree = ast.parse(code)
        if any(node for node in ast.walk(tree) if isinstance(node, ast.For)):
            nested_loops = 0
            for node in ast.walk(tree):
                if isinstance(node, ast.For):
                    for child in ast.walk(node):
                        if isinstance(child, ast.For):
                            nested_loops+=1

            if nested_loops>0:
                return "O(n^2)", "Nested loops indicate quadratic time complexity."
            else:
                return "O(n)", "Loops typically indicate linear time complexity."
        elif any(node for node in ast.walk(tree) if isinstance(node, ast.While)):
            return "O(n)", "While loops typically indicate linear time complexity."
        else:
            return "O(1)", "No loops or obvious complexity drivers suggest constant time complexity."
    except SyntaxError:
        return "Error", "Invalid Python code."
    except Exception as e:
        return "Error", f"An error occurred during analysis: {e}"


def execute_code(code):
    start_time = time.time()
    try:
        exec(code)  
        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time
    except Exception as e:
        return f"Error during execution: {e}"


if __name__ == '__main__':
    code_example = """
    def example_function(n):
        for i in range(n):
            print(i)
    example_function(10)
    """
    complexity, explanation = analyze_complexity(code_example)
    print(f"Complexity: {complexity}")
    print(f"Explanation: {explanation}")

    execution_time = execute_code(code_example)
    print(f"Execution time: {execution_time}")