document.getElementById("investmentForm").addEventListener("input", calculateInvestment);

let chart; // Declare the chart variable outside the function

function calculateInvestment() {
    const timeHorizon = parseFloat(document.getElementById("timeHorizon").value);
    const interestRateInput = parseFloat(document.getElementById("interestRate").value) / 100;
    const increaseInterestRate = parseFloat(document.getElementById("increaseInterestRate").value) / 100;
    const initialWealth = parseFloat(document.getElementById("initialWealth").value);
    const inflationRateInput = parseFloat(document.getElementById("inflationRate").value) / 100;
    const increaseInflationRate = parseFloat(document.getElementById("increaseInflationRate").value) / 100;
    const target = parseFloat(document.getElementById("target").value);
    const increaseInvestmentRate = parseFloat(document.getElementById("increaseInvestmentRate").value) / 100;

    if (isNaN(timeHorizon) || isNaN(interestRateInput) || isNaN(increaseInterestRate) ||
        isNaN(initialWealth) || isNaN(inflationRateInput) || isNaN(increaseInflationRate) ||
        isNaN(target) || isNaN(increaseInvestmentRate)) {
        return;
    }

    let res = initialWealth;
    let investmentRate = 1;
    let interestRate = interestRateInput;
    let inflationRate = inflationRateInput;
    let loopRange = timeHorizon - 1;

    const accumulatedWealthSavings = [initialWealth];
    const timepoints = [0];

    for (let i = 0; i <= loopRange; i++) {
        res += (((1 + interestRate) * (timeHorizon - i)) * investmentRate) / ((1 + inflationRate) * (timeHorizon - i));
        accumulatedWealthSavings.push(res);
        timepoints.push(i + 1);
        investmentRate *= (1 + increaseInvestmentRate);
        interestRate += increaseInterestRate;
        inflationRate += increaseInflationRate;
    }

    const annualSaving = target / res;
    document.getElementById("annualSavingResult").innerText = annualSaving.toFixed(2);

    res = initialWealth;
    investmentRate = 1;
    interestRate = interestRateInput;
    inflationRate = inflationRateInput;

    const accumulatedWealthInvestment = [initialWealth];

    for (let i = 0; i <= loopRange; i++) {
        res += (((1 + interestRate) * (timeHorizon - i)) * investmentRate) / ((1 + inflationRate) * (timeHorizon - i));
        accumulatedWealthInvestment.push(res);
        interestRate += increaseInterestRate;
        inflationRate += increaseInflationRate;
    }

    const increaseRateOneOffInvestment = target / res;
    document.getElementById("annualInvestmentResult").innerText = increaseRateOneOffInvestment.toFixed(2);

    updateChart(timepoints, accumulatedWealthSavings, accumulatedWealthInvestment);
}

function updateChart(timepoints, accumulatedWealthSavings, accumulatedWealthInvestment) {
    const ctx = document.getElementById('growthChart').getContext('2d');

    if (chart) {
        chart.destroy(); // Destroy the existing chart before creating a new one
    }

    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: timepoints,
            datasets: [
                {
                    label: 'Accumulated Wealth from Annual Savings',
                    data: accumulatedWealthSavings,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    fill: false
                },
                {
                    label: 'Growth of a One-Off Investment',
                    data: accumulatedWealthInvestment,
                    borderColor: 'rgba(153, 102, 255, 1)',
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Savings and Investment Growth Over Time'
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Time (years)'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Accumulated Wealth'
                    }
                }
            }
        }
    });
}