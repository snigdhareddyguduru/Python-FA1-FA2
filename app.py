# --- WATERBUDDY APP PART 1 ---
# By Snigdha :) 💧

import streamlit as st  # we’re using streamlit for the web app
import random
from datetime import datetime

# ---------- SIDEBAR (always visible) ----------
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3104/3104941.png",
    caption="Stay hydrated 💧",
    use_container_width=True
)

side_tips = [
    "Keep a water bottle with you while studying.",
    "Start your day with a full glass of water.",
    "Set hourly reminders to sip 150–200 ml.",
    "Add cucumber or lemon slices for taste.",
    "Take a sip when switching tasks to refresh your focus.",
    "Pair a glass of water with every snack or meal.",
    "Keep a small bottle on your bedside table for morning sips.",
    "Try chilled water after exercise to cool down safely.",
    "Use a bottle with measurements to track progress visually.",
    "Drink a small glass before and after screen time breaks."
]

# pick 3 different tips randomly and show each as a blue popup
import random as _rand  # local alias so we don't clash with other imports
_chosen = _rand.sample(side_tips, k=3) if len(side_tips) >= 3 else side_tips
for t in _chosen:
    st.sidebar.info(t)

# 1️⃣ Set the title of the app
st.title("💧 WaterBuddy — Your Daily Hydration Companion")

# 2️⃣ Add a short sentence below the title
st.write("Track your daily water intake and stay hydrated every day!")

# Time-based greeting
now = datetime.now()
hour = now.hour

if hour < 12:
    greeting = "Good morning ☀️"
elif hour < 18:
    greeting = "Good afternoon 🌤"
else:
    greeting = "Good evening 🌙"

st.write(f"{greeting}! Let's stay hydrated today 💧")

# 3️⃣ Create a dropdown to select the user’s age group
age_group = st.selectbox(
    "Select your age group:",
    ["6–12 years", "13–18 years", "19–50 years", "65+ years"]
)

# 4️⃣ Set daily water goal (in ml) depending on age
if age_group == "6–12 years":
    daily_goal = 1600
elif age_group == "13–18 years":
    daily_goal = 2000
elif age_group == "19–50 years":
    daily_goal = 2500
else:
    daily_goal = 2000

# 5️⃣ Let users adjust the goal if they want
daily_goal = st.number_input(
    "Set your daily goal (ml):",
    min_value=1000,
    max_value=5000,
    step=100,
    value=daily_goal
)

# 6️⃣ Display the final goal
st.success(f"Your daily hydration goal is **{daily_goal} ml** 💧")

# --- WATERBUDDY APP PART 2 ---
# Continue building from Part 1

# 7️⃣ Add buttons for quick water logging
st.markdown("---")
st.subheader("Log your water intake:")

# Ensure session_state total exists
if "total_intake" not in st.session_state:
    st.session_state.total_intake = 0

# Create 3 columns for buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("+100 ml"):
        st.session_state.total_intake += 100
with col2:
    if st.button("+250 ml"):
        st.session_state.total_intake += 250
with col3:
    if st.button("+500 ml"):
        st.session_state.total_intake += 500

# 8️⃣ Add custom input option
custom_amount = st.number_input("Or add a custom amount (ml):", min_value=0, step=50)
if st.button("Add custom amount"):
    st.session_state.total_intake += custom_amount

# 9️⃣ Add reset button
if st.button("Reset for today 🔄"):
    st.session_state.total_intake = 0
    st.success("Reset done — today's intake is now 0 ml.")

# 🔟 Calculate progress
st.markdown("---")
st.subheader("Your progress today 💧")

# safe calculation of progress
try:
    progress = st.session_state.total_intake / float(daily_goal)
except Exception:
    progress = 0.0

if progress > 1:
    progress = 1  # cap it at 100%

st.progress(progress)
st.write(f"Total water consumed: {st.session_state.total_intake} ml")
st.write(f"Remaining: {max(0, daily_goal - st.session_state.total_intake)} ml")

# 🎉 Motivational messages
if progress >= 1:
    st.balloons()
    st.success("Amazing job! You've reached your daily goal! 🥳")
elif progress >= 0.75:
    st.info("Almost there! Keep sipping! 💦")
elif progress >= 0.5:
    st.write("Halfway there — great job! 👏")
else:
    st.write("Keep going — small sips add up! 💧")

# ---------- END-OF-DAY SUMMARY (Expanded Version) ----------
st.markdown("---")
st.subheader("End-of-day summary 🕓")

total = st.session_state.total_intake
goal = daily_goal
percent = round((total / goal) * 100, 1) if goal > 0 else 0

st.write(f"### 📊 Hydration Report for Today")
st.write(f"- **Goal:** {goal} ml")
st.write(f"- **Total consumed:** {total} ml")
st.write(f"- **You achieved:** {percent}% of your goal")

# Give detailed feedback and recommendations
if percent >= 120:
    st.balloons()
    st.success("💦 Incredible! You drank **more than enough** today! Remember, balance is key — overhydration isn’t ideal either. Slow down a bit tomorrow. 😊")
    next_goal = goal
elif 100 <= percent < 120:
    st.balloons()
    st.success("🎉 Perfect! You met your goal and stayed well-hydrated. Keep this streak going tomorrow! 💪")
    next_goal = goal
elif 80 <= percent < 100:
    st.info("🌤 Almost there! You reached **most** of your goal. Try keeping a bottle nearby tomorrow — small sips more often will get you to 100%! 💧")
    next_goal = goal + 100
elif 50 <= percent < 80:
    st.warning("🌈 You got **halfway** through your goal. You can do better tomorrow — maybe set reminders every few hours or pair each meal with a drink. 🕒")
    next_goal = goal + 200
else:
    st.error("🚰 You drank **very little** today. Dehydration can make you tired and affect focus. Aim to double your intake tomorrow and start your day with a big glass of water! 💧")
    next_goal = goal + 300

# Display a simple "hydration score"
hydration_score = min(int(percent), 120)
st.markdown(f"### 💧 Hydration Score: {hydration_score}/120")

# Add daily tip of the day
daily_tips = [
    "✅ Refill your bottle every time you check your phone.",
    "💙 Eat water-rich fruits like watermelon or oranges.",
    "⏰ Set hourly reminders to sip 150–200 ml.",
    "🌿 Add a slice of lemon or mint to make water more exciting.",
    "💧 Keep a small bottle beside your bed for morning hydration."
]
st.info(f"**Tip for tomorrow:** {random.choice(daily_tips)}")

# Suggest next day's goal and encouragement
st.markdown("---")
st.write(f"### 🔮 Suggested goal for tomorrow: **{next_goal} ml**")
if percent >= 100:
    st.write("✨ Fantastic! Try to maintain consistency — hydration habits matter more than single-day goals.")
elif 80 <= percent < 100:
    st.write("💫 You’re close! Tomorrow, aim to close that last gap and celebrate your full target.")
else:
    st.write("🚀 Let’s push a little harder tomorrow. Small changes = big results!")

# Closing message
st.markdown("---")
st.caption("Made with 💧 by Snigdha Reddy — FA2 Python Project 2025")
