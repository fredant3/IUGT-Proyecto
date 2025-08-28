/**
 * Dashboard Analytics
 */

'use strict';

(function () {
  let cardColor, headingColor, axisColor, shadeColor, borderColor;

  cardColor = config.colors.cardColor;
  headingColor = config.colors.headingColor;
  axisColor = config.colors.axisColor;
  borderColor = config.colors.borderColor;

  // Gráfico 1: Barras (Incidencias)
  // --------------------------------------------------------------------
  const optionsBarIncidencia = {
    series: [{
      name: 'Emergencias',
      data: data
    }],
    chart: {
      type: 'bar',
      height: 350
    },
    plotOptions: {
      bar: {
        borderRadius: 4,
        borderRadiusApplication: 'end',
        horizontal: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    xaxis: {
      categories: labels
    },
    colors: [config.colors.primary]
  };

  // Gráfico 2: Torta (Estados)
  // --------------------------------------------------------------------
  const pieChartConfig = {
    chart: {
      height: 350,
      type: 'donut'
    },
    labels: labelsTorta,
    series: dataTorta,
    colors: colorsTorta,
    stroke: {
      width: 2,
      colors: [cardColor]
    },
    dataLabels: {
      enabled: true,
      formatter: function (val, opt) {
          return opt.w.globals.labels[opt.seriesIndex] + ': ' + parseInt(val) + '%';
      }
    },
    legend: {
      position: 'right'
    },
    plotOptions: {
      pie: {
        donut: {
          size: '65%',
          labels: {
            show: true,
            total: {
              show: true,
              label: 'Total',
              formatter: function (w) {
                return w.globals.seriesTotals.reduce((a, b) => a + b, 0);
              }
            }
          }
        }
      }
    }
  };

  // Gráfico 3: Barras (Organismos)
  // --------------------------------------------------------------------
  const optionsBarOrganismos = {
    series: [{
      name: 'Emergencias',
      data: dataOrganismos
    }],
    chart: {
      type: 'bar',
      height: 350
    },
    plotOptions: {
      bar: {
        borderRadius: 4,
        columnWidth: '45%',
        distributed: true,
      }
    },
    dataLabels: {
      enabled: false
    },
    xaxis: {
      categories: labelsOrganismos,
      labels: {
        style: {
          fontSize: '12px'
        }
      }
    },
    colors: colorsOrganismos,
    tooltip: {
      y: {
        formatter: function(val) {
          return val + " emergencias";
        }
      }
    }
  };

  // Renderizar gráficos
  const chartBarIncidencia = document.querySelector('#idFirstStatisticsChart');
  if (chartBarIncidencia) {
    new ApexCharts(chartBarIncidencia, optionsBarIncidencia).render();
  }

  const chartPieEstados = document.querySelector('#idSecondStatisticsChart');
  if (chartPieEstados) {
    new ApexCharts(chartPieEstados, pieChartConfig).render();
  }

  const chartBarOrganismos = document.querySelector('#idThirdStatisticsChart');
  if (chartBarOrganismos) {
    new ApexCharts(chartBarOrganismos, optionsBarOrganismos).render();
  }
})();
