// Get the context of the canvas element we want to select
var ctx = document.getElementById('myChart').getContext('2d');

// Create a new Chart object
var myChart = new Chart(ctx, {
    type: 'doughnut', // The type of chart we want to create
    data: {
        labels: ['Match', 'Not Matched'], // Labels for the chart
        datasets: [{
            data: [score, 100-score], // Data points for the chart
            backgroundColor: [
                '#ffffff',
                '#219ebc',
            ],
        }]
    },
    options: {
        plugins: {
            legend: {
                labels: {
                    font: {
                        family: 'DM Serif Text' //set legend fon family
                    },
                    color: 'white' // set legend font color
                }
            }
        }
    }
});