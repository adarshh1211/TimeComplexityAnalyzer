document.addEventListener('DOMContentLoaded', function() {
    const analyzeButton = document.getElementById('analyze');
    const codeInput = document.getElementById('code');
    const complexityOutput = document.getElementById('complexity');
    const explanationOutput = document.getElementById('explanation');
    const executionTimeOutput = document.getElementById('executionTime');
    const errorOutput = document.getElementById('error');

    analyzeButton.addEventListener('click', function() {
        const code = codeInput.value;

        
        if (!code.trim()) {
            errorOutput.textContent = "Please enter some Python code.";
            complexityOutput.textContent = "Complexity: ";
            explanationOutput.textContent = "Explanation: ";
            executionTimeOutput.textContent = "Execution Time: ";
            return;
        }

        errorOutput.textContent = ""; 

        
        fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ code: code })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                complexityOutput.textContent = "Complexity: ";
                explanationOutput.textContent = "Explanation: ";
                executionTimeOutput.textContent = "Execution Time: ";
                errorOutput.textContent = "Error: " + data.error;
            } else {
                complexityOutput.textContent = "Complexity: " + data.complexity;
                explanationOutput.textContent = "Explanation: " + data.explanation;
                executionTimeOutput.textContent = "Execution Time: " + data.execution_time;
                errorOutput.textContent = "";
            }
        })
        .catch(error => {
            console.error('Error:', error);
            complexityOutput.textContent = "Complexity: ";
            explanationOutput.textContent = "Explanation: ";
            executionTimeOutput.textContent = "Execution Time: ";

            errorOutput.textContent = "Error: Failed to connect to the server.";
        });
    });
});