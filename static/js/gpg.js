;(function($document, $page, $navbar_li) {
    var $pages = {};
    var pages = [
        'home', 
        'playing_the_game', 
        'rules',
        'connections',
        'about', 
        'history',
        'hesse', 
        'current_playing', 
        'cards', 
        'contact', 
        'links'
    ];
    var all_pages = pages;
    $.map(all_pages, function(id) { $pages[id] = $('#' + id); });
    
    // HTML5 Routing 
    var routing = Davis(function() {
        var self = this;
        // Here we merge the pages array with a blank string to account for no path
        $.map(_.union([''], pages), function(page) {
            self.get('/' + page, function() {
                if (page == '')
                    page = 'home';
                set_page(page);
            });
        });
    });
    routing.configure(function(config) {
        config.linkSelector = 'a[class!=picture]';
        config.formSelector = '_form';
    })
    routing.start();
    var noop = function() {};
    //routing.logger = { info: noop, warning: noop, error: noop };

    function set_page(id) {
        $page.hide();
        $navbar_li.removeClass('active');
        $pages[id].show();
        var linkurl = id === 'home' ? '' : id;
        $('a[href="/' + linkurl + '"]', $navbar_li).parent().addClass('active');
        $document.trigger('set-page-' + id)
    }

    $('.card').hover(function() {
        $(this).append('<strong>' + $(this).data('card') + '</strong>').find('img').hide();
    }, function() {
        $(this).find('img').show().siblings('strong').remove();

    });

    $('[data-api=game]').on('api-deleted', function(e, id) {
        $('[data-id=' + id + ']').parents('.game').fadeOut(function() {
            $(this).remove();
        });
    })

    var csrf = $('meta[name="csrf-token"]').attr('content');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrf)
            }
        }
    });
})($(document), $('.page'), $('#menu li'));