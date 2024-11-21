// Display button value on click
document.querySelectorAll('.button').forEach(button => {
    button.addEventListener('click', () => {
        const display = document.getElementById('display');
        //display.value += button.textContent.trim();

        // Check if the button clicked is "C"
        if (button.textContent.trim() === 'C') {
            display.value = ''; // Clear the display
        }
        // If the button is "DEL", remove the last character from the display
        else if (button.textContent.trim() === 'DEL') {
            display.value = display.value.slice(0, -1); // Remove last character
        }
        // Handle x^y operation
        else if (buttonText === 'x^y'){
            const input = display.value.trim();
            const match = input.match(/^([\d.]+),([\d.]+)$/);

            if(match){
                const x = parseFloat(match[1]);
                const y = parseFloat(match[2]);

                // Call the Python function via an API
                fetch('http://127.0.0.1:5000/calculate_power', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ x, y })
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            display.value = data.result; // Show the result
                        } else {
                            display.value = 'Error'; // Handle errors
                        }
                    })
                    .catch(() => {
                        display.value = 'Error: Network issue'; // Handle network errors
                    });
            }
            else{
                display.value = 'Error: Invalid format (use x,y)';
            }
        }
        else {
            display.value += button.textContent.trim(); // Add other button values to the display
        }

    });
});
