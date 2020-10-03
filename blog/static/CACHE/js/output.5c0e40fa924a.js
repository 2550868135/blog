$(function(){var url=window.location.href;if(url.indexOf('user')>=0)
{$(".avail-item").removeClass('active');$(".avail-item").eq(0).addClass('active')}
else if(url.indexOf('picture')>=0){$(".avail-item").removeClass('active');$(".avail-item").eq(4).addClass('active')}
else if(url.indexOf('article')>=0){$(".avail-item").removeClass('active');$(".avail-item").eq(1).addClass('active')}
else if(url.indexOf('item')>=0){$(".avail-item").removeClass('active');$(".avail-item").eq(2).addClass('active')}else if(url.indexOf('data')>=0){$(".avail-item").removeClass('active');$(".avail-item").eq(3).addClass('active')}});;