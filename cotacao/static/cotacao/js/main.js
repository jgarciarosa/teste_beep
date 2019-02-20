var url = '/api/data/'

window.onload = function() {

	$(function() {
		cotacao.init();
	});

	$('.brl').on('click', function(){
	    cotacao.get_dados('BRL');
	});

	$('.ars').on('click', function(){
	    cotacao.get_dados('ARS');
	});

	$('.eur').on('click', function(){
	    cotacao.get_dados('EUR');
	});

	var cotacao = {
	    init : function(){
            cotacao.get_dados('BRL');
	    },
	    get_dados : function(moeda){
	        $.ajax({
                method: "GET",
                url: url,
                success: function(dados){
                    categorias = dados.DIAS
                    series = dados[moeda]
                    cotacao.cria_chart();
                },
                error: function(error_dados){
                    console.log("error")
                    console.log(error_dados)
                },
            })
	    },
	    cria_chart : function(){
	        Highcharts.chart('container', {
	            chart: {
                    type: 'line'
                },
                legend: {
                    enabled: false,
                },
                title: {
                    text: 'Cotação Dólar(USD) x ' + series.nome + ' nos últimos 7 dias:'
                },
                xAxis: {
                    categories: categorias
                },
                yAxis: {
                    allowDecimals: true,
                    title: {
                        text: 'Variação Cambial',
                    },
                },
                series: [{
                    name: 'Dólar X ' + series.nome,
                    data: series.dado,
                }]
            })
	    },
	};
}