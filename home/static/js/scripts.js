yearElement.innerHTML = digits.map((d, i) => `<span class="year-digit" data-index="${i}">${d}</span>`).join('');

let counter = 0;
setInterval(() => {
    const digits = document.querySelectorAll('.year-digit');
    digits.forEach((digit, index) => {
        const colorIndex = (counter + index) % colors.length;
        digit.style.color = colors[colorIndex];
    });
    counter++;
}, 1000);
