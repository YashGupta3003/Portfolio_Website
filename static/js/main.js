document.addEventListener('DOMContentLoaded', function() {
    // Custom cursor
    const cursor = document.createElement('div');
    cursor.classList.add('custom-cursor');
    document.body.appendChild(cursor);

    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
    });

    document.addEventListener('mousedown', () => cursor.classList.add('active'));
    document.addEventListener('mouseup', () => cursor.classList.remove('active'));

    // Dragon scales effect
    const canvas = document.getElementById('backgroundCanvas');
    const ctx = canvas.getContext('2d');
    
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    const scales = [];
    const maxScales = 50;

    class Scale {
        constructor(x, y) {
            this.x = x;
            this.y = y;
            this.size = Math.random() * 20 + 10;
            this.opacity = 1;
            this.rotation = Math.random() * Math.PI * 2;
        }

        draw() {
            ctx.save();
            ctx.translate(this.x, this.y);
            ctx.rotate(this.rotation);
            ctx.beginPath();
            ctx.moveTo(-this.size/2, 0);
            ctx.lineTo(0, -this.size);
            ctx.lineTo(this.size/2, 0);
            ctx.closePath();
            ctx.strokeStyle = `rgba(100, 255, 218, ${this.opacity})`;
            ctx.stroke();
            ctx.restore();

            this.opacity -= 0.02;
        }
    }

    document.addEventListener('mousemove', (e) => {
        if (scales.length > maxScales) {
            scales.shift();
        }
        scales.push(new Scale(e.clientX, e.clientY));
    });

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        for (let i = scales.length - 1; i >= 0; i
