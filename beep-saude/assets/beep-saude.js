const doAjax = (url, successCallback, errorCallback) => {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            successCallback(this.responseText);
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
};

const doChart = (series, categories) => {
    return Highcharts.chart('chart-container', {
        title: {
            text: 'US Dollar over time'
        },
        subtitle: {
            text: 'how much 1 unit value compare to other currencies'
        },
        xAxis: {
            categories: categories,
            reversed: true,
        },
        yAxis: {
            title: {
                text: ''
            }
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: false
            }
        },
        series: series,
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                chartOptions: {
                    legend: {
                        layout: 'horizontal',
                        align: 'center',
                        verticalAlign: 'bottom'
                    }
                }
            }]
        }
    });
};


document.addEventListener("DOMContentLoaded", function(event) { 
    doAjax(
        "/api/exchange-rates?source=USD&currency=BRL&currency=EUR&currency=ARS", 
        (response) => {
            var data = JSON.parse(response);
            var chart = doChart(data["series"], data["categories"]);
        }
    );
});
