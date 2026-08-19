import streamlit as st
import time
st.config.set_option("theme.backgroundColor", "#c2f6c0")
st.config.set_option("theme.textColor", "#c1051b")

# 1. Page Configuration & Theme Vibe
st.set_page_config(
    page_title="Happy Birthday!",
    page_icon="🎉",
    layout="centered"
)

# 2. Custom Styling
st.markdown("""
    <style>
    .big-title {
        font-size: 50px !important;
        font-weight: bold;
        color: ce1c1c;
        text-align: center;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 24px;
        text-align: center;
        color: #c1051b;
        margin-bottom: 30px;
    }
    .card {
        background-color: #FFF0F5;
        padding: 30px;
        border-radius: 15px;
        border: 2px dashed #FF69B4;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. The Front of the Card
st.markdown('<p class="big-title">🎂 HAPPY BIRTHDAY! 🎂</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">This is an interactive digital card<3 </p>', unsafe_allow_html=True)

# 4. Floating Balloons Trigger
if st.button("🎈 Click to Release Balloons", use_container_width=True):
    st.balloons()
    st.toast("Yay! Happy Birthday! 🎉")
    st.toast("Thank you for always being with us!")
    st.toast("We Love You")
    st.toast("We'll choose you over again and again to be our mother")
    st.toast("We're lucky to have you.")
    st.toast("I hope you enjoy your day.")

# 5. Unwrapping the Gift Box
st.subheader("🎁 Open it, 'Cause why not")
gift_opened = st.toggle("click to open!")

if gift_opened:
    with st.spinner("wait a minute..."):
        time.sleep(1)

    st.markdown("""
    <div class="card">
        <h3>✨ A Message for You ✨</h3>
        <p style="font-size: 18px; line-height: 1.6;">
            "Happy Birthday Nanay. Thank you for everything. 
            For giving birth to us, for being both our mother and father figure, for doing anything for our survival,
            and for always being on our side. I'm sorry if I'm not the daughter you needed. 
            I love you, and I hope you happiness for this day."
        </p>
        <h1 style="font-size: 60px; margin: 10px 0;">🍰🍕🎁🍟🎸</h1>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    mood = st.feedback("stars")
    if mood is not None:
        st.success(f"Awesome! You rated this card {mood + 1} stars! 😊")
else:
    st.info("☝️ Turn on Green")

st.divider()

# 6. Device Photo Slideshow Setup
# Update file paths and captions to match the photos inside your images folder
slides = [
    {
        "image": "hbd/1.jpg"
    },
    {
        "image": "hbd/2.jpg"
    },
    {
        "image": "hbd/3.jpg"
    },
    {
        "image": "hbd/4.jpg"
    },
    {
        "image": "hbd/5.jpg"
    },
    {
        "image": "hbd/6.jpg"
    },
    {
        "image": "hbd/7.jpg"
    },
    {
        "image": "hbd/8.jpg"
    },
    {
        "image": "hbd/9.jpg"
    },
    {
        "image": "hbd/10.jpg"
    },
    {
        "image": "hbd/11.jpg"
    },
    {
        "image": "hbd/12.jpg"
    },
    {
        "image": "hbd/13.jpg"
    },
    {
        "image": "hbd/14.jpg"
    },
    {
        "image": "hbd/15.jpg"
    },
    {
        "image": "hbd/16.jpg"
    },
    {
        "image": "hbd/17.jpg"
    },
    {
        "image": "hbd/18.jpg"
    },
    {
        "image": "hbd/19.jpg"
    },
    {
        "image": "hbd/20.jpg"
    },
    {
        "image": "hbd/21.jpg"
    },
    {
        "image": "hbd/22.jpg"
    },
    {
        "image": "hbd/23.jpg"
    },
    {
        "image": "hbd/24.jpg"
    },
    {
        "image": "hbd/25.jpg"
    },
    {
        "image": "hbd/26.jpg"
    },
    {
        "image": "hbd/27.jpg"
    },
    {
        "image": "hbd/28.jpg"
    },
    {
        "image": "hbd/29.jpg"
    },
    {
        "image": "hbd/30.jpg"
    }
]

# 7. Initialize Session State for Slideshow
if "current_slide" not in st.session_state:
    st.session_state.current_slide = 0

current_index = st.session_state.current_slide

# 8. Render Current Image
with st.container():
    st.image(
        slides[current_index]["image"],
        use_container_width=True
    )

# 9. Slideshow Navigation Buttons with Automatic Looping
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("👈 Previous", use_container_width=True):
        # Wrap around to the last slide (29) if pressed on slide 0
        st.session_state.current_slide = (st.session_state.current_slide - 1) % len(slides)
        st.rerun()

with col2:
    st.markdown(
        f"<p style='text-align: center; font-weight: bold;'>Slide {current_index + 1} of {len(slides)}</p>",
        unsafe_allow_html=True
    )

with col3:
    if st.button("Next 👉", use_container_width=True):
        # Wrap around to the first slide (0) if pressed on slide 29
        st.session_state.current_slide = (st.session_state.current_slide + 1) % len(slides)
        st.rerun()