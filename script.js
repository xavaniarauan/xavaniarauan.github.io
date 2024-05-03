function validateNumber() {
    const numberInput = document.getElementById("number");
    const numberValue = numberInput.value.trim();
    const resultElement = document.getElementById("result");
  
    // Regular expression for scientific number validation
    const regex = /^-?\d+\.?\d*(?:e|E)[-+]?\d+$/;
  
    if (regex.test(numberValue)) {
      resultElement.textContent = `${numberValue} is a valid scientific number.`;
      resultElement.style.color = "green";
    } else {
      resultElement.textContent = `${numberValue} is not a valid scientific number.`;
      resultElement.style.color = "red";
    }
  }
  