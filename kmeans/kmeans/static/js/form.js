
function add_cluster_line(target){
	var $output = $('#output');
	text_line = 'Cluster tag: ' + target['centroid']['tag'] + '<br>' + 'Images real tags: ';
	line = '<img src="' + target['centroid']['path'] + '?' + (new Date().getTime()) + '" style="padding-right: 8px">';
	for (i = 0; i < 5; i++) {
		var im_name = 'sample' + i.toString();
		line += '<img src="' + target[im_name]['path'] + '?' + (new Date().getTime()) +'">';
		text_line = text_line + target[im_name]['tag'] + ' ';
	}
	$output.append('<p>' + text_line + '</p>');
	$output.append('<li>' + line + '</li>');
	$output.append('<br>');
}


$(document).ready(function() {

	var $container = $('#mainContainer');

	$('form').on('submit', function(event) {

		$('#errorAlert').hide();
		$('#successAlert').text('It might take a few minutes...').show();

		$.ajax({
			data : {
				number : $('#nameInput').val()
			},
			type : 'POST',
			url : '/kmean'
		})
		.done(function(data) {

			$('#successAlert').hide();

			if (data.error){
				$('#errorAlert').text(data.error).show();
			}
			else{
				$('#errorAlert').hide();
				var $output = $('#output').remove();
				$('#mainContainer').append('<ul id="output"></ul>');
				$.each(data, function (i, cluster) {
					add_cluster_line(cluster);
				})
			}

		});

		event.preventDefault();

	});

});