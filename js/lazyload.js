;
(function() {
    // Initialize
    var bLazy = new Blazy({
        breakpoints: [{
                width: 480 // max-width
                    ,
                src: 'data-src-small'
            },
            {
                width: 1000,
                src: 'data-src-med'
            }
        ],
        container: '#scrolling-container',
    });
})();