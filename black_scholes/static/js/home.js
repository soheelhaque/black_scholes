var color = Chart.helpers.color;

var numDataPointsExpected = 0;
var numDataPointsDone = 0;

window.chartColors = {
    red: 'rgb(204, 0, 0)',
    orange: 'rgb(255, 159, 64)',
    yellow: 'rgb(255, 205, 86)',
    green: 'rgb(75, 192, 192)',
    blue: 'rgb(0, 0, 204)',
    purple: 'rgb(153, 102, 255)',
    grey: 'rgb(201, 203, 207)'
};

var scatterChartData = {
    datasets: [{
        label: 'Price Today',
        borderColor: window.chartColors.blue,
        backgroundColor: color(window.chartColors.blue).alpha(0.2).rgbString(),
        fill: false,
        showLine: true,
        lineTension: 0,
        data: []
    }, {
        label: 'Payoff At Maturity',
        borderColor: window.chartColors.red,
        backgroundColor: color(window.chartColors.red).alpha(0.2).rgbString(),
        fill: false,
        showLine: true,
        lineTension: 0,
        data: []
    }]
};

function calcOptionPrices() {

    reset();

    var call_put = $('input[name=call_put]:checked').val();
    var strike_price = parseFloat($("#strike_price").val());
    var option_maturity_years = parseFloat($("#option_maturity_years").val());
    var option_maturity_for_payoff = 0.001; //zero gives an arithmetic error, so choose a small value
    var volatility_percent = parseFloat($("#volatility_percent").val());
    var risk_free_rate_percent = parseFloat($("#risk_free_rate_percent").val());

    for (var price = Math.max(strike_price -10, 1); price <= strike_price+10; ++price) {
        calculate(updateOptionPrices, call_put, strike_price, option_maturity_years, price, volatility_percent, risk_free_rate_percent);
        ++numDataPointsExpected;
        calculate(updatePayoffs, call_put, strike_price, option_maturity_for_payoff, price, volatility_percent, risk_free_rate_percent);
        ++numDataPointsExpected;
    }
}

function reset() {
    numDataPointsExpected = 0;
    numDataPointsDone= 0;
    scatterChartData["datasets"][0]["data"] = [];
    scatterChartData["datasets"][1]["data"] = [];
}


/* JQuery Syntax: $(selector).action()
$() is shorthand for jQuery()
# denotes selector for an HTML id
. denotes selector for an HTML class */
function calculate(resultsHandler, call_put, strike_price, option_maturity_years, current_price, volatility_percent, risk_free_rate_percent) {
    let ajax_options = {
        type: 'POST',
        url: 'api/calculator',
        accepts: 'application/json',
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify({
            'call_put': call_put,
            'strike_price': strike_price,
            'option_maturity_years': option_maturity_years,
            'current_price': current_price,
            'volatility_percent': volatility_percent,
            'risk_free_rate_percent': risk_free_rate_percent})
    };
    $.ajax(ajax_options)
    .done(function(data) {
        resultsHandler(current_price, data);
    })
    .fail(function(jqXHR, textStatus, errorThrown) {
        let err_details = JSON.stringify(jqXHR.responseJSON);
        let error_msg = textStatus + ': ' + errorThrown + '\n' + err_details;
        alert(error_msg);
    });
}

function calcOptionPrice() {
    var call_put = $('input[name=call_put]:checked').val();
    var strike_price = parseFloat($("#strike_price").val());
    var option_maturity_years = parseFloat($("#option_maturity_years").val());
    var current_price = parseFloat($("#current_price").val());
    var volatility_percent = parseFloat($("#volatility_percent").val());
    var risk_free_rate_percent = parseFloat($("#risk_free_rate_percent").val());

    calculate(updateOptionPrice, call_put, strike_price, option_maturity_years, current_price, volatility_percent, risk_free_rate_percent);
}

function updateOptionPrices(price, optionPrice) {
    scatterChartData["datasets"][0]["data"].push({
            x: price,
            y: optionPrice
        })
    ++numDataPointsDone;
    drawChart();
}

function updatePayoffs(price, payoff) {
    scatterChartData["datasets"][1]["data"].push({
            x: price,
            y: payoff
        })
    ++numDataPointsDone;
    drawChart();
}

function updateOptionPrice(price, optionPrice) {
    $("#optionprice").text(optionPrice);
}

function drawChart() {
    // Only draw the chart once we have all the data points. Needed because of the
    // asynchronous nature of the Ajax calls
    if(numDataPointsDone >= numDataPointsExpected) {
        
        // First, sort the arrays, so that the lines connect points from left to right
        scatterChartData["datasets"][0]["data"].sort(compare)
        scatterChartData["datasets"][1]["data"].sort(compare)

        // Now update the graph if it exists, otherwise create it
        if(window.myScatter) {
            window.myScatter.update();
        } else {
            var ctx = document.getElementById('canvas').getContext('2d');
            window.myScatter = new Chart(ctx, {
                type: 'scatter',
                data: scatterChartData,
                options: {
                    title: {
                        display: true,
                        text: 'Option Price & Payoff'
                    }
                }
            });
        }
    }
}

// Helper function, needed to sort arrays holding charting data
function compare(a, b) {
    var comparison = 0;

    if(a.x > b.x) {
      comparison = 1;
    } else if (a.x < b.x) {
      comparison = -1;
    }
    return comparison;
}

// When the calculate button is pressed, calculate the option price and redraw the chart
$("#calculate").click(function() {
    calcOptionPrice();
    calcOptionPrices();
});
