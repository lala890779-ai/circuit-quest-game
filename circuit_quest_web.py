import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(
    page_title="Circuit Quest: Master of Voltages",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark neon engineering theme
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stMetric {
        background-color: #1e222d;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #2e364f;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);
        color: #000000;
        border: none;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #92FE9D 0%, #00C9FF 100%);
        color: #000000;
    }
    .success-box {
        padding: 15px;
        background-color: #1b382b;
        border-left: 5px solid #2ecc71;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .error-box {
        padding: 15px;
        background-color: #3d1c1c;
        border-left: 5px solid #e74c3c;
        border-radius: 5px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'grid_health' not in st.session_state:
    st.session_state.grid_health = 100
if 'completed_levels' not in st.session_state:
    st.session_state.completed_levels = set()

# Header
st.title("⚡ Circuit Quest: Master of Voltages")
st.caption("بازی وب‌محور آموزشی و تعاملی درس مدار الکتریکی و الکترونیکی")

# Sidebar Stats & Navigation
with st.sidebar:
    st.header("📊 وضعیت مهندس")
    col1, col2 = st.columns(2)
    col1.metric("امتیاز (XP)", st.session_state.score)
    col2.metric("پایداری شبکه", f"{st.session_state.grid_health}%")
    
    st.progress(st.session_state.grid_health / 100)
    
    if st.button("🔄 بازنشانی وضعیت بازی"):
        st.session_state.score = 0
        st.session_state.grid_health = 100
        st.session_state.completed_levels = set()
        st.rerun()

    st.divider()
    menu = st.radio(
        "📌 منوی اصلی",
        ["🚀 بخش داستانی (Campaign)", "📚 فصول آموزشی", "🧪 آزمایشگاه تعاملی (Sandbox)", "📖 درس‌نامه و فرمول‌ها"]
    )

# --- Helper Functions for Circuit Diagrams ---
def draw_resistor_circuit(v_val, r1_val, r2_val):
    fig, ax = plt.subplots(figsize=(6, 2.5), facecolor='#1e222d')
    ax.set_facecolor('#1e222d')
    
    # Simple schematic drawing using matplotlib
    ax.plot([0, 0, 2], [0, 2, 2], color='#00C9FF', lw=3) # V to R1
    ax.plot([2, 2.5, 2.7, 2.9, 3.1, 3.3, 3.5, 4], [2, 2.3, 1.7, 2.3, 1.7, 2.3, 2, 2], color='#92FE9D', lw=3) # R1
    ax.text(3, 2.5, f"R1 = {r1_val}Ω", color="white", fontsize=11, ha='center')
    
    ax.plot([4, 4.5, 4.7, 4.9, 5.1, 5.3, 5.5, 6], [2, 2.3, 1.7, 2.3, 1.7, 2.3, 2, 2], color='#FFD700', lw=3) # R2
    ax.text(5, 2.5, f"R2 = {r2_val}Ω", color="white", fontsize=11, ha='center')
    
    ax.plot([6, 8, 8, 0], [2, 2, 0, 0], color='#00C9FF', lw=3) # Wire back
    
    # DC Source symbol
    ax.add_patch(plt.Circle((0, 1), 0.4, color='#00C9FF', fill=False, lw=3))
    ax.text(0, 1, f"{v_val}V", color="white", fontsize=11, ha='center', va='center')
    
    ax.set_xlim(-1, 9)
    ax.set_ylim(-0.5, 3.5)
    ax.axis('off')
    return fig

# --- App Views ---
if menu == "🚀 بخش داستانی (Campaign)":
    st.subheader("🏙️ سناریوی داستان: نجات شهر ElectroCity")
    st.info("شبکه اصلی برق و سیگنالینگ شهر دچار اختلال شده است. با حل پازل‌های مداری، شبکه را به حالت پایدار برگردانید!")
    
    # Level 1
    st.markdown("### 🔹 مرحله ۱: تنظیم جریان مدار سری (قانون اهم)")
    fig1 = draw_resistor_circuit(v_val=20, r1_val=10, r2_val="?")
    st.pyplot(fig1)
    
    st.write("**مسئله:** ولتاژ منبع 20V و مقاومت اول R1 = 10Ω است. مقاومت دوم (R2) چقدر باشد تا جریان کل مدار **0.8 آمپر** شود؟")
    
    ans1 = st.number_input("مقدار R2 به اوم (Ω):", min_value=0.0, max_value=100.0, value=0.0, step=0.5, key="q1")
    if st.button("ثبت پاسخ مرحله ۱"):
        if abs(ans1 - 5.0) < 0.1:
            st.markdown("<div class='success-box'>✅ <b>عالی بود!</b> R_total = 20/0.8 = 25Ω -> R2 = 25 - 10 = 5Ω</div>", unsafe_allow_html=True)
            if "l1" not in st.session_state.completed_levels:
                st.session_state.score += 100
                st.session_state.completed_levels.add("l1")
                st.rerun()
        else:
            st.markdown("<div class='error-box'>❌ <b>نادرست!</b> فرمول: R_total = V / I = 20 / 0.8 = 25Ω -> R2 = 25 - 10 = 5Ω</div>", unsafe_allow_html=True)
            st.session_state.grid_health = max(0, st.session_state.grid_health - 15)

elif menu == "📚 فصول آموزشی":
    st.subheader("📚 انتخاب فصل آموزشی")
    chapter = st.selectbox("یک فصل را انتخاب کنید:", [
        "فصل ۱: قانون اهم و شبکه‌های مقاومتی",
        "فصل ۲: قوانین کیرشلوف (KVL/KCL) و قضیه تونن",
        "فصل ۳: خازن و سلف (پاسخ گذرا RC/RL)",
        "فصل ۴: الکترونیک آنالوگ (Op-Amp و ترانزیستور)"
    ])
    
    if "فصل ۱" in chapter:
        st.write("#### 💡 یادگیری تقسیم ولتاژ")
        v_in = st.slider("ولتاژ ورودی (V):", 1, 50, 12)
        r1 = st.slider("مقاومت R1 (kΩ):", 1, 20, 4)
        r2 = st.slider("مقاومت R2 (kΩ):", 1, 20, 8)
        
        v_out = v_in * (r2 / (r1 + r2))
        st.success(f"⚡ ولتاژ خروجی روی R2 برابر است با: **{v_out:.2f} ولت**")

elif menu == "🧪 آزمایشگاه تعاملی (Sandbox)":
    st.subheader("🧪 آزمایشگاه آنلاین مدار")
    tool = st.radio("ابزار محاسباتی:", ["محاسبه مقاومت معادل", "محاسبه ثابت زمانی RC", "محاسبه بهره Op-Amp"])
    
    if tool == "محاسبه مقاومت معادل":
        r1 = st.number_input("R1 (Ω):", value=10.0)
        r2 = st.number_input("R2 (Ω):", value=20.0)
        mode = st.radio("نوع اتصال:", ["سری", "موازی"])
        if mode == "سری":
            st.write(f"**مقاومت معادل:** {r1 + r2:.2f} Ω")
        else:
            r_par = (r1 * r2) / (r1 + r2) if (r1 + r2) > 0 else 0
            st.write(f"**مقاومت معادل:** {r_par:.2f} Ω")
            
    elif tool == "محاسبه ثابت زمانی RC":
        r_k = st.number_input("مقاومت R (kΩ):", value=10.0)
        c_u = st.number_input("خازن C (µF):", value=100.0)
        tau = (r_k * 1000) * (c_u * 1e-6)
        st.info(f"⏱️ **ثابت زمانی (Tau = R × C):** {tau:.4f} ثانیه")

elif menu == "📖 درس‌نامه و فرمول‌ها":
    st.subheader("📖 خلاصه فرمول‌های کلیدی")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        #### ⚡ مدار الکتریکی ۱
        * **قانون اهم:** $V = I \\cdot R$
        * **تقسیم ولتاژ:** $V_{R2} = V_{in} \\cdot \\frac{R_2}{R_1 + R_2}$
        * **تقسیم جریان:** $I_{R1} = I_{total} \\cdot \\frac{R_2}{R_1 + R_2}$
        * **ثابت زمانی RC:** $\\tau = R \\cdot C$
        """)
    with col2:
        st.markdown("""
        #### 🔌 الکترونیک آنالوگ
        * **بهره Op-Amp معکوس‌کننده:** $A_v = -\\frac{R_f}{R_{in}}$
        * **بهره Op-Amp غیرمعکوس‌کننده:** $A_v = 1 + \\frac{R_f}{R_{in}}$
        * **رابطه ترانزیستور BJT:** $I_C = \\beta \\cdot I_B$
        """)
