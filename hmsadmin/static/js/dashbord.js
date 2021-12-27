const ctx = document.getElementById("chart").getContext('2d');
      const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["jan", "feb", "mar", "april",
          "may", "june", "july"],
          datasets: [{
            label: 'Appointments',
            backgroundColor: ' #84a1c2',
            borderColor: 'rgb(47, 128, 237)',
            data: [300, 400, 200, 500, 800, 900, 200],
          }]
        },
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true,
              }
            }]
          }
        },
      });