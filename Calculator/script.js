function addToExpression(value) {
    const input = document.querySelector('input[name="expression"]');
    input.value += value;
}

function eraseLast() {
    const input = document.querySelector('input[name="expression"]');
    input.value = input.value.slice(0, -1);
}

function clearExpression() {
    const input = document.querySelector('input[name="expression"]');
    input.value = '';
}