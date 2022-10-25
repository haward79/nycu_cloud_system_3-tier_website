
$(document).ready(function ()
{
    update_comments();

    $('#button_addComment').on('click', function ()
    {
        send_comment();
    });
});


function send_comment()
{
    let textarea_comment = $('#textarea_comment');
    let data = JSON.stringify({data: textarea_comment.val()});

    textarea_comment.val('');

    $.ajax({
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        url: 'http://192.168.56.3:5000/',
        data: data,
        dataType: 'json',
        success: update_comments,
        error: function (data)
        {
            alert(data.responseJSON['msg']);
        }
    }).done();
}


function update_comments()
{
    let text_numComments = $('#text_numComments');
    let container_comments = $('#container_comments');

    text_numComments.html('?');
    container_comments.empty();

    $.ajax({
        type: 'GET',
        url: 'http://192.168.56.3:5000/',
        dataType: 'json',
        success: function (data)
        {
            data = data['data'];

            text_numComments.html(data.length);
            
            $.each(data, function (index, comment)
            {
                let div = $(document.createElement('div'));
                let p = $(document.createElement('p'));

                comment = comment.replaceAll(' ', '&nbsp;').replaceAll('\n', '<br />');

                p.html(comment);

                div.addClass('block_comment');

                div.append(p);
                container_comments.append(div);
            });
        },
        error: function () { alert('Failed to get comment list!'); }
    });
}
