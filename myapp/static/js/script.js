$(document).ready(function () {
    $(".tab_head").click(function () {
        if ($(this).attr('class').indexOf('expand') == -1) 
        
        $(this).toggleClass("expand").next().slideToggle('fast')

        // $(".tab").not($(this)).removeClass("open");
        $(".collap").not($(this).next()).slideUp('fast');
    });
});
