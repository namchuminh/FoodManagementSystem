$(document).ready(function() {
    lineChart();
    $(window).resize(function() {
        window.lineChart.redraw();
        window.donutChart.redraw();
        window.pieChart.redraw();
    });
});

function lineChart() {
    window.lineChart = Morris.Line({
        element: 'line-chart',
        data: [
            { y: '1', a: 100},
            { y: '2', a: 75},
            { y: '3', a: 50},
            { y: '4', a: 75},
            { y: '5', a: 50},
            { y: '6', a: 75},
            { y: '7', a: 100},
            { y: '8', a: 100},
            { y: '9', a: 100},
            { y: '10', a: 100},
            { y: '11', a: 100},
            { y: '12', a: 100}
        ],
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Tháng'],
        lineColors: ['#009688'],
        lineWidth: '3px',
        resize: true,
        redraw: true
    });
}

