from flask import Flask, render_template
import os

app = Flask(__name__)

# Create folder structure
if not os.path.exists('templates'):
    os.makedirs('templates')
if not os.path.exists('static'):
    os.makedirs('static/css')
    os.makedirs('static/js')
    os.makedirs('static/images')

# Create basic HTML templates
with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yash Gupta - Portfolio</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.7.1/gsap.min.js"></script>
</head>
<body>
    <canvas id="backgroundCanvas"></canvas>
    <div class="loading-screen" id="loadingScreen">
        <div class="loader"></div>
        <div class="loading-text">Welcome to My Portfolio</div>
    </div>
    <div class="container" style="display: none;" id="mainContent">
        <nav class="nav-menu">
            <div class="nav-item" data-section="education">Education</div>
            <div class="nav-item" data-section="achievements">Achievements</div>
            <div class="nav-item" data-section="projects">Projects</div>
            <div class="nav-item" data-section="experience">Experience</div>
            <div class="nav-item" data-section="skills">Skills</div>
        </nav>
        <div class="content">
            <div class="header-container">
                <h1 class="name-title">Yash Gupta</h1>
                <p class="subtitle">Computer Science and Mathematics Student at BITS Pilani</p>
                <p class="contact-info">
                    +91 8888-0022-00 | gupta.yash3003@gmail.com | 
                    <a href="https://linkedin.com/in/yash-gupta-7b0684224/" target="_blank" class="hover-effect">LinkedIn</a> | 
                    <a href="https://github.com/YashGupta3003/" target="_blank" class="hover-effect">GitHub</a>
                </p>
            </div>
            
            <div class="two-column-grid">
                <div class="left-column">
                    <div class="education section-card" id="education">
                        <h2 class="section-title">Education</h2>
                        <div class="education-item card-hover">
                            <h3>BITS Pilani (Aug 2021 – May 2026)</h3>
                            <p>B.E. Computer Science and M.Sc Mathematics, Minor in Finance</p>
                        </div>
                    </div>

                    <div class="achievements section-card" id="achievements">
                        <h2 class="section-title">Achievements</h2>
                        <div class="achievement-grid">
                            <div class="achievement card-hover">
                                <h3>Goldman Sachs QA Hackathon</h3>
                                <p>Rank 3 in BITS Hyderabad</p>
                            </div>
                            <div class="achievement card-hover">
                                <h3>Nomura Markets Challenge</h3>
                                <p>Rank 1 in BITS Hyderabad</p>
                            </div>
                            <div class="achievement card-hover">
                                <h3>CodeChef: yash3003</h3>
                                <p>1700 Rating (3-Star)</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="right-column">
                    <div class="projects section-card" id="projects">
                        <h2 class="section-title">Projects</h2>
                        <div class="project-grid">
                            <div class="project card-hover">
                                <h3>Stock Price Prediction</h3>
                                <p class="tech-stack">Python, ML, Llama3</p>
                            </div>
                            <div class="project card-hover">
                                <h3>BITSBIDS</h3>
                                <p class="tech-stack">SpringBoot, React, AWS</p>
                            </div>
                            <div class="project card-hover">
                                <h3>Rain Forecast</h3>
                                <p class="tech-stack">Python, Keras</p>
                            </div>
                        </div>
                    </div>

                    <div class="experience-skills-grid">
                        <div class="experience section-card" id="experience">
                            <h2 class="section-title">Experience</h2>
                            <div class="exp-item card-hover">
                                <h3>ML Summer Intern - IMD</h3>
                                <p>May-July 2023 | Improved prediction by 34%</p>
                            </div>
                        </div>

                        <div class="skills section-card" id="skills">
                            <h2 class="section-title">Skills</h2>
                            <div class="skills-grid">
                                <div class="skill-category">
                                    <div class="skill-items">
                                        <div class="skill-item">Python</div>
                                        <div class="skill-item">C++</div>
                                        <div class="skill-item">Java</div>
                                        <div class="skill-item">SQL</div>
                                        <div class="skill-item">Git</div>
                                        <div class="skill-item">ML</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    <script>
        window.addEventListener('load', function() {
            setTimeout(function() {
                document.getElementById('loadingScreen').style.display = 'none';
                document.getElementById('mainContent').style.display = 'block';
            }, 2000);
        });
    </script>
</body>
</html>
    ''')

# Create CSS file with enhanced styles
with open('static/css/style.css', 'w', encoding='utf-8') as f:
    f.write('''
/* Loading Screen */
.loading-screen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #0a192f;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

#backgroundCanvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    pointer-events: none;
}

.loader {
    width: 50px;
    height: 50px;
    border: 5px solid #64ffda;
    border-radius: 50%;
    border-top-color: transparent;
    animation: spin 1s linear infinite;
}

