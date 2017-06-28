$(function() {
	var $timeStamp = $('.jsc-time-stamp');
	setInterval(function(){
		var now = new Date(),
			yyyy = now.getFullYear(),
			mm = ('0'+(now.getMonth() + 1)).slice(-2),
			dd = ('0'+now.getDate()).slice(-2),
			hh = ('0'+now.getHours()).slice(-2),
			mi = ('0'+now.getMinutes()).slice(-2),
			ss = ('0'+now.getSeconds()).slice(-2);
		$timeStamp.text(yyyy + '/' + mm + '/' + dd + ' '  + hh + ':' + mi + ' ' + ss);
	}, 1000);
	$('.jsc-radio-label').on('click', function(){
		var $parent = $(this).closest('.jsc-form-name-group');
		if (!$parent.hasClass('is-checked')) {
			$parent.addClass('is-checked');
		}
		if ($('.jsc-form-name-group').size() <= $('.is-checked').size()) {
			$('.jsc-submit-button').removeClass('is-disabled');
		}
	});
	$('.jsc-submit-button').on('click', function(){
		if(!$(this).hasClass('is-disabled')){
			$('.jsc-modal').addClass('is-show');
		}
	});

});
