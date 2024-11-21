// Display button value on click
document.querySelectorAll('.button').forEach(button => {
    button.addEventListener('click', () => {
        const display = document.getElementById('display');
        const buttonText = button.textContent.trim();
        const unit = document.querySelector('input[name="radius"]:checked').value;

        // Check if the button clicked is "C"
        if (buttonText === 'C') {
            display.value = ''; // Clear the display
        }
        // If the button is "DEL", remove the last character from the display
        else if (buttonText === 'DEL') {
            display.value = display.value.slice(0, -1); // Remove last character
        }
        // Handle constants: e and pi
        /* else if (buttonText === 'e'){
            display.value += Math.E.toFixed(10);
        }
        else if(buttonText === 'π'){
            display.value += Math.PI.toFixed(10);
        } */
        // Append `e` and `π` to the display without evaluating them immediately
        else if (buttonText === 'e' || buttonText === 'π') {
            display.value += buttonText; // Just add `e` or `π` as-is
        }
        // Handle arccos calculation
        else if (buttonText === 'arccos(x)'){
            display.value += 'arccos('; // Add "arccos" to the display
        }
        // Handle the arccos operation
        else if(display.value.startsWith('arccos')){
            // Append to arccos input
            if(buttonText === ')'){
                display.value += ')';
            }
            else if(buttonText === '='){
                // Extract the value from arccos()
                const input = display.value.replace('arccos(', '').replace(')', '').trim();
                const x = parseFloat(input);

                // Validate the number after arccos
                if (isNaN(x) || x < -1 || x > 1) {
                    display.value = 'Error: Invalid input'; // Input must be between -1 and 1
                    return;
                }

                // Send the input to Flask API
                fetch('http://127.0.0.1:5000/calculate_arccos', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ x: x, unit: unit })
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            display.value = `${data.result} ${unit}`;
                        } else {
                            display.value = `Error: ${data.error}`;
                        }
                    })
                    .catch(() => {
                        display.value = 'Error: Network issue'; // Handle network errors
                    });
            }
            else{
                display.value += buttonText;
            }
        }
        // Handle x^y operation
        /* else if (buttonText === 'x^y'){
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
        } */
        else if(buttonText === 'x^y'){
            let expression = display.value.trim()

            expression = expression
                .replace(/π/g, Math.PI)
                .replace(/e/g, Math.E);

            expression = expression
                .replace(/(\d)(\()/g, '$1*(') // Example: 5(5) -> 5*(5)
                .replace(/(\))(\()/g, ')*(')
                .replace(/(\))(\d)/g, ')*$2') // Example: (5)5 -> (5)*5
                .replace(/(\d)(π|e)/g, '$1*$2') // Example: 5π -> 5*Math.PI
                .replace(/(π|e)(\d)/g, '$1*$2');

            const match = expression.match(/^([\d.]+),([\d.]+)$/);

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
        // Handle a(b^x) function
        else if (buttonText === 'a(b^x)'){
            const input = display.value.trim();
            const match = input.match(/^([\d.]+),([\d.]+),([\d.]+)$/);

            if(match){
                const a = parseFloat(match[1]);
                const b = parseFloat(match[2]);
                const x = parseFloat(match[3]);

                // Call the Python function via an API
                fetch('http://127.0.0.1:5000/calculate_abx', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ a, b, x})
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
                display.value = 'Error: Invalid format (use a,b,x)';
            }
        }
        else if(buttonText === 'arccos(x)'){

        }
        else if(buttonText === 'log_b(x)'){
            const input = display.value.trim();
            const match = input.match(/^([\d.]+),([\d.]+)$/);

            if(match){
                const b = parseFloat(match[1]);
                const x = parseFloat(match[2]);

                // Call the Python function via an API
                fetch('http://127.0.0.1:5000/calculate_logbx', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ b, x })
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
                display.value = 'Error: Invalid format (use b,x)';
            }
        }

        else if(buttonText == 'MAD'){
            const input = display.value.trim();
            const match = input.match(/^([\d.]+(?:, *[\d.]+)*)$/);

            if (match){
                // Split input into an array of numbers
                const numbers = match[1].split(',').map(num => parseFloat(num.trim()));

                fetch('http://127.0.0.1:5000/calculate_mad', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ data: numbers })
                })
                    .then(response => response.json())
                    .then(data => {
                         if (data.success) {
                             display.value = data.result; // Show the result
                         } else {
                             display.value = 'Error: ' + data.error; // Show error message
                         }
                    })
                    .catch(() => {
                         display.value = 'Error: Network issue'; // Handle network errors
                    });
            }
            else{
                display.value = 'Error: Invalid format (use numbers separated by commas)';
            }
        }
        else if(buttonText === 'σ'){
            const input = display.value.trim();

        }
        else if(buttonText === '='){
            let expression = display.value
                .replace(/π/g, Math.PI)
                .replace(/e/g, Math.E);
            expression = expression
                .replace(/(\d)(\()/g, '$1*(') // Example: 5(5) -> 5*(5)
                .replace(/(\))(\()/g, ')*(')
                .replace(/(\))(\d)/g, ')*$2') // Example: (5)5 -> (5)*5
                .replace(/(\d)(π|e)/g, '$1*$2') // Example: 5π -> 5*Math.PI
                .replace(/(π|e)(\d)/g, '$1*$2');

            try{
                const result = eval(expression);
                display.value = result;
            }
            catch(error){
                display.value = 'Error';
                console.error('Evaluation error:', error);
            }
        }
        else {
            display.value += buttonText; // Add other button values to the display
        }

    });
});
