def calculate_budget(income, expenses):

    # ================================
    # 📊 BASIC CALCULATIONS
    # ================================
    total_expenses = sum(expenses.values())
    savings = income - total_expenses
    savings_rate = (savings / income) * 100 if income > 0 else 0

    # ================================
    # 🧠 FINANCIAL ANALYSIS ENGINE
    # ================================
    advice = []

    # 1. Spending status
    if savings < 0:
        advice.append("⚠️ CRITICAL: You are spending more than you earn. Immediate cost reduction is required.")
    elif savings_rate < 10:
        advice.append("⚠️ WARNING: Very low savings rate. You are financially vulnerable.")
    elif savings_rate < 20:
        advice.append("📊 MODERATE: You are okay but still need better control of expenses.")
    else:
        advice.append("✅ GOOD: You have strong financial discipline.")

    # 2. Identify spending behavior
    highest_category = max(expenses, key=expenses.get)
    highest_value = expenses[highest_category]

    advice.append(
        f"📌 Biggest expense is '{highest_category}' ({highest_value:.2f}). This is your priority area to reduce."
    )

    # 3. Waste detection (small unnecessary expenses)
    small_spends = [k for k, v in expenses.items() if v < income * 0.05 and v > 0]

    if small_spends:
        advice.append(
            f"🧾 Small recurring expenses detected: {', '.join(small_spends)}. These may look small but add up over time."
        )

    # 4. Smart next-month planning (VERY IMPORTANT)
    recommended_savings = income * 0.2
    remaining_budget = income - recommended_savings
    per_category_budget = remaining_budget / len(expenses)

    advice.append(
        f"📅 NEXT MONTH PLAN: Aim to save at least {recommended_savings:.2f}. "
        f"Limit each expense category to around {per_category_budget:.2f}."
    )

    # 5. Emergency insight
    if savings_rate < 5:
        advice.append("🚨 EMERGENCY: You are at high financial risk. Consider reducing fixed costs (housing, transport).")

    # ================================
    # RETURN RESULTS
    # ================================
    return total_expenses, savings, savings_rate, "\n".join(advice)