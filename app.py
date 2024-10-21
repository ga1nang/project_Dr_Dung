import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

def calculate_assumtion1(target, years, annual_rate):
    res = 0
    for i in range(years):
        res += ((1 + annual_rate)**(years - i))
    return target / res

def test_calculate_assumtion1(x, years, annual_rate):
    res = 0
    x_lst = []
    sum_lst = []
    x_lst.append(x)
    sum_lst.append(x)
    if years > 1:
        for i in range(1, years):
            x_lst.append(x)
            sum_lst.append(sum_lst[-1] * (1 + annual_rate) + x_lst[i])

    sum_lst.append(sum_lst[years - 1] * (1 + annual_rate))
    return x_lst, sum_lst

def calculate_assumtion3(target, years, annual_rate, increase_investment_rate):
    res = 0
    investment_rate = 1
    total_rate = investment_rate
    for i in range(years):
        res += ((1 + annual_rate)**(years - i) * investment_rate)
        investment_rate *= (1 + increase_investment_rate)

    return target / res

def test_calculate_assumtion3(x, years, annual_rate, increase_investment_rate):
    res = 0
    investment_rate = 1
    total_rate = investment_rate
    x_lst = []
    sum_lst = []
    x_lst.append(x)
    sum_lst.append(x)
    
    if years > 1:
        for i in range(1, years):
            x *= (1 + increase_investment_rate)
            x_lst.append(x)
            sum_lst.append(sum_lst[i - 1] * 1.05 + x_lst[i])

    sum_lst.append(sum_lst[years - 1] * 1.05)
    return x_lst, sum_lst

def calculate_assumption4(target, years, annual_rate, increase_investment_rate, inflation_rate):
    res = 0
    effective_rate = (1 + annual_rate) / (1 + inflation_rate) - 1
    effective_investment_rate = (1 + increase_investment_rate) / (1 + inflation_rate)
    for i in range(years):
        res += ((1 + effective_rate)**(years - i) * (effective_investment_rate**i))

    return target / res

def test_calculate_assumtion4(x, years, annual_rate, increase_investment_rate, inflation_rate):
    investment_rate = 1
    x_lst = []
    sum_lst = []
    x_lst.append(x)
    sum_lst.append(x)
    effective_rate = (1 + annual_rate) / (1 + inflation_rate) - 1
    effective_investment_rate = (1 + increase_investment_rate) / (1 + inflation_rate) - 1

    for i in range(1, years):
        x *= ((1 + effective_investment_rate))
        x_lst.append(x)

        new_sum = sum_lst[i - 1] * (1 + effective_rate) + x_lst[i]
        sum_lst.append(new_sum)

    final_sum = sum_lst[-1] * (1 + annual_rate) / (1 + inflation_rate)
    sum_lst.append(final_sum)

    return x_lst, sum_lst

# Streamlit app
st.title("Wealth Development Calculator")

# User inputs
years = st.number_input("Time horizon", min_value=1, value=6, step=1)
annual_rate = st.number_input("Interest rate", min_value=0.0, value=5.0, step=0.1) / 100
increased_annual_rate = st.number_input("Increase rate of interest", min_value=0.0, value=2.0, step=0.1) / 100
init_wealth = st.number_input("Initial Wealth", min_value=0.0, value=0.0, step=100.0)
target = st.number_input("Amount of wealth  needed to be accumulated", min_value=0.0, value=1500.0, step=100.0)
increase_investment_rate = st.number_input("Increase rate of one-off investment", min_value=0.0, value=10.0, step=0.1) / 100
inflation_rate = st.number_input("Inflation Rate", min_value=0.0, value=3.0, step=0.1) / 100
increased_inflation_rate = st.number_input("Increase rate of inflation", min_value=0.0, value=3.0, step=0.1) / 100

# Calculate annual investments for each assumption
annual_investment_assumption1 = calculate_assumtion1(target, years, annual_rate)
annual_investment_assumption3 = calculate_assumtion3(target, years, annual_rate, increase_investment_rate)
annual_investment_assumption4 = calculate_assumption4(target, years, annual_rate, increase_investment_rate, inflation_rate)

# Display calculated annual investments
st.write(f"Saving Amount Every Year: {annual_investment_assumption1:.2f} €")
st.write(f"Increase Rate of One-off Investment: {annual_investment_assumption3:.2f} €")
st.write(f"Increase Rate of One-off Investment with inflation: {annual_investment_assumption4:.2f} €")

# Calculate investment growth for all assumptions
x_lst1, res_lst1 = test_calculate_assumtion1(annual_investment_assumption1, years, annual_rate)
x_lst3, res_lst3 = test_calculate_assumtion3(annual_investment_assumption3, years, annual_rate, increase_investment_rate)
x_lst4, res_lst4 = test_calculate_assumtion4(annual_investment_assumption4, years, annual_rate, increase_investment_rate, inflation_rate)

# Determine y-axis limit based on the maximum value from all assumptions
y_limit = max(max(res_lst1), max(res_lst3), max(res_lst4)) + 200

# Create an array for years
x = np.array(range(years + 1))

# Convert results to numpy arrays
res_lst1 = np.array(res_lst1)
res_lst3 = np.array(res_lst3)
res_lst4 = np.array(res_lst4)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))  # Set figure size to expand the graph
ax.plot(x, res_lst1, label="Investment Growth (Assumption 1)", linestyle='--')
ax.plot(x, res_lst3, label="Investment Growth (Assumption 3)", linestyle='-')
ax.plot(x, res_lst4, label="Investment Growth (Assumption 4)", linestyle='-.')
ax.scatter(x, res_lst1, color='blue')  # Show original data points for Assumption 1
ax.scatter(x, res_lst3, color='red')   # Show original data points for Assumption 3
ax.scatter(x, res_lst4, color='green') # Show original data points for Assumption 4
ax.set_ylim(0, y_limit)  # Setting y-axis limit
ax.set_xlabel("Years")
ax.set_ylabel("Wealth (€)")
ax.set_title("Development of Wealth Over Time")
ax.legend()
ax.grid(True)

# Annotate each original data point with the corresponding y-value for all assumptions
for i, value in enumerate(res_lst1):
    ax.annotate(f"{value:.2f}", (x[i], res_lst1[i]), textcoords="offset points", xytext=(0, 5), ha='center', color='blue')

for i, value in enumerate(res_lst3):
    ax.annotate(f"{value:.2f}", (x[i], res_lst3[i]), textcoords="offset points", xytext=(0, 5), ha='center', color='red')

for i, value in enumerate(res_lst4):
    ax.annotate(f"{value:.2f}", (x[i], res_lst4[i]), textcoords="offset points", xytext=(0, 5), ha='center', color='green')

plt.tight_layout()  # Adjust layout to use space more effectively

# Display the plot in Streamlit
st.pyplot(fig)
