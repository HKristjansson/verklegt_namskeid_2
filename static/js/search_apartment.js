$(document).ready(function() {
    $('#search-form').on('submit', function(e) {
        e.preventDefault();
        var searchText = $('[name=search_filter]').val();
        console.log('search text '+searchText);
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
            error: function(xhr, ststus, error) {
                //todo: Show toastr
                console.log(error);
            }
        })

    });
});