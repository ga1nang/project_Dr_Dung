# import matplotlib.pyplot as plt
# import streamlit as st
# import numpy as np
# from scipy.interpolate import make_interp_spline

# def calculate_assumtion1(target, years, annual_rate):
#     res = 0
#     for i in range(years):
#       res += ((1 + annual_rate)**(years - i))
#     return target / res

# def test_calculate_assumtion1(x, years, annual_rate):
#     res = 0
#     x_lst = []
#     sum_lst = []
#     x_lst.append(x)
#     sum_lst.append(x)
#     if x > 1:
#         for i in range(years):
#             x_lst.append(x)
#             sum_lst(sum_lst[-1]*(1 + annual_rate) + x_lst[i])

#     sum_lst.append(sum_lst[years - 1]*1.05)
#     return x_lst, sum_lst

# def calculate_assumtion3(target, years, annual_rate, increase_investment_rate):
#     res = 0
#     investment_rate = 1
#     total_rate = investment_rate
#     for i in range(years):
#         res += ((1 + annual_rate)**(years - i) * investment_rate)
#         investment_rate *= (1 + increase_investment_rate)

#     return target / res

# def test_calculate_assumtion3(x, years, annual_rate, increase_investment_rate):
#     res = 0
#     investment_rate = 1
#     total_rate = investment_rate
#     x_lst = []
#     sum_lst = []
#     x_lst.append(x)
#     sum_lst.append(x)
    
#     if years > 1:
#         for i in range(1, years):
#             x *= (1 + increase_investment_rate)
#             x_lst.append(x)
#             sum_lst.append(sum_lst[i - 1]*1.05 + x_lst[i])

#     sum_lst.append(sum_lst[years - 1]*1.05)
#     return x_lst, sum_lst


# # Streamlit app
# st.title("Wealth Development Calculator")

# # User inputs
# target = st.number_input("Target Wealth (€)", min_value=0.0, value=1500.0, step=100.0)
# years = st.number_input("Investment Period (years)", min_value=1, value=6, step=1)
# annual_rate = st.number_input("Annual Growth Rate (%)", min_value=0.0, value=5.0, step=0.1) / 100
# increase_investment_rate = st.number_input("Annual Increase in Investment Rate (%)", min_value=0.0, value=10.0, step=0.1) / 100

# # Calculate annual investment needed
# annual_investment = calculate_assumtion3(target, years, annual_rate, increase_investment_rate)

# # Display calculated annual investment
# st.write(f"Calculated Annual Investment: {annual_investment:.2f} €")

# # Calculate investment growth and plot the graph
# x_lst, res_lst = test_calculate_assumtion3(annual_investment, years, annual_rate, increase_investment_rate)
# y_limit = res_lst[-1] + 200
# x = np.array(range(years + 1))
# res_lst = np.array(res_lst)

# # Plotting
# fig, ax = plt.subplots(figsize=(12, 8))  # Set figure size to expand the graph
# ax.plot(x, res_lst, label="Investment Growth")
# ax.scatter(x, res_lst, color='red')  # Show original data points
# ax.set_ylim(0, y_limit)  # Setting y-axis limit
# ax.set_xlabel("Years")
# ax.set_ylabel("Wealth (€)")
# ax.set_title("Development of Wealth Over Time")
# ax.legend()
# ax.grid(True)

# # Annotate each original data point with the corresponding y-value
# for i, value in enumerate(res_lst):
#     ax.annotate(f"{value:.2f}", (x[i], res_lst[i]), textcoords="offset points", xytext=(0, 5), ha='center')

# plt.tight_layout()  # Adjust layout to use space more effectively

# # Display the plot in Streamlit
# st.pyplot(fig)
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

# def calculate_assumtion2(target, years, annual_rate, increase_rate):
#     res = 0
#     for i in range(years):
#       res += ((1 + annual_rate)**(years - i))
#       annual_rate += increase_rate
#     return target / res

# def test_calculate_assumtion2(x, years, annual_rate, increase_rate):
#     res = 0
#     x_lst = []
#     sum_lst = []
#     x_lst.append(x)
#     sum_lst.append(x)
#     if years > 1:
#         for i in range(1, years):
#             x_lst.append(x)
#             sum_lst.append(sum_lst[-1] * (1 + annual_rate) + x_lst[i])
#             annual_rate += increase_rate
#             print(annual_rate, end=' ')

#     sum_lst.append(sum_lst[years - 1] * (1 + annual_rate))
#     return x_lst, sum_lst

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

# Streamlit app
st.title("Wealth Development Calculator")

# User inputs
target = st.number_input("Target Wealth (€)", min_value=0.0, value=1500.0, step=100.0)
years = st.number_input("Investment Period (years)", min_value=1, value=6, step=1)
annual_rate = st.number_input("Annual Growth Rate (%)", min_value=0.0, value=5.0, step=0.1) / 100
increase_investment_rate = st.number_input("Annual Increase in Investment Rate (%)", min_value=0.0, value=10.0, step=0.1) / 100

# Calculate annual investment needed for both assumptions
annual_investment_assumption1 = calculate_assumtion1(target, years, annual_rate)
annual_investment_assumption3 = calculate_assumtion3(target, years, annual_rate, increase_investment_rate)

# Display calculated annual investments
st.write(f"Calculated Annual Investment for Assumption 1: {annual_investment_assumption1:.2f} €")
st.write(f"Calculated Annual Investment for Assumption 3: {annual_investment_assumption3:.2f} €")

# Calculate investment growth for both assumptions
x_lst1, res_lst1 = test_calculate_assumtion1(annual_investment_assumption1, years, annual_rate)
x_lst3, res_lst3 = test_calculate_assumtion3(annual_investment_assumption3, years, annual_rate, increase_investment_rate)

# Determine y-axis limit based on the maximum value from both assumptions
y_limit = max(max(res_lst1), max(res_lst3)) + 200

# Create an array for years
x = np.array(range(years + 1))

# Convert results to numpy arrays
res_lst1 = np.array(res_lst1)
res_lst3 = np.array(res_lst3)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))  # Set figure size to expand the graph
ax.plot(x, res_lst1, label="Investment Growth (Assumption 1)", linestyle='--')
ax.plot(x, res_lst3, label="Investment Growth (Assumption 3)", linestyle='-')
ax.scatter(x, res_lst1, color='blue')  # Show original data points for Assumption 1
ax.scatter(x, res_lst3, color='red')  # Show original data points for Assumption 3
ax.set_ylim(0, y_limit)  # Setting y-axis limit
ax.set_xlabel("Years")
ax.set_ylabel("Wealth (€)")
ax.set_title("Development of Wealth Over Time")
ax.legend()
ax.grid(True)

# Annotate each original data point with the corresponding y-value for both assumptions
for i, value in enumerate(res_lst1):
    ax.annotate(f"{value:.2f}", (x[i], res_lst1[i]), textcoords="offset points", xytext=(0, 5), ha='center', color='blue')

for i, value in enumerate(res_lst3):
    ax.annotate(f"{value:.2f}", (x[i], res_lst3[i]), textcoords="offset points", xytext=(0, 5), ha='center', color='red')

plt.tight_layout()  # Adjust layout to use space more effectively

# Display the plot in Streamlit
st.pyplot(fig)
