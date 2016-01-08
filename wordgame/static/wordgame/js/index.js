$('.toggle').on('click', function() {
  $('.container').stop().addClass('active');
});

$('.close').on('click', function() {
  $('.container').stop().removeClass('active');
});

error = $('.error').text();
if (error) {
	$('.container').stop().addClass('active');
}
