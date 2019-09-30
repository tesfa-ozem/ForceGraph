// Shorthand for $( document ).ready()
$(function() {
    $('.filter').on('click',function(){
		$(this).toggleClass('border-white');
		$('.drop-down-container').toggleClass('drop-60');
	});
	
	$('.right-bar-show').on('click', function(){
		$('.right-side-bar').removeClass('l-100');
	});
	
	$('.option-items').on('click',function(){
		$('.right-side-bar').addClass('l-100');
		$('.option-items').removeClass('border-white');
		$(this).toggleClass('border-white');
	})
	
});