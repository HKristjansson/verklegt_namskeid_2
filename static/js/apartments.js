$(document).ready(function() {
    $('#search-btn').on('click',function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/apartments?search_filter=' + searchText,
                type: 'GET',
                success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return '<div class="well apartment">
                        <a href="/apartments/${d.id}">
                        <img class="apartment-img" src="${d.firstImage}" />
                        <h4>${d.address}</h4>
                        <p>${d.description}</p>
                    </a>
                    </div>'
                });
                $('.apartments').html(newHtml.join(''));
                $('#search-box').val( '');
            },
            error: function(xhr, ststus, error) {
                //todo: Show toastr
                console.log((error);
            }
        })

    });
});