.loading-text {
    color: #64ffda;
    margin-top: 20px;
    font-size: 1.2em;
    letter-spacing: 2px;
    font-family: 'Poppins', sans-serif;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

body {
    margin: 0;
    padding: 0;
    font-family: 'Poppins', sans-serif;
    background: radial-gradient(circle at center, #112240 0%, #0a192f 50%, #020c1b 100%);
    background-attachment: fixed;
    color: #e6f1ff;
    overflow-x: hidden;
    cursor: none;
}

.custom-cursor {
    width: 20px;
    height: 20px;
    border: 2px solid #64ffda;
    border-radius: 50%;
    position: fixed;
    pointer-events: none;
    z-index: 9999;
    transition: transform 0.2s ease;
}

.custom-cursor.active {
    transform: scale(1.5);
}

/* Navigation Menu */
.nav-menu {
    position: fixed;
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
    z-index: 100;
}

.nav-item {
    padding: 10px;
    margin: 5px 0;
    cursor: none;
    color: #64ffda;
    font-weight: 500;
    transition: all 0.3s ease;
    position: relative;
}

.nav-item::after {
    content: '';
    position: absolute;
    right: -10px;
    top: 50%;
    width: 0;
    height: 2px;
    background: #64ffda;
    transition: width 0.3s ease;
}

.nav-item:hover::after {
    width: 20px;
}

/* Name Title Animation */
.name-title {
    font-size: 3.5em;
    font-weight: 700;
    color: #ccd6f6;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    animation: titlePulse 3s infinite;
    margin-bottom: 0.5em;
}

@keyframes titlePulse {
    0% { opacity: 1; }
    50% { opacity: 0.8; text-shadow: 0 0 10px #64ffda; }
    100% { opacity: 1; }
}

.subtitle {
    font-size: 1.5em;
    color: #8892b0;
    margin-bottom: 1em;
    font-weight: 400;
}

.contact-info {
    color: #8892b0;
    font-size: 1.1em;
}

.contact-info a {
    color: #64ffda;
    text-decoration: none;
    transition: all 0.3s ease;
    cursor: none;
}

.contact-info a:hover {
    color: #fff;
}

.container {
    position: relative;
    min-height: 100vh;
    padding: 2rem;
}

.content {
    position: relative;
    max-width: 1200px;
    margin: 0 auto;
    z-index: 2;
}

.two-column-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}

.section-card {
    opacity: 0;
    transform: translateY(50px);
    transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    margin: 2rem 0;
    padding: 1.5rem;
    background: rgba(17, 34, 64, 0.8);
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(10px);
}

.section-card.visible {
    opacity: 1;
    transform: translateY(0);
}

.section-title {
    color: #64ffda;
    font-size: 1.8em;
    font-weight: 600;
    margin-bottom: 1em;
}

h3 {
    color: #ccd6f6;
    font-size: 1.2em;
    font-weight: 600;
    margin-bottom: 0.3em;
}

p {
    color: #8892b0;
    line-height: 1.4;
    font-size: 0.9em;
}

.tech-stack {
    color: #64ffda;
    font-size: 0.8em;
    font-weight: 500;
}

.achievement-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
}

.project-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1rem;
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
    gap: 0.5rem;
}

.skill-item {
    background: rgba(100, 255, 218, 0.1);
    color: #ccd6f6;
    padding: 0.4rem 0.8rem;
    border-radius: 15px;
    font-size: 0.8em;
    font-weight: 500;
    text-align: center;
    transition: all 0.3s ease;
}

.skill-item:hover {
    background: rgba(100, 255, 218, 0.2);
    transform: translateY(-2px);
}

.experience-skills-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
}

/* Responsive Design */
@media (max-width: 1024px) {
    .two-column-grid {
        grid-template-columns: 1fr;
    }
}
    ''')

# Create JavaScript file for enhanced animations and interactions
with open('static/js/main.js', 'w', encoding='utf-8') as f:
    f.write('''
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
        
        for (let i = scales.length - 1; i >= 0; i--) {
            scales[i].draw();
            if (scales[i].opacity <= 0) {
                scales.splice(i, 1);
            }
        }
        
        requestAnimationFrame(animate);
    }

    animate();

    // Show sections when they come into view
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('.section-card').forEach((section) => {
        observer.observe(section);
    });

    // Navigation menu click handling
    document.querySelectorAll('.nav-item').forEach(item => {
        item.addEventListener('click', function() {
            const sectionId = this.getAttribute('data-section');
            const section = document.getElementById(sectionId);
            section.scrollIntoView({ behavior: 'smooth' });
        });
    });
});
    ''')

# Create the basic route for single page
@app.route('/')
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()
