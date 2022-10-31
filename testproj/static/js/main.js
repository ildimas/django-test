$('.arrow').on('click', function(e) {
    e.preventDefault;
    $(this).toggleClass('arrow_active');});
$('.navBarActivateBtn').on('click', function(e) {
    e.preventDefault;
    $(this).toggleClass('navBarActivateBtn_active');});
    $('.navBarActivateBtn_active').on('click', function(e) {
        e.preventDefault;
        $(this).toggleClass('navBarActivateBtn');});