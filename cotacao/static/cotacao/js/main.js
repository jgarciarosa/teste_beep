var url = '/api/data/'

window.onload = function() {

    //carrega a pagina
	$(function() {
		cotacao.init();
	});

    //escuta os eventos de click dos botoes da página, passando como paraâmetro sua respectiva cotação
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
	    //passa como parâmetro a cotação do real para inicialização da página
	    init : function(){
            cotacao.get_dados('BRL');
	    },
	    //recebe os dados da api
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
	    //exibe na tela as estatisticas das cotações passadas como parâmetro
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