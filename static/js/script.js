/* Author: 

*/


$(document).ready(function() {

	function showPlayer() {
		var $img = $(this).find('img');
		var $figure = $img.parents("figure");
		var big_url = $img.attr('src').replace('.png', '_big.png');
		var $figure_copy = $figure.clone();
		$figure_copy.find('img').attr('src', big_url);
		
		$player = $('#player');
		$player.children().remove();
		$player.append($figure_copy);
		$('.thumbnails').hide();
		return false;
	}
	
	function showThumbnails(e) {
		$target = $(e.target);
		console.log(e.target.tagName);
		if (e.target.tagName.toUpperCase() == 'IMG' && ($target.attr('id') == '#player' || $target.parents('#player').length > 0)) {
		} else {
			$player = $('#player').children().remove();
			$('.thumbnails').show();
		}
	}
	
	$('section.thumbnails figure.thumbnail a').click(showPlayer);
	$('body').click(showThumbnails);


});




















