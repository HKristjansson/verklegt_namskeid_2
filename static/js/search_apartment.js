$(document).ready(function() {
    $('#search-form').on('submit', function(e) {
        e.preventDefault();
        var searchText = $('[name=search_filter]').val();
        $.ajax({
            url: '/apartments/search_apartment/?search_filter=' + searchText,
                type: 'GET',
                data: $('#search-form').serialize(),
                success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="well apartment">
                        <a href="/apartments/${d.id}">
                        <img class="apartment-img" alt="building" src="${d.firstImage}" />
                        <h4>${d.address}</h4>
                        <p>${d.description}</p>
                    </a>
                    </div>`
                });
                $('.apartments-index').html(newHtml.join(''));
                $('.search-form').val( '');
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        })

    });
});

$(document).ready(function() {
    $('#search-history-form').on('submit', function(e) {
        e.preventDefault();
        var searchText = $('[name=search_history]').val();
        $.ajax({
            url: '/apartments/search_apartment/?search_history=' + searchText,
                type: 'GET',
                data: $('#search-history').serialize(),
                    success: function(resp) {
                    var newHtml = resp.data.map(d => {
                        return `<div class="well apartment">
                            <a href="/apartments/${d.id}">
                            <img class="apartment-img" alt="building" src="${d.firstImage}" />
                            <h4>${d.address}</h4>
                            <p>${d.description}</p>
                        </a>
                        </div>`
                    });
                    $('.apartments-index').html(newHtml.join(''));
                    $('.search-form').val( '');
                },
            error: function(xhr, status, error) {
                console.log(error);
            }
        })

    });
});
