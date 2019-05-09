$(document).ready(function() {
    $('#search-apa').on('click',function(e) {
        e.preventDefault();
        var searchText = $('.search-form').val();
        $.ajax({
            url: '/apartments/search_apartment/?search_filter=' + searchText,
                type: 'GET',
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