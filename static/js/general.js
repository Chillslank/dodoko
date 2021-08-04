$(document).ready(function(){
    $('#btn_likes').click(function() {    
        var name = $('#username_likes').val();
        var game = $('#gameId_likes').val();
        $.get("/game/category/page/likes/",{'username':name, 'game':game}, 
        function(ret){ 
            if (ret == "success") {
                alert("your thumbs up!");
                window.location.reload()
            }
        });
    });
    
    $('#btn_comment').click(function() {
        var name = $('#username_comments').val();
        var game = $('#gameTitle_comments').val();
        var comment = $('#comment_comments').val();
        $.get("/game/category/page/comments/",{'username':name, 'game':game, 'comment':comment},
        function(ret){
            if (ret == "success") {
                alert("posted");
                window.location.reload()
            }
        });
    });

    $('#game_wishlist').click(function() {
        var name = $('#username_likes').val();
        var url = $('#game_url').val();
        var title = $('#gameId_likes').val();
        $.get("/game/category/page/wishlist/",{'username':name, 'url':url, 'title':title},
        function(ret){
            if (ret == "success") {
                //$("#disappare").fadeIn().delay(3000).hide(300);
                alert("success add to wish list");
                window.location.reload()
            }else if(ret == "have"){
                alert("you already have")
            }
        });
    });

    
});

function del_comment(obj){
    
    var res = confirm('Comfirm Delete?');  
    if(res == true)
    {
        var content = obj.value
        $.get("/game/account/delete_comment/",{'content':content},
        function(ret){
            if (ret == "success") {
                window.location.reload()
            }
        });
    }
}

function del_wishlist(obj){
    
    var res = confirm('Comfirm Delete?');  
    if(res == true)
    {
        var content = obj.value
        $.get("/game/account/delete_wishlist/",{'content':content},
        function(ret){
            if (ret == "success") {
                window.location.reload()
            }
        });
    }
}
