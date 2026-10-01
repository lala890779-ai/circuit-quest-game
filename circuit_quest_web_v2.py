import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(
    page_title="Circuit Quest: Master of Voltages v2",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Cyberpunk CSS for Streamlit Shell
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Vazirmatn', sans-serif;
        background-color: #0a0e17;
        color: #e0e6ed;
    }
    
    .stApp {
        background: linear-gradient(135deg, #070a11 0%, #0f172a 100%);
    }
    
    .main-title {
        text-align: center;
        background: linear-gradient(90deg, #00f2fe 0%, #4facfe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 900;
        margin-bottom: 0.2rem;
        text-shadow: 0 0 20px rgba(0, 242, 254, 0.3);
    }
    
    .sub-title {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }
    
    .stButton>button {
        background: linear-gradient(90deg, #00c6ff 0%, #0072ff 100%);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1.2rem;
        box-shadow: 0 4px 15px rgba(0, 198, 255, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 198, 255, 0.6);
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">⚡ Circuit Quest v2: Cyberpunk Edition</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">بازی و شبیه‌ساز دوبعدی تعاملی مدار الکتریکی و الکترونیکی</div>', unsafe_allow_html=True)

# HTML5 Canvas + JavaScript Game Engine
game_html = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<style>
    * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
    body {
        background-color: #090d16;
        color: #fff;
        font-family: 'Vazirmatn', Tahoma, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        overflow: hidden;
    }

    #game-container {
        position: relative;
        width: 1000px;
        max-width: 98vw;
        height: 680px;
        background: #0d1322;
        border: 2px solid #00f2fe;
        border-radius: 16px;
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.25), inset 0 0 15px rgba(0, 242, 254, 0.1);
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    /* HUD Bar */
    .hud-bar {
        height: 60px;
        background: rgba(15, 23, 42, 0.9);
        border-bottom: 1px solid #1e293b;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 20px;
        font-size: 15px;
        font-weight: bold;
    }

    .hud-item {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .health-bg {
        width: 140px;
        height: 16px;
        background: #1e293b;
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid #334155;
    }

    .health-fill {
        height: 100%;
        width: 100%;
        background: linear-gradient(90deg, #10b981, #34d399);
        transition: width 0.3s ease, background 0.3s ease;
    }

    /* Canvas Area */
    #canvas-wrap {
        position: relative;
        flex: 1;
        width: 100%;
        background: #070a12;
    }

    canvas {
        width: 100%;
        height: 100%;
        display: block;
    }

    /* Control Panel UI */
    .controls-panel {
        height: 140px;
        background: rgba(15, 23, 42, 0.95);
        border-top: 1px solid #1e293b;
        padding: 12px 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
    }

    .dialog-box {
        flex: 1;
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 10px 15px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .dialog-title {
        color: #38bdf8;
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 4px;
    }

    .dialog-desc {
        color: #cbd5e1;
        font-size: 13px;
        line-height: 1.4;
    }

    .interactive-zone {
        display: flex;
        align-items: center;
        gap: 15px;
        background: rgba(30, 41, 59, 0.4);
        padding: 10px 20px;
        border-radius: 10px;
        border: 1px solid #334155;
    }

    .slider-group {
        display: flex;
        flex-direction: column;
        gap: 6px;
        align-items: center;
    }

    .slider-group label {
        font-size: 12px;
        color: #94a3b8;
    }

    input[type=range] {
        width: 130px;
        accent-color: #00f2fe;
        cursor: pointer;
    }

    .btn-action {
        background: linear-gradient(135deg, #00f2fe, #4facfe);
        color: #000;
        font-weight: bold;
        border: none;
        padding: 10px 18px;
        border-radius: 8px;
        cursor: pointer;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.4);
        transition: transform 0.1s;
        font-size: 14px;
    }

    .btn-action:active {
        transform: scale(0.96);
    }

    /* Chapter Selector Tabs */
    .chapter-tabs {
        position: absolute;
        top: 10px;
        right: 10px;
        display: flex;
        gap: 8px;
        z-index: 10;
    }

    .tab-btn {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid #334155;
        color: #94a3b8;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 12px;
        cursor: pointer;
        transition: all 0.2s;
    }

    .tab-btn.active {
        background: #00f2fe;
        color: #000;
        font-weight: bold;
        border-color: #00f2fe;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.5);
    }

    /* Sound Button */
    .sound-btn {
        position: absolute;
        top: 10px;
        left: 10px;
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid #334155;
        color: #38bdf8;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        z-index: 10;
        font-size: 16px;
    }
</style>
</head>
<body>

<div id="game-container">
    <!-- Sound Toggle -->
    <button class="sound-btn" id="soundBtn" onclick="toggleSound()">🔊</button>

    <!-- Chapter Tabs -->
    <div class="chapter-tabs">
        <button class="tab-btn active" id="tab1" onclick="loadChapter(1)">فصل ۱: قانون اهم</button>
        <button class="tab-btn" id="tab2" onclick="loadChapter(2)">فصل ۲: KVL و KCL</button>
        <button class="tab-btn" id="tab3" onclick="loadChapter(3)">فصل ۳: خازن RC</button>
        <button class="tab-btn" id="tab4" onclick="loadChapter(4)">فصل ۴: تقویت‌کننده Op-Amp</button>
    </div>

    <!-- HUD -->
    <div class="hud-bar">
        <div class="hud-item">
            <span>🛡️ پایداری شبکه:</span>
            <div class="health-bg"><div class="health-fill" id="healthFill"></div></div>
            <span id="healthTxt" style="color:#10b981;">100%</span>
        </div>
        <div class="hud-item">
            <span>⭐ امتیاز: <span id="scoreVal" style="color:#f59e0b;">0</span></span>
        </div>
        <div class="hud-item">
            <span>🎯 مرحله: <span id="chapterTitle" style="color:#38bdf8;">فصل ۱ - تثبیت جریان شهر</span></span>
        </div>
    </div>

    <!-- Canvas -->
    <div id="canvas-wrap">
        <canvas id="gameCanvas" width="1000" height="460"></canvas>
    </div>

    <!-- Controls Panel -->
    <div class="controls-panel">
        <div class="dialog-box">
            <div class="dialog-title" id="dialogTitle">⚡ ماموریت: تنظیم مقاومت بار</div>
            <div class="dialog-desc" id="dialogDesc">
                مقاومت R_load را طوری تنظیم کنید که جریان خروجی دقیقا روی 1.5 آمپر قرار گیرد. جریان اضافی باعث اتصالی و داغ شدن سیم‌ها می‌شود!
            </div>
        </div>
        <div class="interactive-zone" id="interactiveZone">
            <!-- Dynamic Controls Inject Here -->
        </div>
    </div>
</div>

<script>
// --- Web Audio API FX ---
let audioCtx = null;
let soundEnabled = true;

function initAudio() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
}

function playSound(type) {
    if (!soundEnabled) return;
    initAudio();
    if (!audioCtx) return;

    let osc = audioCtx.createOscillator();
    let gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);

    let now = audioCtx.currentTime;

    if (type === 'beep') {
        osc.frequency.setValueAtTime(600, now);
        gain.gain.setValueAtTime(0.1, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.1);
        osc.start(now);
        osc.stop(now + 0.1);
    } else if (type === 'success') {
        osc.frequency.setValueAtTime(523.25, now);
        osc.frequency.setValueAtTime(659.25, now + 0.1);
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
        osc.start(now);
        osc.stop(now + 0.3);
    } else if (type === 'spark') {
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(150, now);
        osc.frequency.linearRampToValueAtTime(80, now + 0.2);
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
        osc.start(now);
        osc.stop(now + 0.2);
    }
}

function toggleSound() {
    soundEnabled = !soundEnabled;
    document.getElementById('soundBtn').innerText = soundEnabled ? '🔊' : '🔇';
}

// --- Game State ---
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let currentChapter = 1;
let score = 0;
let health = 100;

// Particles
let electrons = [];
let sparks = [];

// Chapter Parameters
let ch1_Rload = 10; // target is 6 Ohm for I = 20/(4+6) = 2.0A
let ch2_switches = [false, true, false]; // Switch States for KCL
let ch3_time = 0;
let ch3_charging = false;
let ch3_capVoltage = 0;
let ch3_rcTau = 2.0; // seconds
let ch4_Rf = 20; // Op-Amp Feedback

// Initialize Particles
for (let i = 0; i < 40; i++) {
    electrons.push({
        pos: Math.random(), // 0 to 1 along circuit loop
        speed: 0.005
    });
}

function updateHealth(delta) {
    health = Math.max(0, Math.min(100, health + delta));
    const fill = document.getElementById('healthFill');
    const txt = document.getElementById('healthTxt');
    fill.style.width = health + '%';
    txt.innerText = Math.round(health) + '%';

    if (health > 50) {
        fill.style.background = 'linear-gradient(90deg, #10b981, #34d399)';
        txt.style.color = '#10b981';
    } else if (health > 20) {
        fill.style.background = 'linear-gradient(90deg, #f59e0b, #fbbf24)';
        txt.style.color = '#f59e0b';
    } else {
        fill.style.background = 'linear-gradient(90deg, #ef4444, #f87171)';
        txt.style.color = '#ef4444';
    }
}

function loadChapter(ch) {
    currentChapter = ch;
    playSound('beep');

    // Update Tabs UI
    for (let i = 1; i <= 4; i++) {
        document.getElementById('tab' + i).classList.remove('active');
    }
    document.getElementById('tab' + ch).classList.add('active');

    const dialogTitle = document.getElementById('dialogTitle');
    const dialogDesc = document.getElementById('dialogDesc');
    const interactiveZone = document.getElementById('interactiveZone');
    const chapterTitle = document.getElementById('chapterTitle');

    if (ch === 1) {
        chapterTitle.innerText = "فصل ۱ - تعادل قانون اهم";
        dialogTitle.innerText = "⚡ ماموریت: تنظیم جریان شبکه اصلی";
        dialogDesc.innerText = "منبع ولتاژ 24V به مقاومت منبع 4Ω و مقاومت قابل تنظیم R_load متصل است. اسلایدر را طوری تنظیم کنید که جریان دقیقا 2.0A شود (I = V / R_total).";
        
        interactiveZone.innerHTML = `
            <div class="slider-group">
                <label>مقاومت R_load: <b id="rloadVal" style="color:#00f2fe">10 Ω</b></label>
                <input type="range" id="rloadSlider" min="1" max="20" step="0.5" value="10" oninput="onCh1Slider(this.value)">
            </div>
            <button class="btn-action" onclick="checkCh1()">تایید و تثبیت</button>
        `;
    } else if (ch === 2) {
        chapterTitle.innerText = "فصل ۲: تعادل گره‌ها (KCL)";
        dialogTitle.innerText = "⚡ ماموریت: مسیریابی جریان گره مرکزی";
        dialogDesc.innerText = "منبع جریان 10A به گره مرکزی می‌رسد. کلیدها را طوری روشن/خاموش کنید تا مجموع جریان‌های خروجی دقیقا برابر 10A شود (KCL: ΣI_in = ΣI_out).";

        interactiveZone.innerHTML = `
            <button class="btn-action" id="sw1" onclick="toggleSwitch(0)">شاخه A (4A): OFF</button>
            <button class="btn-action" id="sw2" onclick="toggleSwitch(1)">شاخه B (6A): ON</button>
            <button class="btn-action" id="sw3" onclick="toggleSwitch(2)">شاخه C (2A): OFF</button>
            <button class="btn-action" style="background:#10b981;" onclick="checkCh2()">تست گره</button>
        `;
        updateSwitchBtns();
    } else if (ch === 3) {
        chapterTitle.innerText = "فصل ۳: شارژ خازن RC";
        dialogTitle.innerText = "⚡ ماموریت: زمان‌بندی دکمه تخلیه خازن";
        dialogDesc.innerText = "دکمه 'شارژ خازن' را بزنید و اسیلوسکوپ را نظر داشته باشید. وقتی ولتاژ خازن به 63.2% ولتاژ نهایی (معادل τ = 2s) رسید، دکمه 'تثبیت' را فشار دهید!";

        interactiveZone.innerHTML = `
            <button class="btn-action" onclick="startCapCharge()">⚡ شروع شارژ خازن</button>
            <button class="btn-action" style="background:#10b981;" onclick="stopCapCharge()">🎯 ثبت در t = τ (63.2%)</button>
        `;
    } else if (ch === 4) {
        chapterTitle.innerText = "فصل ۴: تقویت‌کننده Op-Amp";
        dialogTitle.innerText = "⚡ ماموریت: تنظیم بهره ولتاژ (Av)";
        dialogDesc.innerText = "ورودی سینوسی 0.5V به تقویت‌کننده معکوس‌کننده متصل است (R_in = 2kΩ). مقاومت بازخورد R_f را طوری تنظیم کنید که ولتاژ خروجی به 5V برسد بدون اینکه اشباع (Clipping) شود.";

        interactiveZone.innerHTML = `
            <div class="slider-group">
                <label>مقاومت Rf: <b id="rfVal" style="color:#00f2fe">20 kΩ</b></label>
                <input type="range" id="rfSlider" min="2" max="40" step="1" value="20" oninput="onCh4Slider(this.value)">
            </div>
            <button class="btn-action" onclick="checkCh4()">تست تقویت‌کننده</button>
        `;
    }
}

// Ch 1 Logic
function onCh1Slider(val) {
    ch1_Rload = parseFloat(val);
    document.getElementById('rloadVal').innerText = ch1_Rload + ' Ω';
}

function checkCh1() {
    // V = 24V, R_src = 4, R_total = 4 + R_load. Target I = 2.0A => R_total = 12 => R_load = 8
    const I = 24 / (4 + ch1_Rload);
    if (Math.abs(I - 2.0) < 0.1) {
        playSound('success');
        score += 200;
        updateHealth(15);
        document.getElementById('scoreVal').innerText = score;
        alert("🎉 عالی بود! مقاومت R_load = 8Ω تنظیم شد و جریان شبکه روی 2.0A تثبیت گردید.");
    } else {
        playSound('spark');
        updateHealth(-20);
        addSparks(500, 230);
        alert(`❌ خطا! جریان فعلی ${I.toFixed(2)}A است. هدف 2.0A می‌باشد (فرمول: I = 24 / (4 + R_load)).`);
    }
}

// Ch 2 Logic
function toggleSwitch(idx) {
    ch2_switches[idx] = !ch2_switches[idx];
    playSound('beep');
    updateSwitchBtns();
}

function updateSwitchBtns() {
    const vals = [4, 6, 2];
    const names = ['A (4A)', 'B (6A)', 'C (2A)'];
    for (let i = 0; i < 3; i++) {
        const btn = document.getElementById('sw' + (i+1));
        if (btn) {
            btn.innerText = `شاخه ${names[i]}: ${ch2_switches[i] ? 'ON' : 'OFF'}`;
            btn.style.background = ch2_switches[i] ? 'linear-gradient(135deg, #00f2fe, #4facfe)' : '#334155';
            btn.style.color = ch2_switches[i] ? '#000' : '#fff';
        }
    }
}

function checkCh2() {
    let currentOut = 0;
    if (ch2_switches[0]) currentOut += 4;
    if (ch2_switches[1]) currentOut += 6;
    if (ch2_switches[2]) currentOut += 2;

    if (currentOut === 10) {
        playSound('success');
        score += 250;
        updateHealth(20);
        document.getElementById('scoreVal').innerText = score;
        alert("🎉 آفرین! قانون KCL برقرار شد (10A ورود = 10A خروج).");
    } else {
        playSound('spark');
        updateHealth(-15);
        addSparks(500, 230);
        alert(`❌ عدم تعادل گره! جریان خروجی فعلی ${currentOut}A است اما ورودی 10A می‌باشد.`);
    }
}

// Ch 3 Logic
function startCapCharge() {
    ch3_time = 0;
    ch3_charging = true;
    ch3_capVoltage = 0;
    playSound('beep');
}

function stopCapCharge() {
    if (!ch3_charging) return;
    ch3_charging = false;
    
    // Target is t = 2.0s (63.2% of 10V = 6.32V)
    const targetV = 10 * (1 - Math.exp(-1)); // ~6.32V
    const diff = Math.abs(ch3_capVoltage - targetV);

    if (diff < 0.8) {
        playSound('success');
        score += 300;
        updateHealth(20);
        document.getElementById('scoreVal').innerText = score;
        alert(`🎉 زمان‌بندی فوق‌العاده! ولتاژ ثبت‌شده: ${ch3_capVoltage.toFixed(2)}V (هدف: 6.32V در t=τ).`);
    } else {
        playSound('spark');
        updateHealth(-15);
        alert(`❌ خطا در زمان‌بندی! ولتاژ ثبت‌شده: ${ch3_capVoltage.toFixed(2)}V بود. هدف 6.32V در ثابت زمانی τ=2s است.`);
    }
}

// Ch 4 Logic
function onCh4Slider(val) {
    ch4_Rf = parseFloat(val);
    document.getElementById('rfVal').innerText = ch4_Rf + ' kΩ';
}

function checkCh4() {
    // Vin = 0.5V, Rin = 2k. Av = -Rf / Rin => Vo = -Vin * (Rf/Rin)
    // Target Vo magnitude = 5.0V => Rf / 2 = 10 => Rf = 20k
    const Av = ch4_Rf / 2.0;
    const Vo = 0.5 * Av;

    if (Math.abs(Vo - 5.0) < 0.2) {
        playSound('success');
        score += 350;
        updateHealth(25);
        document.getElementById('scoreVal').innerText = score;
        alert(`🎉 بهره خروجی عالی! Av = ${Av.toFixed(1)} و ولتاژ خروجی دقیقا 5.0V بدون برشدگی (Clipping) تنظیم شد.`);
    } else {
        playSound('spark');
        updateHealth(-15);
        addSparks(500, 230);
        alert(`❌ ولتاژ خروجی ${Vo.toFixed(2)}V است. هدف 5.0V می‌باشد (فرمول: Vo = Vin * (Rf / Rin)).`);
    }
}

function addSparks(x, y) {
    for (let i = 0; i < 20; i++) {
        sparks.push({
            x: x,
            y: y,
            vx: (Math.random() - 0.5) * 8,
            vy: (Math.random() - 0.5) * 8,
            life: 1.0
        });
    }
}

// --- Render Loop ---
function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Grid Background
    ctx.strokeStyle = 'rgba(30, 41, 59, 0.4)';
    ctx.lineWidth = 1;
    for (let x = 0; x < canvas.width; x += 40) {
        ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
    }
    for (let y = 0; y < canvas.height; y += 40) {
        ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
    }

    if (currentChapter === 1) {
        renderChapter1();
    } else if (currentChapter === 2) {
        renderChapter2();
    } else if (currentChapter === 3) {
        renderChapter3();
    } else if (currentChapter === 4) {
        renderChapter4();
    }

    // Render Sparks
    for (let i = sparks.length - 1; i >= 0; i--) {
        let p = sparks[i];
        ctx.fillStyle = `rgba(255, 100, 50, ${p.life})`;
        ctx.beginPath();
        ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
        ctx.fill();
        p.x += p.vx;
        p.y += p.vy;
        p.life -= 0.04;
        if (p.life <= 0) sparks.splice(i, 1);
    }

    requestAnimationFrame(render);
}

// Chapter 1 Circuit Rendering
function renderChapter1() {
    const I = 24 / (4 + ch1_Rload);

    // Main Circuit Wire Loop
    ctx.strokeStyle = (I > 2.2) ? '#ef4444' : '#00f2fe';
    ctx.lineWidth = 4;
    ctx.shadowBlur = (I > 2.2) ? 15 : 8;
    ctx.shadowColor = (I > 2.2) ? '#ef4444' : '#00f2fe';

    ctx.beginPath();
    ctx.rect(200, 100, 600, 260);
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Voltage Source (Left)
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(170, 200, 60, 60);
    ctx.strokeStyle = '#38bdf8';
    ctx.strokeRect(170, 200, 60, 60);
    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 16px Vazirmatn';
    ctx.fillText('24V', 183, 235);

    // Source Resistor R_src (Top)
    ctx.fillStyle = '#1e293b';
    ctx.fillRect(350, 85, 80, 30);
    ctx.strokeStyle = '#f59e0b';
    ctx.strokeRect(350, 85, 80, 30);
    ctx.fillStyle = '#f59e0b';
    ctx.font = '13px Vazirmatn';
    ctx.fillText('R_src = 4Ω', 355, 105);

    // Variable Load Resistor R_load (Right)
    ctx.fillStyle = '#1e293b';
    ctx.fillRect(785, 200, 30, 80);
    ctx.strokeStyle = '#10b981';
    ctx.strokeRect(785, 200, 30, 80);
    ctx.fillStyle = '#10b981';
    ctx.fillText(`R_load`, 825, 235);
    ctx.fillText(`${ch1_Rload} Ω`, 825, 255);

    // Ammeter (Bottom Center)
    ctx.fillStyle = '#0284c7';
    ctx.beginPath();
    ctx.arc(500, 360, 25, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#fff';
    ctx.font = 'bold 14px Vazirmatn';
    ctx.fillText(`${I.toFixed(2)} A`, 478, 365);

    // Animated Electrons
    const path = [
        {x: 200, y: 100}, {x: 800, y: 100},
        {x: 800, y: 360}, {x: 200, y: 360}
    ];
    let speed = I * 0.003;
    electrons.forEach(e => {
        e.pos = (e.pos + speed) % 1;
        let pt = getPointOnRect(200, 100, 600, 260, e.pos);
        ctx.fillStyle = '#fbbf24';
        ctx.shadowBlur = 6; ctx.shadowColor = '#fbbf24';
        ctx.beginPath(); ctx.arc(pt.x, pt.y, 4, 0, Math.PI * 2); ctx.fill();
        ctx.shadowBlur = 0;
    });
}

function getPointOnRect(x, y, w, h, t) {
    let perimeter = 2 * (w + h);
    let dist = t * perimeter;
    if (dist < w) return {x: x + dist, y: y};
    dist -= w;
    if (dist < h) return {x: x + w, y: y + dist};
    dist -= h;
    if (dist < w) return {x: x + w - dist, y: y + h};
    dist -= w;
    return {x: x, y: y + h - dist};
}

// Chapter 2 KCL Rendering
function renderChapter2() {
    // Node Circle
    ctx.fillStyle = '#38bdf8';
    ctx.shadowBlur = 12; ctx.shadowColor = '#38bdf8';
    ctx.beginPath(); ctx.arc(500, 230, 20, 0, Math.PI * 2); ctx.fill();
    ctx.shadowBlur = 0;
    ctx.fillStyle = '#000'; ctx.font = 'bold 12px Vazirmatn'; ctx.fillText('KCL Node', 472, 234);

    // Input Wire (Left)
    ctx.strokeStyle = '#00f2fe'; ctx.lineWidth = 5;
    ctx.beginPath(); ctx.moveTo(200, 230); ctx.lineTo(480, 230); ctx.stroke();
    ctx.fillStyle = '#00f2fe'; ctx.font = 'bold 16px Vazirmatn'; ctx.fillText('I_in = 10 A ➔', 250, 215);

    // Output Branches (Right Top, Center, Bottom)
    const branches = [
        {y: 130, val: 4, name: 'A (4A)', active: ch2_switches[0]},
        {y: 230, val: 6, name: 'B (6A)', active: ch2_switches[1]},
        {y: 330, val: 2, name: 'C (2A)', active: ch2_switches[2]}
    ];

    branches.forEach(b => {
        ctx.strokeStyle = b.active ? '#10b981' : '#475569';
        ctx.lineWidth = 4;
        ctx.beginPath(); ctx.moveTo(520, 230); ctx.lineTo(620, b.y); ctx.lineTo(800, b.y); ctx.stroke();

        // Switch box
        ctx.fillStyle = b.active ? '#065f46' : '#1e293b';
        ctx.fillRect(680, b.y - 15, 60, 30);
        ctx.strokeStyle = b.active ? '#34d399' : '#64748b';
        ctx.strokeRect(680, b.y - 15, 60, 30);
        ctx.fillStyle = '#fff'; ctx.font = '12px Vazirmatn';
        ctx.fillText(b.name, 688, b.y + 4);
    });
}

// Chapter 3 RC Capacitor Rendering
function renderChapter3() {
    if (ch3_charging) {
        ch3_time += 0.016; // ~60fps
        ch3_capVoltage = 10 * (1 - Math.exp(-ch3_time / ch3_rcTau));
    }

    // Oscilloscope Screen Box
    ctx.fillStyle = '#040d1a'; ctx.fillRect(150, 80, 700, 300);
    ctx.strokeStyle = '#1e3a8a'; ctx.lineWidth = 2; ctx.strokeRect(150, 80, 700, 300);

    // Osc Grid Lines
    ctx.strokeStyle = 'rgba(30, 58, 138, 0.4)'; ctx.lineWidth = 1;
    for (let x = 150; x <= 850; x += 50) {
        ctx.beginPath(); ctx.moveTo(x, 80); ctx.lineTo(x, 380); ctx.stroke();
    }
    for (let y = 80; y <= 380; y += 50) {
        ctx.beginPath(); ctx.moveTo(150, y); ctx.lineTo(850, y); ctx.stroke();
    }

    // Target 63.2% Line (Tau)
    const targetY = 380 - (6.32 / 10) * 260;
    ctx.strokeStyle = '#f59e0b'; ctx.setLineDash([5, 5]);
    ctx.beginPath(); ctx.moveTo(150, targetY); ctx.lineTo(850, targetY); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = '#f59e0b'; ctx.font = '12px Vazirmatn';
    ctx.fillText('V(τ) = 6.32V (63.2%)', 710, targetY - 6);

    // Live Capacitor Curve
    ctx.strokeStyle = '#00f2fe'; ctx.lineWidth = 3; ctx.beginPath();
    ctx.moveTo(150, 380);
    let pts = Math.min(600, Math.floor(ch3_time * 100));
    for (let i = 0; i <= pts; i++) {
        let t = i / 100;
        let v = 10 * (1 - Math.exp(-t / ch3_rcTau));
        let px = 150 + (t / 6.0) * 700; // 6s span
        let py = 380 - (v / 10.0) * 260;
        ctx.lineTo(px, py);
    }
    ctx.stroke();

    // Readout Display
    ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 18px Vazirmatn';
    ctx.fillText(`زمان (t): ${ch3_time.toFixed(2)}s`, 180, 120);
    ctx.fillText(`ولتاژ خازن (Vc): ${ch3_capVoltage.toFixed(2)} V`, 180, 150);
}

// Chapter 4 Op-Amp Rendering
function renderChapter4() {
    const Av = ch4_Rf / 2.0;
    const Vo = 0.5 * Av;

    // Triangle Op-Amp Symbol
    ctx.fillStyle = '#0f172a'; ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(400, 130); ctx.lineTo(400, 330); ctx.lineTo(600, 230); ctx.closePath();
    ctx.fill(); ctx.stroke();

    ctx.fillStyle = '#fff'; ctx.font = 'bold 20px Vazirmatn';
    ctx.fillText('-', 415, 175);
    ctx.fillText('+', 415, 295);

    // Waveform Input vs Output
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 2; ctx.beginPath();
    for (let x = 150; x < 380; x++) {
        let y = 170 + Math.sin((x - 150) * 0.1) * 15;
        if (x === 150) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();
    ctx.fillStyle = '#10b981'; ctx.font = '12px Vazirmatn'; ctx.fillText('ورودی: Vin = 0.5V', 200, 140);

    // Output Wave
    ctx.strokeStyle = (Vo > 6.0) ? '#ef4444' : '#00f2fe'; ctx.lineWidth = 3; ctx.beginPath();
    for (let x = 600; x < 850; x++) {
        let amp = Math.min(80, Vo * 12);
        let y = 230 - Math.sin((x - 600) * 0.1) * amp; // inverted
        if (x === 600) ctx.moveTo(x, y); else ctx.lineTo(x, y);
    }
    ctx.stroke();

    ctx.fillStyle = '#38bdf8'; ctx.font = 'bold 16px Vazirmatn';
    ctx.fillText(`بهره ولتاژ (Av): -${Av.toFixed(1)}`, 450, 380);
    ctx.fillText(`ولتاژ خروجی (Vo): ${Vo.toFixed(2)} V`, 450, 410);
}

// Start Engine
loadChapter(1);
render();
</script>
</body>
</html>
"""

# Render Game inside Streamlit Application
components.html(game_html, height=710, scrolling=False)

# Footer Info & Formula Reference
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📘 **فرمول فصل ۱ & ۲:**\n* $V = I \\cdot R$\n* KCL: $\\sum I_{in} = \\sum I_{out}$")

with col2:
    st.info("📙 **فرمول فصل ۳ (RC):**\n* $\\tau = R \\cdot C$\n* $v_c(t) = V_{final}(1 - e^{-t/\\tau})$")

with col3:
    st.info("📗 **فرمول فصل ۴ (Op-Amp):**\n* $A_v = - \\frac{R_f}{R_{in}}$\n* $V_o = A_v \\cdot V_{in}$")
