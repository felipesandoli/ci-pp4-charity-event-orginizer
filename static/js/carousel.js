// From codeply example https://www.codeply.com/go/EIOtI7nkP8/bootstrap-carousel-with-multiple-cards
if (window.matchMedia("(min-width:768px").matches) {
    $('.carousel .carousel-item').each(function() {
        let itemPerSlide = 4;
        let next = $(this).next();
        if (next.length === 0) {
            next = $(this).siblings(':first');
        }
        next.children(':first-child').clone().appendTo($(this));
    
        for (let i = 0; i < itemPerSlide; i++) {
            next = next.next();
            if (next.length === 0) {
                next = $(this).siblings(':first');
            }
            
            next.children(':first-child').clone().appendTo($(this));
        }
    });    
}
