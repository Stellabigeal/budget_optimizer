# ================================
# 🌍 SMART PERSONAL BUDGET OPTIMIZER 
# ================================

import streamlit as st
from budget_logic import calculate_budget
import matplotlib.pyplot as plt

# ================================
# 🎯 PAGE CONFIGURATION
# ================================
st.set_page_config(
    page_title="Budget Optimizer",
    layout="wide"
)

# ================================
# 🏠 HEADER
# ================================
st.title("🌍 Smart Personal Budget Optimizer")
st.write("AI-style financial advisor that helps you plan, reduce, and optimize spending.")

# ================================
# 💰 INPUT SECTION
# ================================
currency = st.text_input("Currency Symbol (e.g $, €, ₦)", "$")

col1, col2 = st.columns(2)

with col1:
    income = st.number_input("Monthly Income", min_value=0.0)

with col2:
    st.subheader("Expenses")
    housing = st.number_input("Housing")
    food = st.number_input("Food")
    transport = st.number_input("Transport")

internet = st.number_input("Internet")
entertainment = st.number_input("Entertainment")
other = st.number_input("Other Expenses")

# ================================
# 🧠 EXPENSE STRUCTURE
# ================================
expenses = {
    "Housing": housing,
    "Food": food,
    "Transport": transport,
    "Internet": internet,
    "Entertainment": entertainment,
    "Other": other
}

# ================================
# 🔘 ANALYZE BUTTON
# ================================
if st.button("Analyze My Finances"):

    total, savings, rate, advice_text = calculate_budget(income, expenses)

    # ================================
    # 📊 FINANCIAL DASHBOARD
    # ================================
    st.subheader("📊 Financial Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Income", f"{currency}{income}")
    col2.metric("Expenses", f"{currency}{total}")
    col3.metric("Savings", f"{currency}{savings}")

    st.info(f"Savings Rate: {rate:.2f}%")

    # ================================
    # 🧠 AI FINANCIAL ADVISOR REPORT
    # ================================
    st.subheader("🤖 Financial Advisor Report")

    advice_list = advice_text.split("\n")

    for item in advice_list:
        if "CRITICAL" in item or "EMERGENCY" in item:
            st.error(item)
        elif "WARNING" in item:
            st.warning(item)
        elif "GOOD" in item:
            st.success(item)
        elif "MODERATE" in item:
            st.info(item)
        else:
            st.write(item)

    # ================================
    # 📅 NEXT MONTH PLANNING SECTION
    # ================================
    st.subheader("📅 Next Month Budget Plan")

    recommended_savings = income * 0.2
    remaining_budget = income - recommended_savings
    per_category_budget = remaining_budget / len(expenses)

    st.write(f"🎯 Recommended Savings Target: {currency}{recommended_savings:.2f}")
    st.write(f"📊 Suggested Budget Per Category: {currency}{per_category_budget:.2f}")

    # ================================
    # 📈 VISUALIZATION
    # ================================
    st.subheader("Expense Breakdown")

    labels = list(expenses.keys())
    values = list(expenses.values())

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.set_title("Spending Distribution")

    st.pyplot(fig)

    st.subheader("Income vs Expenses")

    fig2, ax2 = plt.subplots()
    ax2.bar(["Income", "Expenses"], [income, total])
    ax2.set_title("Financial Comparison")

    st.pyplot(fig2)