// Test-loggning för att verifiera länkning
console.log('timer.js är korrekt länkad');

// Modul för att rita en analog klocka på canvas
function drawClock() {
    const canvas = document.getElementById('clock');
    const ctx = canvas.getContext('2d');
    const radius = canvas.height / 2;
    ctx.save(); // Spara det ursprungliga tillståndet
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.translate(radius, radius);

    function drawFace() {
        ctx.beginPath();
        ctx.arc(0, 0, radius, 0, 2 * Math.PI);
        ctx.fillStyle = 'white';
        ctx.fill();
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 4;
        ctx.stroke();
    }

    function drawTimeLeft() {
        const totalTime = 300; // Total tid i sekunder (5 minuter)
        const elapsedTime = totalTime - remainingTime;
        const endAngle = (elapsedTime / totalTime) * 2 * Math.PI - Math.PI / 2;

        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.arc(0, 0, radius, -Math.PI / 2, endAngle, false);
        ctx.fillStyle = 'red';
        ctx.fill();
    }

    function drawHands() {
        const now = new Date();
        const seconds = now.getSeconds();
        const minutes = now.getMinutes();
        const hours = now.getHours() % 12;

        // Draw hour hand
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(0, -radius * 0.5);
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 6;
        ctx.stroke();

        // Draw minute hand
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(0, -radius * 0.7);
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 4;
        ctx.stroke();

        // Draw second hand
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(0, -radius * 0.9);
        ctx.strokeStyle = 'red';
        ctx.lineWidth = 2;
        ctx.stroke();
    }

    drawFace();
    drawTimeLeft();
    drawHands();

    ctx.restore(); // Återställ det ursprungliga tillståndet
}

setInterval(drawClock, 1000);

// Modul för att hantera timer-state
let timerInterval;
let remainingTime = 300; // Standardvärde: 5 minuter

function updateDisplay() {
    const display = document.getElementById('display');
    const minutes = Math.floor(remainingTime / 60);
    const seconds = remainingTime % 60;
    display.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

// Lägg till ljudsignal vid timeout
function playAlarm() {
    const audio = new Audio('https://www.soundjay.com/button/beep-07.wav');
    audio.play();
}

// Uppdatera startTimer för att inkludera ljudsignal
function startTimer() {
    if (timerInterval) return; // Förhindra flera intervall
    timerInterval = setInterval(() => {
        if (remainingTime > 0) {
            remainingTime--;
            updateDisplay();
        } else {
            clearInterval(timerInterval);
            timerInterval = null;
            playAlarm(); // Spela ljudsignal när tiden är slut
        }
    }, 1000);
}

function stopTimer() {
    clearInterval(timerInterval);
    timerInterval = null;
}

function resetTimer() {
    stopTimer();
    remainingTime = 300; // Återställ till 5 minuter
    updateDisplay();
}

// Event listeners för knappar
const startBtn = document.getElementById('startBtn');
const stopBtn = document.getElementById('stopBtn');
const resetBtn = document.getElementById('resetBtn');

startBtn.addEventListener('click', startTimer);
stopBtn.addEventListener('click', stopTimer);
resetBtn.addEventListener('click', resetTimer);

// Initiera displayen
updateDisplay();

// Testa och justera MVP
// Kontrollera att alla funktioner fungerar som förväntat och justera eventuella buggar eller inkonsekvenser.

function testTimer() {
    console.log('Startar test av timer-funktioner...');

    // Testa start
    console.log('Testar start...');
    startTimer();
    setTimeout(() => {
        console.log('Stoppar timer efter 3 sekunder...');
        stopTimer();

        // Testa reset
        console.log('Testar reset...');
        resetTimer();

        console.log('Test av timer-funktioner slutfört.');
    }, 3000);
}

// Kör test
// testTimer(); // Avkommentera för att köra testet