var endpoint = 'https://issue-tracker-zainshafiq.c9users.io/charts/api/data/'
var title = []
var user_profile = []
var tot_views= []

queue()
    .defer(d3.json, endpoint)
    .await(makeGraphs);


function makeGraphs(error, DatabaseTickets) {
    if (error) {
        console.error("makeGraphs error on receiving dataset:", error.statusText);
        throw error;
    }
    // Helper function
    function print_filter(filter){
        var f = eval(filter);
        if (typeof(f.length) != "undefined") {}else{}
        if (typeof(f.top) != "undefined") {f=f.top(Infinity);}else{}
        if (typeof(f.dimension) != "undefined") {f=f.dimension(function(d) { return "";}).top(Infinity);}else{}
        console.log(filter+"("+f.length+") = "+JSON.stringify(f).replace("[","[\n\t").replace(/}\,/g,"},\n\t").replace("]","\n]"));
    }
    
    $(document).ready(function () {
        $.ajax({
            type: "GET",
            url: endpoint,
            datatype:'json',
            success: function(data){
                $(data).each(function(index, value){
                    user_profile.push(value.fields.profile_user);
                    tot_views.push(value.fields.views);
                    title.push(value.fields.title);
                });
            setChart()
            }
        });
    });
    
    
}

function setChart(){
    var ctx = document.getElementById("BarChart").getContext('2d');
    var ctx2 = document.getElementById("PieChart").getContext('2d');
    
    var myChart2 = new Chart(ctx2, {
        type: 'polarArea',
        data: {
            labels: title,
            datasets: [{
                label: 'Total views of single ticket',
                data: tot_views,
                backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
            ],
            }]
        },
    })
    
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: title,
            datasets: [{
                label: 'Total views of single ticket',
                data: tot_views,
                backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
            ],
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        },
    })
}

// var ctx = document.getElementById("myChart").getContext('2d');
// var myChart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//         labels: labels,
//         datasets: [{
//             label: '# of Votes',
//             data: [12, 19, 3, 5, 2, 3],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',
//                 'rgba(153, 102, 255, 0.2)',
//                 'rgba(255, 159, 64, 0.2)'
//             ],
//             borderColor: [
//                 'rgba(255,99,132,1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(75, 192, 192, 1)',
//                 'rgba(153, 102, 255, 1)',
//                 'rgba(255, 159, 64, 1)'
//             ],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero:true
//                 }
//             }]
//         }
//     }
// });

