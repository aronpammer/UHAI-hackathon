
		var presets = window.chartColors;
		var utils = Samples.utils;
		var inputs = {
			min: 8,
			max: 16,
			count: 8,
			decimals: 2,
			continuity: 1
		};

		function generateData() {
			// radar chart doesn't support stacked values, let's do it manually
			var values = utils.numbers(inputs);
			inputs.from = values;
			return values;
		}

		function generateLabels(config) {
			return utils.months({count: inputs.count});
		}

		utils.srand(42);
        console.log(generateLabels());
		var data = {
			labels: ["20", "25", "30", "35", "40", "45", "50"],
			datasets: [{
				backgroundColor: utils.transparentize(presets.red),
				borderColor: presets.red,
				data: [75, 92, 88, 90, 72, 88, 89],
				label: 'Health score'
			}]
		};

		var options = {
			maintainAspectRatio: true,
			spanGaps: false,
			elements: {
				line: {
					tension: 0.000001
				}
			},
			plugins: {
				filler: {
					propagate: false
				},
				samples_filler_analyser: {
					target: 'chart-analyser'
				}
			}
		};

		var chart = new Chart('chart-0', {
			type: 'radar',
			data: data,
			options: options
		});

		function togglePropagate(btn) {
			var value = btn.classList.toggle('btn-on');
			chart.options.plugins.filler.propagate = value;
			chart.update();
		}

		function toggleSmooth(btn) {
			var value = btn.classList.toggle('btn-on');
			chart.options.elements.line.tension = value? 0.4 : 0.000001;
			chart.update();
		}

		function randomize() {
			inputs.from = [];
			chart.data.datasets.forEach(function(dataset) {
				dataset.data = generateData();
			});
			chart.update();
		}
